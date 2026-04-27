import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def carregar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

dados_clientes = carregar_json(os.path.join(BASE_DIR, "data.json"))
dados_otrs = carregar_json(os.path.join(BASE_DIR, "data", "otrs_fake.json"))
dados_zabbix = carregar_json(os.path.join(BASE_DIR, "data", "zabbix_fake.json"))

def listar_clientes():
    return dados_clientes

def buscar_otrs(cliente):
    return dados_otrs.get(cliente)

def buscar_zabbix(cliente):
    return dados_zabbix.get(cliente)

def extrair_percentual(valor):
    try:
        return int(str(valor).replace("%", "").strip())
    except:
        return 0

def extrair_ms(valor):
    try:
        return int(str(valor).replace("ms", "").strip())
    except:
        return 0

def analisar_cliente(cliente, info):
    alertas = []
    recomendacoes = []

    perda = extrair_percentual(info.get("perda", "0"))
    latencia = extrair_ms(info.get("latencia", "0"))
    status = info.get("status", "").lower()
    severidade = info.get("severidade", "")

    if status != "normal":
        alertas.append(f"Status operacional: {info['status']}")

    if perda >= 10:
        alertas.append(f"Perda alta: {info['perda']}")
        recomendacoes.append("Validar perda no enlace e coletar evidências")

    if latencia >= 100:
        alertas.append(f"Latência alta: {info['latencia']}")
        recomendacoes.append("Validar rota, caminho e possíveis alterações")

    if severidade == "SEV1":
        alertas.append("Incidente SEV1")
        recomendacoes.append("Escalar imediatamente e acompanhar SLA")

    zabbix = buscar_zabbix(cliente)
    if zabbix and zabbix["status_monitoramento"] == "PROBLEM":
        alertas.append(f"Monitoramento: {zabbix['trigger']}")
        recomendacoes.append("Validar evento no monitoramento")

    otrs = buscar_otrs(cliente)
    if otrs and otrs["status_ticket"] in ["aberto", "em tratamento"]:
        recomendacoes.append("Atualizar chamado OTRS com evidências recentes")

    return alertas, recomendacoes