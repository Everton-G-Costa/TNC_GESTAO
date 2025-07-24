# 🚀 TNC Gestão

Sistema Desktop para Gestão de Tratativas de Não Conformidades

## ✨ Funcionalidades

- 📊 **Dashboard Analítico**: Visualização em tempo real das estatísticas
- 📋 **Gestão de TNCs**: CRUD completo com filtros avançados
- 📄 **Relatórios PDF**: Geração automática de relatórios detalhados
- 🏢 **Multi-empresa**: Gestão de múltiplas empresas e projetos
- 💾 **Banco Local**: SQLite para armazenamento local seguro
- 🎨 **Interface Moderna**: PyQt6 com design profissional

## 🔧 Instalação

### 1. Pré-requisitos
- Python 3.8 ou superior
- Windows (testado no Windows 10/11)

### 2. Instalação Automática
```bash
# Execute o script de instalação
install_dependencies.bat
```

### 3. Instalação Manual
```bash
# Instalar dependências principais
pip install PyQt6 reportlab pandas matplotlib pillow

# Dependências opcionais
pip install openpyxl xlsxwriter
```

## 🚀 Como Usar

### Modo Gráfico (Recomendado)
```bash
python main.py
```

### Modo Console (Teste)
```bash
python test_basic.py
```

### Demo Completa
```bash
python demo_console.py
```

## 📁 Estrutura do Projeto

```
tnc-gestao/
├── 📂 src/                    # Código fonte
│   ├── 📂 database/           # Conexão e modelos de dados
│   ├── 📂 gui/                # Interface gráfica
│   ├── 📂 models/             # Modelos de dados
│   ├── 📂 services/           # Serviços (PDF, etc.)
│   └── 📂 controllers/        # Controladores
├── 📂 data/                   # Dados da aplicação
│   ├── 📂 exports/            # Relatórios exportados
│   ├── 📂 backups/            # Backups automáticos
│   └── 📂 database/           # Banco SQLite
├── 📂 resources/              # Recursos (ícones, templates)
├── 📄 main.py                 # Aplicação principal
├── 📄 demo_console.py         # Demo em console
└── 📄 test_basic.py           # Teste básico
```

## 💻 Funcionalidades Principais

### 1. Dashboard
- Estatísticas em tempo real
- Gráficos de status e gravidade
- Valores financeiros
- Indicadores de performance

### 2. Gestão de TNCs
- Criar, editar e excluir TNCs
- Filtros por status, gravidade, data
- Busca avançada
- Histórico de alterações

### 3. Relatórios PDF
- Relatórios executivos
- Gráficos e análises
- Detalhamento completo
- Exportação automática

### 4. Administração
- Gestão de projetos
- Cadastro de empresas
- Configuração de disciplinas
- Backup automático

## 🗃️ Banco de Dados

O sistema utiliza SQLite com as seguintes tabelas:

- **tncs**: Dados principais das TNCs
- **projetos**: Projetos cadastrados
- **empresas**: Empresas participantes
- **disciplinas**: Disciplinas técnicas
- **tnc_historico**: Histórico de alterações
- **tnc_comentarios**: Comentários e observações
- **tnc_anexos**: Anexos e documentos

## 🎯 Status do Desenvolvimento

### ✅ Concluído
- [x] Banco de dados SQLite
- [x] Modelos de dados completos
- [x] Interface gráfica base
- [x] Geração de relatórios PDF
- [x] Dashboard estatístico
- [x] Sistema de filtros
- [x] Gestão de projetos/empresas

### 🔄 Em Desenvolvimento
- [ ] Formulários de cadastro
- [ ] Sistema de anexos
- [ ] Backup/restore avançado
- [ ] Integração com Excel
- [ ] Notificações

### 🚀 Futuras Versões
- [ ] Relatórios Excel/CSV
- [ ] API REST
- [ ] Versão web
- [ ] Mobile app
- [ ] Integração ERP

## 🛠️ Solução de Problemas

### PyQt6 não encontrado
```bash
pip install PyQt6
```

### Erro de importação matplotlib
```bash
pip install matplotlib
```

### Banco não inicializa
1. Verifique permissões na pasta `data/`
2. Execute: `python test_basic.py`
3. Reinicie a aplicação

### Relatório PDF não gera
1. Verifique se a pasta `data/exports/pdf/` existe
2. Instale: `pip install reportlab`
3. Execute o teste: `python demo_console.py`

## 📞 Suporte

Para suporte técnico:
1. Execute `python test_basic.py` para verificar funcionamento
2. Verifique os logs em `data/logs/`
3. Consulte a documentação técnica

## 🔄 Versionamento

### v1.0.0 (Atual)
- Sistema base funcional
- Interface gráfica completa
- Relatórios PDF
- Banco SQLite

### Roadmap v1.1.0
- Formulários avançados
- Sistema de anexos
- Exportação Excel

## 📄 Licença

Este projeto é proprietário. Todos os direitos reservados.

---

**TNC Gestão v1.0** - Sistema Profissional para Gestão de Não Conformidades
