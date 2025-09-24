# 🌐 TNC Gestão - Sistema Web de Gestão de TNCs

Sistema Web para Gestão de **TNCs (Tratativas de Não Conformidades)** com Dashboard Analítico e Gráficos Interativos.

## 🎯 **Objetivo do Sistema**

Desenvolver um sistema web inteligente e responsivo para controle, análise e acompanhamento de TNCs originadas em projetos de engenharia e inspeções técnicas. O sistema substitui o uso de planilhas manuais, permitindo visualização clara de dados, geração de indicadores, controle de status e suporte à tomada de decisão.

## 📁 **Estrutura de Pastas Sugerida**

```
TNC_GESTAO/
├── 📄 app.py                     # Configuração principal Flask
├── 📄 run.py                     # Ponto de entrada da aplicação
├── 📄 main.py                    # Sistema principal (compatibilidade)
├── 📄 requirements.txt           # Dependências do projeto
├── 📄 .env                       # Variáveis de ambiente
├── 📄 .gitignore                 # Arquivos ignorados pelo Git
├── 📄 README.md                  # Documentação principal
├── 📁 app/                       # Código fonte da aplicação
│   ├── 📄 __init__.py            # Inicialização do módulo
│   ├── 📁 main/                  # Blueprint principal
│   │   ├── 📄 __init__.py
│   │   └── 📄 routes.py          # Rotas gerais
│   ├── 📁 auth/                  # Sistema de autenticação
│   │   ├── 📄 __init__.py
│   │   ├── 📄 routes.py          # Login, logout, controle de acesso
│   │   └── 📄 forms.py           # Formulários de autenticação
│   ├── 📁 tnc/                   # Gestão de TNCs
│   │   ├── 📄 __init__.py
│   │   ├── 📄 routes.py          # CRUD de TNCs
│   │   └── 📄 forms.py           # Formulários de TNC
│   ├── 📁 dashboard/             # Dashboard analítico
│   │   ├── 📄 __init__.py
│   │   └── 📄 routes.py          # Gráficos e estatísticas
│   ├── 📁 reports/               # Sistema de relatórios
│   │   ├── 📄 __init__.py
│   │   └── 📄 routes.py          # Geração de PDFs e exportações
│   ├── 📁 admin/                 # Administração do sistema
│   │   ├── 📄 __init__.py
│   │   └── 📄 routes.py          # Gestão de empresas, projetos, usuários
│   ├── 📁 models/                # Modelos de dados
│   │   ├── 📄 __init__.py
│   │   ├── 📄 user.py            # Modelo de usuário
│   │   ├── 📄 empresa.py         # Modelo de empresa
│   │   ├── 📄 projeto.py         # Modelo de projeto
│   │   ├── 📄 disciplina.py      # Modelo de disciplina
│   │   └── 📄 tnc.py             # Modelo principal TNC
│   ├── 📁 services/              # Serviços da aplicação
│   │   ├── 📄 __init__.py
│   │   ├── 📄 pdf_service.py     # Geração de relatórios PDF
│   │   ├── 📄 excel_service.py   # Importação/Exportação Excel
│   │   └── 📄 notification_service.py  # Sistema de notificações
│   └── 📁 utils/                 # Utilitários
│       ├── 📄 __init__.py
│       ├── 📄 validators.py      # Validadores customizados
│       └── 📄 helpers.py         # Funções auxiliares
├── 📁 templates/                 # Templates HTML (Jinja2)
│   ├── 📄 base.html              # Template base
│   ├── 📁 auth/                  # Templates de autenticação
│   │   ├── 📄 login.html
│   │   └── 📄 profile.html
│   ├── 📁 main/                  # Templates principais
│   │   ├── 📄 index.html
│   │   └── 📄 about.html
│   ├── 📁 dashboard/             # Templates do dashboard
│   │   └── 📄 index.html
│   ├── 📁 tnc/                   # Templates de TNC
│   │   ├── 📄 index.html         # Lista de TNCs
│   │   ├── 📄 create.html        # Criar TNC
│   │   ├── 📄 edit.html          # Editar TNC
│   │   └── 📄 view.html          # Visualizar TNC
│   ├── 📁 reports/               # Templates de relatórios
│   │   └── 📄 index.html
│   └── 📁 admin/                 # Templates de administração
│       └── 📄 index.html
├── 📁 static/                    # Arquivos estáticos
│   ├── 📁 css/                   # Estilos CSS
│   │   └── 📄 main.css           # Estilos principais
│   ├── 📁 js/                    # JavaScript
│   │   └── 📄 main.js            # Scripts principais
│   ├── 📁 images/                # Imagens
│   │   └── 📄 logo.png
│   ├── 📁 uploads/               # Arquivos enviados
│   └── 📁 reports/               # Relatórios gerados
├── 📁 config/                    # Configurações
│   ├── 📄 __init__.py
│   └── 📄 config.py              # Classes de configuração
├── 📁 data/                      # Dados da aplicação
│   ├── 📄 tnc_gestao.db          # Banco de dados SQLite
│   ├── 📁 exports/               # Exportações
│   │   ├── 📁 pdf/
│   │   ├── 📁 excel/
│   │   └── 📁 csv/
│   ├── 📁 backups/               # Backups
│   └── 📁 uploads/               # Uploads de arquivos
├── 📁 tests/                     # Testes da aplicação
│   ├── 📄 __init__.py
│   ├── 📄 test_models.py         # Testes dos modelos
│   ├── 📄 test_routes.py         # Testes das rotas
│   └── 📄 test_services.py       # Testes dos serviços
└── 📁 migrations/                # Migrações do banco (Flask-Migrate)
    └── 📁 versions/
```

## ⚙ **Funcionalidades Principais**

### ✅ **Cadastro e Gerenciamento de TNCs**
- Inserção manual e via importação Excel (.xlsx)
- Campos: Nº de sequência, Dados de emissão, Projeto, Documento, Empresa, Gravidade, Valor, Responsáveis, Dados de reinspeção, Status, Disciplina, Observações
- Sistema de workflow com controle de status

### ✅ **Dashboard Analítico**
- Gráficos dinâmicos e filtros com visualização interativa:
  - TNCs por Projeto
  - TNCs por Gravidade (Grave, Média, Leve)
  - TNCs por Disciplina Técnica
  - Status das TNCs (Aberta, Em Reinspeção, Concluída)
  - Evolução temporal das TNCs
  - Custo acumulado por Projeto/Empresa

### ✅ **Controle de Acesso**
- Perfis de usuários (Admin, Inspetor, Visualizador)
- Login com autenticação segura Flask-Login
- Controle de permissões por funcionalidade

### ✅ **Notificações e Alertas**
- Alertas de TNCs com reinspeção pendente
- Sistema de notificação em tempo real
- Opção de envio de e-mail automático (configurável)

### ✅ **Histórico e Comentários**
- Registro de alterações em cada TNC
- Comentários com dados, usuário e tipo de ação
- Auditoria completa de mudanças

### ✅ **Exportação e Relatórios**
- Exportar dados filtrados em PDF, Excel ou CSV
- Relatórios gerenciais com gráficos embutidos
- Templates profissionais para impressão

## 🧱 **Tecnologias Utilizadas**

### **Back-end**
- **Flask 3.0.0** - Framework web Python
- **Flask-SQLAlchemy** - ORM para banco de dados
- **Flask-Login** - Sistema de autenticação
- **Flask-Migrate** - Migrações de banco
- **SQLite** - Banco de dados embarcado

### **Front-end**
- **HTML5 + Bootstrap 5** - Interface responsiva
- **JavaScript + jQuery** - Interatividade
- **Chart.js** - Gráficos interativos
- **Jinja2** - Template engine

### **Relatórios e Dados**
- **ReportLab** - Geração de PDFs
- **Pandas** - Manipulação de dados
- **Openpyxl** - Excel import/export

### **Segurança**
- **Werkzeug** - Hashing de senhas
- **Flask-WTF** - Proteção CSRF
- **Validadores customizados**

## 🚀 **Como Executar**

### **1. Instalação**
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/TNC_GESTAO.git
cd TNC_GESTAO

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente (opcional)
cp .env.example .env
# Edite o arquivo .env conforme necessário
```

### **2. Execução**
```bash
# Método 1: Usando o run.py
python run.py

# Método 2: Usando Flask CLI
flask run

# Método 3: Usando o main.py (compatibilidade)
python main.py
```

### **3. Acesso**
- **URL**: http://localhost:5000
- **Login Admin**: admin / admin123
- **Login Inspetor**: inspetor / inspetor123

## 📊 **Dashboard em Funcionamento**

O sistema possui um dashboard analítico completo com:

- **KPIs em tempo real**: Total de TNCs, abertas, concluídas, valores
- **Gráficos interativos**: Pizza, barras e linha
- **Filtros dinâmicos**: Por status, gravidade, empresa, projeto
- **Exportação**: PDF executivo com todos os gráficos

## 🔐 **Pontos de Destaque do Projeto**

- ✅ **Redução de retrabalho** e padronização de dados
- ✅ **Visualização rápida** de gargalos técnicos
- ✅ **Facilidade na prestação de contas** e gestão de riscos
- ✅ **Suporte à análise financeira** de não conformidades
- ✅ **Flexível** para novos projetos, plantas ou unidades
- ✅ **Interface responsiva** - funciona em desktop, tablet e mobile
- ✅ **Sistema de backup** automático
- ✅ **API REST** para integrações futuras

## 🤝 **Contribuição**

1. Fork o projeto
2. Crie sua feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 **Licença**

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

**TNC Gestão v2.0** - Sistema Web Profissional para Gestão de Não Conformidades | Desenvolvido em 2025