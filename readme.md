# 🛰️ NOControle Agent — AI Copilot for NOC Operations

AI-powered copilot for Network Operations Centers (NOC), designed to assist analysts in incident analysis, prioritization, operational decision-making and report generation.

Este projeto simula um assistente operacional capaz de analisar incidentes, priorizar clientes, integrar dados simulados de monitoramento e chamados (OTRS/Zabbix) e apoiar a tomada de decisão em tempo real.

---

## 🎯 Objetivo

Criar um copiloto operacional para NOC capaz de:

- Reduzir tempo de análise
- Centralizar informações operacionais
- Priorizar incidentes por severidade e impacto
- Simular integrações com ferramentas como OTRS e Zabbix
- Gerar relatórios operacionais automaticamente

---

## 🚀 Funcionalidades

- 💬 Chat estilo IA no terminal
- 🧠 Memória de conversa e contexto
- 📊 Análise geral do ambiente
- 🚨 Detecção automática de clientes críticos
- 🔥 Priorização baseada em severidade, impacto e monitoramento
- 📋 Integração simulada com:
  - OTRS (chamados)
  - Zabbix (monitoramento)
- 🧾 Geração de relatórios automáticos em `.txt`
- 🎨 Interface colorida no terminal com Rich
- 📌 Modo gestor / resumo executivo
- ⚠️ Alertas automáticos ao iniciar

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Rich
- JSON
- Git/GitHub

---

💬 Exemplos de uso:

---

## 📊 Análise do Ambiente:

Você: Como está o ambiente?

NOControle:
Resumo executivo do ambiente com status, riscos e prioridades.

---
## 🚨 Verificação de críticos:

Você: Tem algo crítico?

NOControle:
Lista de clientes com maior prioridade e risco.

---

## 🔍 Consulta de cliente:

Você: Cliente 9

NOControle:
- Status
- Severidade
- Ticket
- Impacto
- Próximo passo
- Monitoramento
- OTRS

---
## 🧠 Memória de contexto:

Você: Cliente 9
Você: Qual o ticket?
Você: Quem está cuidando?

NOControle:
Responde sem precisar repetir o cliente.

---
## 🧾 Geração de relatório:

Você: Gera relatório do cliente 9

NOControle:
Arquivo gerado em /relatorios

---

## 🧪 Dados simulados:
Este projeto utiliza dados fictícios para simular:

-Clientes e ambientes de rede
-Incidentes e degradações
-Chamados OTRS
-Alertas de monitoramento (Zabbix)
-SLA, impacto e priorização

---
## 🚧 Roadmap:
Evoluções planejadas:

-Integração real com OTRS (API)
-Integração real com Zabbix
-Uso de IA (OpenAI ou modelo local)
-Implementação de MCP (Model Context Protocol)
-Histórico persistente de conversas
-Interface web
-Exportação de relatórios em PDF

---

## 📁 Estrutura do projeto

```text
nocontrole-agent/
│
├── agent.py
├── chat.py
├── tools.py
├── data.json
│
├── data/
│   ├── otrs_fake.json
│   └── zabbix_fake.json
│
├── relatorios/
├── requirements.txt
└── README.md
```
## 👨‍💻 Autor

Lucas Antonucci Segatto Zampini
