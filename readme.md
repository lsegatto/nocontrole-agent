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
