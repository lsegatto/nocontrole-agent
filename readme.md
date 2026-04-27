🛰️ NOControle Agent — AI Copilot for NOC Operations

AI-powered copilot for Network Operations Centers (NOC), designed to assist analysts in incident analysis, prioritization, and operational decision-making.

Este projeto simula um assistente operacional capaz de analisar incidentes, priorizar clientes, integrar dados de monitoramento e chamados (OTRS/Zabbix) e apoiar a tomada de decisão em tempo real.

---

## 🚀 Funcionalidades

- 💬 Chat estilo IA (terminal)
- 🧠 Memória de conversa (contexto)
- 📊 Análise de ambiente (status geral)
- 🚨 Detecção automática de clientes críticos
- 🔥 Priorização baseada em severidade + impacto
- 📋 Integração simulada com:
  - OTRS (chamados)
  - Zabbix (monitoramento)
- 🧾 Geração de relatórios automáticos (.txt)
- 🎨 Interface colorida no terminal (Rich)

---

## 🧠 Exemplo de uso

```bash
python chat.py

### 💬 Perguntas suportadas

-Como está o ambiente?
-Tem algo crítico?
-Qual cliente está pior?
-Quais chamados estão abertos?
-O que devo fazer agora?
-Cliente 9
-Gera relatório


### 📁 Estrutura do projeto

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

---

## 📌 Disclaimer

This project is a simulation and does not connect to real OTRS or Zabbix environments.  
All data is mocked for study and demonstration purposes.

---
