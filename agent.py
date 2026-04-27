from tools import listar_clientes, analisar_cliente, buscar_otrs, buscar_zabbix
import os
from datetime import datetime

ultimo_cliente = None
memoria = {
    "ultimo_cliente": None,
    "ultima_intencao": None,
    "ultimas_perguntas": [],
    "ultimas_respostas": []
}

def normalizar(texto):
    return texto.lower().strip()

def contem(pergunta, palavras):
    return any(p in pergunta for p in palavras)

def salvar_memoria(pergunta, resposta, cliente=None, intencao=None):
    memoria["ultimas_perguntas"].append(pergunta)
    memoria["ultimas_respostas"].append(resposta)

    if cliente:
        memoria["ultimo_cliente"] = cliente

    if intencao:
        memoria["ultima_intencao"] = intencao

    memoria["ultimas_perguntas"] = memoria["ultimas_perguntas"][-5:]
    memoria["ultimas_respostas"] = memoria["ultimas_respostas"][-5:]

def classificar_clientes():
    dados = listar_clientes()
    resultado = []

    for cliente, info in dados.items():
        alertas, recomendacoes = analisar_cliente(cliente, info)
        score = 0

        if info["severidade"] == "SEV1":
            score += 100
        elif info["severidade"] == "SEV2":
            score += 70
        elif info["severidade"] == "SEV3":
            score += 40

        if info["status"].lower() != "normal":
            score += 20

        if "100%" in info.get("perda", ""):
            score += 30

        zabbix = buscar_zabbix(cliente)
        if zabbix:
            if zabbix["severity"] == "Disaster":
                score += 40
            elif zabbix["severity"] == "High":
                score += 20

        resultado.append({
            "cliente": cliente,
            "info": info,
            "alertas": alertas,
            "recomendacoes": recomendacoes,
            "otrs": buscar_otrs(cliente),
            "zabbix": zabbix,
            "score": score
        })

    return sorted(resultado, key=lambda x: x["score"], reverse=True)

def gerar_texto_relatorio(cliente, info):
    otrs = buscar_otrs(cliente)
    zabbix = buscar_zabbix(cliente)
    alertas, recomendacoes = analisar_cliente(cliente, info)

    texto = f"""
RELATÓRIO OPERACIONAL - NOControle

Cliente: {cliente.title()}
Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

STATUS
- Status: {info['status']}
- Severidade: {info['severidade']}
- Prioridade: {info['prioridade']}
- Ticket: {info['ticket']}
- Impacto: {info['impacto']}
- SLA: {info['sla']}

DADOS TÉCNICOS
- Equipamento: {info['equipamento']}
- Interface: {info['interface']}
- Latência: {info['latencia']}
- Perda: {info['perda']}
- Jitter: {info['jitter']}
- Localidade: {info['localidade']}

ANÁLISE
- Causa provável: {info['causa_provavel']}
- Ação atual: {info['acao']}
- Próximo passo: {info['proximo_passo']}
- Último update: {info['ultimo_update']}
"""

    if zabbix:
        texto += f"""

MONITORAMENTO
- Host: {zabbix['host']}
- Trigger: {zabbix['trigger']}
- Severidade: {zabbix['severity']}
- Evento: {zabbix['ultimo_evento']}
"""

    if otrs:
        texto += f"""

OTRS
- Fila: {otrs['fila']}
- Status: {otrs['status_ticket']}
- Responsável: {otrs['responsavel']}
- Última atualização: {otrs['ultima_atualizacao']}
"""

    if alertas:
        texto += "\nALERTAS\n"
        for a in alertas:
            texto += f"- {a}\n"

    if recomendacoes:
        texto += "\nRECOMENDAÇÕES\n"
        for r in recomendacoes:
            texto += f"- {r}\n"

    return texto

def exportar_relatorio(cliente, info):
    pasta = "relatorios"

    if not os.path.exists(pasta):
        os.makedirs(pasta)

    nome = f"relatorio_{cliente.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    caminho = os.path.join(pasta, nome)

    with open(caminho, "w", encoding="utf-8") as f:
        f.write(gerar_texto_relatorio(cliente, info))

    return caminho

def resumo_executivo():
    lista = classificar_clientes()

    total = len(lista)
    normais = len([c for c in lista if c["info"]["status"] == "normal"])
    incidentes = total - normais
    sev1 = len([c for c in lista if c["info"]["severidade"] == "SEV1"])
    sev2 = len([c for c in lista if c["info"]["severidade"] == "SEV2"])

    resposta = f"""
📌 RESUMO EXECUTIVO

- Total de clientes monitorados: {total}
- Clientes normais: {normais}
- Clientes com incidente/degradação: {incidentes}
- SEV1: {sev1}
- SEV2: {sev2}

Risco operacional: {"ALTO" if sev1 > 0 else "MODERADO" if sev2 > 0 else "BAIXO"}
"""
    return resposta

def alertas_iniciais():
    lista = classificar_clientes()
    criticos = [c for c in lista if c["score"] > 0][:5]

    if not criticos:
        return "✅ Ambiente estável."

    texto = "🚨 ALERTAS ATUAIS\n\n"

    for c in criticos:
        texto += f"{c['cliente'].title()} - {c['info']['status']} ({c['info']['severidade']})\n"

    return texto

def listar_criticos():
    lista = classificar_clientes()
    resposta = "🚨 PRIORIDADES ATUAIS\n\n"

    for c in lista[:6]:
        if c["score"] <= 0:
            continue

        resposta += f"{c['cliente'].title()}\n"
        resposta += f"- Score: {c['score']}\n"
        resposta += f"- Status: {c['info']['status']}\n"
        resposta += f"- Severidade: {c['info']['severidade']}\n"
        resposta += f"- Ticket: {c['info']['ticket']}\n\n"

    return resposta

def pior_cliente():
    lista = classificar_clientes()
    pior = lista[0]

    return f"""
🔥 CLIENTE COM MAIOR PRIORIDADE

{pior['cliente'].title()}

- Score: {pior['score']}
- Status: {pior['info']['status']}
- Severidade: {pior['info']['severidade']}
- Ticket: {pior['info']['ticket']}
- Impacto: {pior['info']['impacto']}
- Próximo passo: {pior['info']['proximo_passo']}
"""

def recomendar_acoes():
    lista = classificar_clientes()
    resposta = "🧠 PLANO DE AÇÃO SUGERIDO\n\n"

    for c in lista[:5]:
        if c["score"] <= 0:
            continue

        resposta += f"{c['cliente'].title()} — {c['info']['prioridade']} / {c['info']['severidade']}\n"

        for r in c["recomendacoes"][:3]:
            resposta += f"- {r}\n"

        resposta += "\n"

    return resposta

def chamados_abertos():
    lista = classificar_clientes()
    resposta = "📋 CHAMADOS ABERTOS / EM TRATAMENTO\n\n"
    encontrou = False

    for c in lista:
        otrs = c["otrs"]
        if otrs and otrs["status_ticket"] in ["aberto", "em tratamento"]:
            encontrou = True
            resposta += f"{c['cliente'].title()}\n"
            resposta += f"- Ticket: {otrs['ticket']}\n"
            resposta += f"- Status: {otrs['status_ticket']}\n"
            resposta += f"- Fila: {otrs['fila']}\n"
            resposta += f"- Responsável: {otrs['responsavel']}\n"
            resposta += f"- Última atualização: {otrs['ultima_atualizacao']}\n\n"

    if not encontrou:
        return "✅ Nenhum chamado aberto encontrado."

    return resposta

def detalhes_cliente(cliente, info):
    otrs = buscar_otrs(cliente)
    zabbix = buscar_zabbix(cliente)
    alertas, recomendacoes = analisar_cliente(cliente, info)

    resposta = f"""
📍 {cliente.title()}

DADOS OPERACIONAIS
- Status: {info['status']}
- Severidade: {info['severidade']}
- Prioridade: {info['prioridade']}
- Ticket: {info['ticket']}
- Impacto: {info['impacto']}
- Próximo passo: {info['proximo_passo']}
"""

    if zabbix:
        resposta += f"""
MONITORAMENTO
- Host: {zabbix['host']}
- Trigger: {zabbix['trigger']}
- Severidade: {zabbix['severity']}
- Último evento: {zabbix['ultimo_evento']}
"""

    if otrs:
        resposta += f"""
OTRS
- Fila: {otrs['fila']}
- Status: {otrs['status_ticket']}
- Responsável: {otrs['responsavel']}
- Última atualização: {otrs['ultima_atualizacao']}
"""

    if alertas:
        resposta += "\nALERTAS\n"
        for a in alertas:
            resposta += f"- {a}\n"

    if recomendacoes:
        resposta += "\nRECOMENDAÇÕES\n"
        for r in recomendacoes:
            resposta += f"- {r}\n"

    return resposta

def buscar_cliente(pergunta):
    dados = listar_clientes()
    for cliente in dados:
        if cliente in pergunta:
            return cliente, dados[cliente]
    return None, None

def responder_contexto(pergunta):
    cliente = memoria["ultimo_cliente"]

    if not cliente:
        return None

    info = listar_clientes()[cliente]
    otrs = buscar_otrs(cliente)
    zabbix = buscar_zabbix(cliente)

    if contem(pergunta, ["ticket", "chamado"]):
        if otrs:
            return f"O ticket do {cliente.title()} é {otrs['ticket']} e está {otrs['status_ticket']}."
        return f"O ticket do {cliente.title()} é {info['ticket']}."

    if contem(pergunta, ["quem", "responsável", "responsavel", "dono"]):
        if otrs:
            return f"O responsável pelo {cliente.title()} no OTRS é {otrs['responsavel']}."
        return f"O responsável pelo {cliente.title()} é {info['tecnico']}."

    if contem(pergunta, ["próximo", "proximo", "e agora", "fazer", "ação", "acao"]):
        return f"O próximo passo do {cliente.title()} é: {info['proximo_passo']}"

    if contem(pergunta, ["monitoramento", "zabbix", "trigger", "alarme"]):
        if zabbix:
            return f"No monitoramento, o {cliente.title()} está com trigger {zabbix['trigger']} ({zabbix['severity']}). Último evento: {zabbix['ultimo_evento']}."
        return f"Não há evento de monitoramento registrado para {cliente.title()}."

    if contem(pergunta, ["impacto"]):
        return f"O impacto do {cliente.title()} é: {info['impacto']}"

    if contem(pergunta, ["causa", "motivo", "problema"]):
        return f"A causa provável do {cliente.title()} é: {info['causa_provavel']}"

    if contem(pergunta, ["relatório", "relatorio", "exportar", "gera relatório", "gerar relatório"]):
        caminho = exportar_relatorio(cliente, info)
        return f"📄 Relatório gerado: {caminho}"

    return detalhes_cliente(cliente, info)

def mostrar_memoria():
    cliente = memoria["ultimo_cliente"] or "nenhum"
    intencao = memoria["ultima_intencao"] or "nenhuma"

    texto = f"""
🧠 MEMÓRIA DO NOControle

- Último cliente em contexto: {cliente}
- Última intenção identificada: {intencao}

Últimas perguntas:
"""
    for p in memoria["ultimas_perguntas"]:
        texto += f"- {p}\n"

    return texto

def responder(pergunta):
    global ultimo_cliente
    pergunta = normalizar(pergunta)

    if contem(pergunta, ["memória", "memoria", "contexto", "o que você lembra"]):
        resposta = mostrar_memoria()
        salvar_memoria(pergunta, resposta, intencao="memoria")
        return resposta

    cliente, info = buscar_cliente(pergunta)

    if contem(pergunta, ["relatório", "relatorio", "gerar relatório", "gera relatório", "exportar"]):
        if cliente:
            ultimo_cliente = cliente
            caminho = exportar_relatorio(cliente, info)
            resposta = f"📄 Relatório gerado: {caminho}"
            salvar_memoria(pergunta, resposta, cliente, "relatorio")
            return resposta

        resposta_contexto = responder_contexto(pergunta)
        if resposta_contexto:
            salvar_memoria(pergunta, resposta_contexto, memoria["ultimo_cliente"], "relatorio")
            return resposta_contexto

        return "Informe o cliente para gerar relatório. Exemplo: gera relatório do cliente 9"

    if cliente:
        ultimo_cliente = cliente
        resposta = detalhes_cliente(cliente, info)
        salvar_memoria(pergunta, resposta, cliente, "detalhe_cliente")
        return resposta

    if contem(pergunta, ["executivo", "gestor", "diretoria", "resumo executivo"]):
        resposta = resumo_executivo()
        salvar_memoria(pergunta, resposta, intencao="resumo_executivo")
        return resposta

    if contem(pergunta, ["alerta", "alertas", "critico", "crítico", "atenção", "atencao"]):
        resposta = listar_criticos()
        salvar_memoria(pergunta, resposta, intencao="alertas")
        return resposta

    if contem(pergunta, ["pior cliente", "cliente pior", "mais crítico", "mais critico", "maior prioridade"]):
        resposta = pior_cliente()
        salvar_memoria(pergunta, resposta, intencao="pior_cliente")
        return resposta

    if contem(pergunta, ["chamados abertos", "tickets abertos", "quais chamados", "quais tickets", "otrs"]):
        resposta = chamados_abertos()
        salvar_memoria(pergunta, resposta, intencao="chamados")
        return resposta

    if contem(pergunta, ["o que devo fazer", "plano", "recomenda", "recomendação", "recomendacao", "ações", "acoes"]):
        resposta = recomendar_acoes()
        salvar_memoria(pergunta, resposta, intencao="plano_acao")
        return resposta

    if contem(pergunta, ["resumo", "geral", "ambiente", "como estamos", "como está o ambiente"]):
        resposta = resumo_executivo()
        salvar_memoria(pergunta, resposta, intencao="resumo_geral")
        return resposta

    resposta_contexto = responder_contexto(pergunta)

    if resposta_contexto:
        salvar_memoria(pergunta, resposta_contexto, memoria["ultimo_cliente"], "contexto")
        return resposta_contexto

    resposta = """
Não entendi totalmente sua pergunta.

Tente algo como:
- resumo executivo
- alertas atuais
- cliente 9
- qual o ticket?
- gera relatório
- o que você lembra?
"""
    salvar_memoria(pergunta, resposta, intencao="fallback")
    return resposta