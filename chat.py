from agent import responder, alertas_iniciais
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

console = Console()

def mostrar_banner():
    banner = Text()
    banner.append("🛰️ NOControle Agent v4\n", style="bold #789c33")
    banner.append("Copiloto operacional para NOC", style="bold cyan")

    console.print(Panel(
        banner,
        title="[bold white]NOControle[/bold white]",
        border_style="#789c33"
    ))

def destacar_linhas(texto):
    linhas = texto.split("\n")
    resultado = Text()

    for linha in linhas:
        linha_lower = linha.lower()

        if "alto" in linha_lower or "sev1" in linha_lower or "disaster" in linha_lower or "indisponibilidade" in linha_lower:
            resultado.append(linha + "\n", style="bold red")

        elif "moderado" in linha_lower or "sev2" in linha_lower or "perda alta" in linha_lower or "latência alta" in linha_lower:
            resultado.append(linha + "\n", style="bold yellow")

        elif "baixo" in linha_lower or "normal" in linha_lower or "nenhum" in linha_lower or "estável" in linha_lower:
            resultado.append(linha + "\n", style="bold green")

        elif "direcionamento" in linha_lower or "recomendação" in linha_lower or "recomendações" in linha_lower or "plano de ação" in linha_lower:
            resultado.append(linha + "\n", style="bold #789c33")

        elif "ticket" in linha_lower or "otrs" in linha_lower or "chamado" in linha_lower:
            resultado.append(linha + "\n", style="bold cyan")

        elif "monitoramento" in linha_lower or "zabbix" in linha_lower or "trigger" in linha_lower:
            resultado.append(linha + "\n", style="bold magenta")

        elif "cliente" in linha_lower or linha.strip().startswith("📍") or linha.strip().startswith("📌") or linha.strip().startswith("🚨"):
            resultado.append(linha + "\n", style="bold white")

        else:
            resultado.append(linha + "\n", style="white")

    return resultado

def imprimir_resposta(titulo, texto, cor="blue"):
    console.print(Panel(
        destacar_linhas(texto),
        title=f"[bold cyan]{titulo}[/bold cyan]",
        border_style=cor
    ))

def main():
    mostrar_banner()

    imprimir_resposta(
        "Alertas Iniciais",
        alertas_iniciais(),
        cor="red"
    )

    console.print("[bold yellow]Digite sua pergunta ou 'sair' para encerrar.[/bold yellow]")
    console.print("[dim]Ex: resumo executivo | alertas atuais | como está o ambiente? | qual cliente está pior?[/dim]\n")

    while True:
        pergunta = Prompt.ask("[bold #789c33]Você[/bold #789c33]")

        if pergunta.lower() in ["sair", "exit", "quit"]:
            console.print("\n[bold red]NOControle encerrado.[/bold red]")
            break

        resposta = responder(pergunta)

        imprimir_resposta(
            "NOControle",
            resposta,
            cor="#002053"
        )

if __name__ == "__main__":
    main()