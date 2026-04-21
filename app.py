import os
import sys
import time
from datetime import datetime

NOME = "AInicial"
VERSAO = "1.0"


class Cores:
    RESET = "\033[0m"
    ROXO = "\033[95m"
    AZUL = "\033[94m"
    CIANO = "\033[96m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    VERMELHO = "\033[91m"
    BRANCO = "\033[97m"
    CINZA = "\033[90m"
    NEGRITO = "\033[1m"


def suporta_ansi():
    return sys.stdout.isatty()


def cor(texto, estilo):
    if suporta_ansi():
        return f"{estilo}{texto}{Cores.RESET}"
    return texto


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def digitar(texto, velocidade=0.015):
    for caractere in texto:
        print(caractere, end="", flush=True)
        time.sleep(velocidade)
    print()


def linha(char="═", tamanho=70):
    print(cor(char * tamanho, Cores.CINZA))


def titulo():
    limpar_tela()
    linha()
    print(cor(f"{'🤖  ' + NOME + ' - Assistente Virtual':^70}", Cores.NEGRITO + Cores.ROXO))
    print(cor(f"{'Demonstração local em Python | Versão ' + VERSAO:^70}", Cores.CIANO))
    linha()
    print(cor(" Digite 'menu' para opções rápidas | 'limpar' para limpar a tela | 'sair' para encerrar", Cores.AMARELO))
    linha()


def saudacao_horario():
    hora = datetime.now().hour
    if 5 <= hora < 12:
        return "Bom dia"
    if 12 <= hora < 18:
        return "Boa tarde"
    return "Boa noite"


def horario():
    return datetime.now().strftime("%H:%M")


def data_atual():
    return datetime.now().strftime("%d/%m/%Y")


def pensando():
    print()
    print(cor(f"{NOME}: analisando", Cores.AZUL), end="", flush=True)
    for _ in range(3):
        time.sleep(0.35)
        print(cor(".", Cores.AZUL), end="", flush=True)
    print("\n")


def caixa(texto):
    partes = texto.split("\n")
    largura = max(len(p) for p in partes) + 4
    print(cor("╔" + "═" * largura + "╗", Cores.CINZA))
    for p in partes:
        print(cor("║ ", Cores.CINZA) + p.ljust(largura - 2) + cor(" ║", Cores.CINZA))
    print(cor("╚" + "═" * largura + "╝", Cores.CINZA))


def menu():
    caixa(
        "MENU RÁPIDO\n"
        "1. Quem é você?\n"
        "2. O que é Python?\n"
        "3. O que é inteligência artificial?\n"
        "4. Que horas são?\n"
        "5. Fale sobre estudos\n"
        "6. Fale sobre trabalho\n"
        "7. Fale sobre jogos\n"
        "8. Fale sobre família\n"
        "9. O que você faz?\n"
        "0. Sair"
    )


def intro():
    titulo()
    digitar(cor(f"{NOME}: {saudacao_horario()}! Eu sou a {NOME}.", Cores.VERDE))
    digitar(cor(f"{NOME}: Estou pronta para conversar e participar da sua apresentação.", Cores.VERDE))
    print()
    menu()


def responder_menu(opcao):
    mapa = {
        "1": "quem é você",
        "2": "python",
        "3": "inteligência artificial",
        "4": "que horas são",
        "5": "fale sobre estudos",
        "6": "fale sobre trabalho",
        "7": "fale sobre jogos",
        "8": "fale sobre família",
        "9": "o que você faz",
        "0": "sair",
    }
    return mapa.get(opcao, "")


def responder(pergunta):
    p = pergunta.lower().strip()

    cumprimentos = ["oi", "olá", "ola", "opa", "e aí", "e ai", "hello", "oii"]
    if p in cumprimentos:
        return (
            f"{saudacao_horario()}! Eu sou a {NOME}, uma assistente virtual criada em Python. "
            "É um prazer conversar com você."
        )

    if "seu nome" in p or "qual é o seu nome" in p or "qual e o seu nome" in p:
        return f"Meu nome é {NOME}. Sou uma assistente virtual criada para demonstração e evolução futura."

    if "quem é você" in p or "quem e voce" in p:
        return (
            f"Eu sou a {NOME}, uma assistente virtual em Python. "
            "Fui criada para conversar, responder perguntas simples e mostrar como um projeto pode ganhar vida no terminal."
        )

    if "quem te criou" in p or "quem criou você" in p or "quem criou voce" in p:
        return (
            "Fui criada como parte de um projeto de aprendizado e apresentação. "
            "Hoje sou uma demonstração local, mas posso evoluir bastante."
        )

    if "o que você faz" in p or "o que voce faz" in p:
        return (
            "No momento, eu converso com você usando lógica e respostas programadas. "
            "Meu objetivo é mostrar a base de um assistente virtual que pode ficar cada vez mais inteligente."
        )

    if "python" in p:
        return (
            "Python é uma linguagem de programação muito popular, conhecida por sua sintaxe simples e poderosa. "
            "Ela é muito usada em automação, análise de dados, desenvolvimento web e inteligência artificial."
        )

    if "inteligência artificial" in p or "inteligencia artificial" in p or p == "ia":
        return (
            "Inteligência artificial é a área da tecnologia que busca criar sistemas capazes de analisar informações, "
            "reconhecer padrões, responder perguntas e ajudar na tomada de decisões."
        )

    if "hora" in p or "horas" in p:
        return f"Agora são {horario()}."

    if "data" in p or "dia de hoje" in p:
        return f"Hoje é {data_atual()}."

    if "estudo" in p or "estudar" in p or "aprender" in p:
        return (
            "Aprender um pouco por dia costuma gerar resultados enormes no longo prazo. "
            "Constância, prática e curiosidade fazem muita diferença."
        )

    if "trabalho" in p or "carreira" in p or "profissão" in p or "profissao" in p:
        return (
            "Uma carreira em tecnologia é construída com prática, evolução contínua e vontade de aprender. "
            "Cada projeto é uma chance de crescer."
        )

    if "jogo" in p or "jogos" in p or "game" in p or "games" in p:
        return (
            "Jogos são uma ótima forma de entretenimento e, em muitos casos, também estimulam raciocínio, estratégia e criatividade."
        )

    if "família" in p or "familia" in p:
        return (
            "A família costuma ser o melhor primeiro público para uma demonstração. "
            "É especial mostrar a evolução de um projeto para pessoas importantes."
        )

    if "tudo bem" in p or "como vai" in p or "como você está" in p or "como voce esta" in p:
        return "Estou funcionando muito bem e feliz por participar desta apresentação."

    if "bonita" in p or "legal" in p or "inteligente" in p:
        return "Muito obrigada. Estou em fase inicial, mas fui feita com bastante cuidado."

    if "menu" in p or "ajuda" in p or "help" in p:
        return (
            "Você pode digitar perguntas livremente ou usar o menu numérico.\n"
            "Exemplos:\n"
            "- Quem é você?\n"
            "- O que é Python?\n"
            "- O que é inteligência artificial?\n"
            "- Que horas são?\n"
            "- Fale sobre estudos\n"
            "- Fale sobre trabalho"
        )

    if "obrigado" in p or "obrigada" in p or "valeu" in p:
        return "Eu que agradeço. Foi muito bom conversar com você."

    return (
        "Ainda estou em desenvolvimento, então não sei responder tudo por enquanto. "
        "Mas já consigo conversar sobre tecnologia, estudos, trabalho, jogos, data, horário e assuntos simples."
    )


def executar():
    intro()

    while True:
        entrada = input(cor("\nVocê: ", Cores.NEGRITO + Cores.BRANCO)).strip()

        if not entrada:
            digitar(cor(f"{NOME}: Você não digitou nada. Tente escrever uma pergunta.", Cores.AMARELO))
            continue

        if entrada.lower() == "limpar":
            titulo()
            continue

        if entrada.lower() in ["menu", "ajuda", "help"]:
            menu()
            continue

        entrada_convertida = responder_menu(entrada)
        if entrada_convertida:
            entrada = entrada_convertida

        if entrada.lower() in ["sair", "exit", "quit", "0"]:
            pensando()
            digitar(cor(f"{NOME}: Até mais! Foi um prazer conversar com você.", Cores.VERDE))
            linha()
            break

        pensando()
        resposta = responder(entrada)
        digitar(cor(f"{NOME}: {resposta}", Cores.VERDE))


if __name__ == "__main__":
    executar()