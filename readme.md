# 🛰️ NOControle Agent

Copiloto inteligente para operações de NOC (Network Operations Center).

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
Perguntas Suportadas: 
como está o ambiente?
tem algo crítico?
qual cliente está pior?
quais chamados estão abertos?
o que devo fazer agora?
cliente 9
gera relatório
📁 Estrutura do projeto:
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
🛠 Tecnologias
Python 3
Rich (interface no terminal)
JSON (simulação de dados)
Git/GitHub
🎯 Objetivo:

Simular um assistente inteligente para NOC capaz de:

reduzir tempo de análise
centralizar informações
ajudar na priorização de incidentes
melhorar a tomada de decisão operacional

👨‍💻 Autor

Lucas Segatto


---

# 🧪 Depois disso

No terminal:

```bash
git add .
git commit -m "docs: update README with project details"
git push
