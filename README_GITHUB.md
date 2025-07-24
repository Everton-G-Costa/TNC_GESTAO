# 🐍 TNC GESTÃO - Sistema de Gestão de TNCs

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-GUI-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-orange.svg)
![Status](https://img.shields.io/badge/Status-Funcionando-brightgreen.svg)

Sistema completo para gestão de **Terms de Não Conformidade (TNCs)** desenvolvido em Python com interface gráfica PyQt6.

## 🚀 **Execução Rápida**

```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/tnc-gestao.git
cd tnc-gestao

# Execute o sistema
python main.py
```

**OU use o script automático:**
```bash
.\executar_sistema.bat
```

## ✨ **Funcionalidades**

### 🏢 **Gestão de Empresas**
- ✅ Cadastro de empresas com CNPJ
- ✅ Status ativo/inativo
- ✅ Dados de contato completos
- ✅ 156+ empresas já cadastradas

### 📄 **Sistema TNC**
- ✅ Cadastro de Terms de Não Conformidade
- ✅ Gestão de projetos e disciplinas
- ✅ Controle de tratativas
- ✅ Workflow completo de aprovação

### 📊 **Relatórios e Dashboard**
- ✅ Dashboard interativo com gráficos
- ✅ Relatórios PDF personalizados
- ✅ Análise de distribuição por empresa
- ✅ Estatísticas detalhadas

### ⚙️ **Administração**
- ✅ Gestão de usuários
- ✅ Configurações do sistema
- ✅ Backup e restore
- ✅ Logs de auditoria

## 🛠️ **Tecnologias**

- **Frontend**: PyQt6 (Interface Gráfica)
- **Backend**: Python 3.8+
- **Database**: SQLite3
- **Relatórios**: ReportLab (PDF)
- **Gráficos**: Matplotlib
- **Arquitetura**: MVC (Model-View-Controller)

## 📋 **Requisitos**

### **Python 3.8 ou superior**
```bash
# Verificar versão
python --version
```

### **Dependências**
```bash
# Instalar dependências
pip install -r requirements.txt
```

**Principais dependências:**
- PyQt6
- SQLite3 (incluído no Python)
- Matplotlib
- ReportLab
- Pillow

## 🔧 **Instalação**

### **1. Clone o repositório**
```bash
git clone https://github.com/SEU_USUARIO/tnc-gestao.git
cd tnc-gestao
```

### **2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**OU use o script automático:**
```bash
.\install_dependencies.bat
```

### **3. Execute o sistema**
```bash
python main.py
```

## 📁 **Estrutura do Projeto**

```
tnc-gestao/
├── 📄 main.py                    # Arquivo principal
├── 🔧 executar_sistema.bat       # Script de execução
├── 📦 requirements.txt           # Dependências
├── 🖼️ logo_rnc.ico               # Ícone do sistema
├── 📚 README.md                  # Este arquivo
├── 📁 src/                       # Código fonte
│   ├── gui/                      # Interface gráfica
│   │   ├── dialogs/              # Diálogos
│   │   ├── widgets/              # Widgets customizados
│   │   └── windows/              # Janelas principais
│   ├── models/                   # Modelos de dados
│   │   ├── base_model.py         # Modelo base
│   │   ├── tnc_model.py          # Modelo TNC
│   │   └── support_models.py     # Modelos auxiliares
│   ├── database/                 # Conexão banco de dados
│   ├── services/                 # Serviços
│   │   ├── pdf_report_service.py # Relatórios PDF
│   │   └── chart_service.py      # Gráficos
│   └── utils/                    # Utilitários
└── 📁 data/                      # Dados
    ├── tnc_gestao.db             # Banco principal
    ├── backups/                  # Backups
    └── exports/                  # Exportações
```

## 🎯 **Uso**

### **Executar o Sistema**
```bash
# Método 1: Script recomendado
.\executar_sistema.bat

# Método 2: Python direto
python main.py

# Método 3: Setup completo
.\setup_completo.bat
```

### **Acessar Funcionalidades**
1. **Dashboard**: Visão geral do sistema
2. **TNCs**: Gestão de Terms de Não Conformidade
3. **Administração**: Configurações e gestão
4. **Relatórios**: Geração de PDFs e análises

## 📊 **Status do Projeto**

- ✅ **Sistema**: 100% funcional
- ✅ **Interface**: PyQt6 completa
- ✅ **Database**: SQLite com 156+ empresas
- ✅ **Relatórios**: PDF funcionando
- ✅ **Dashboard**: Gráficos interativos
- ✅ **Testes**: Backend validado

## 🎨 **Screenshots**

### Dashboard Principal
Interface moderna com gráficos interativos e estatísticas em tempo real.

### Gestão de Empresas
Sistema completo para cadastro e gestão de empresas com validação de CNPJ.

### Relatórios PDF
Geração automática de relatórios profissionais em PDF.

## 🚀 **Atalhos com Ícone Personalizado**

O projeto inclui atalhos com ícone personalizado:
- 🚀 **TNC Gestão.lnk** - Atalho principal
- 📄 **executar_sistema.bat** - Script direto

## 🤝 **Contribuição**

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 **Licença**

Este projeto está sob a licença MIT.

## 👨‍💻 **Desenvolvido com**

- ❤️ **Paixão** por desenvolvimento de software
- 🐍 **Python** para lógica robusta
- 🎨 **PyQt6** para interface moderna
- 💾 **SQLite** para persistência confiável

## 📞 **Suporte**

Para suporte ou dúvidas:
- Abra uma [Issue](https://github.com/SEU_USUARIO/tnc-gestao/issues)
- Consulte a documentação no projeto

---

⭐ **Se este projeto foi útil, deixe uma estrela no GitHub!** ⭐

**Sistema TNC GESTÃO - Transformando a gestão de não conformidades em Python** 🐍✨
