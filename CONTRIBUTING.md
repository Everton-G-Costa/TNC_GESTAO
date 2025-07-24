# 🤝 Guia de Contribuição - TNC GESTÃO

Obrigado por seu interesse em contribuir com o projeto TNC GESTÃO! 

## 📋 **Como Contribuir**

### 1. **Fork do Projeto**
```bash
# No GitHub, clique em "Fork"
# Clone seu fork
git clone https://github.com/SEU_USUARIO/tnc-gestao.git
cd tnc-gestao
```

### 2. **Configurar Ambiente**
```bash
# Criar ambiente virtual (recomendado)
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt
```

### 3. **Criar Branch**
```bash
# Criar branch para sua funcionalidade
git checkout -b feature/nova-funcionalidade
# ou
git checkout -b fix/correcao-bug
```

### 4. **Desenvolver**
- Escreva código limpo e documentado
- Siga as convenções do Python (PEP 8)
- Teste suas mudanças
- Adicione comentários quando necessário

### 5. **Commit**
```bash
# Adicionar arquivos
git add .

# Commit com mensagem descritiva
git commit -m "feat: adiciona nova funcionalidade X"
# ou
git commit -m "fix: corrige bug Y"
```

### 6. **Push e Pull Request**
```bash
# Enviar para seu fork
git push origin feature/nova-funcionalidade

# No GitHub, criar Pull Request
```

## 🔍 **Tipos de Contribuição**

### 🚀 **Novas Funcionalidades**
- Novos módulos para o sistema
- Melhorias na interface
- Novos tipos de relatórios
- Integrações com APIs externas

### 🐛 **Correção de Bugs**
- Correções de erros
- Melhorias de performance
- Correções de interface

### 📚 **Documentação**
- Melhorias no README
- Documentação de código
- Guias de uso
- Comentários em código

### 🎨 **Melhorias de UI/UX**
- Design da interface
- Usabilidade
- Acessibilidade
- Responsividade

## 📝 **Padrões de Código**

### **Python**
```python
# Use PEP 8
# Imports organizados
import os
import sys
from typing import List, Optional

from PyQt6.QtWidgets import QWidget
from src.models.base_model import BaseModel

# Classes com docstrings
class MinhaClasse:
    """Descrição da classe."""
    
    def meu_metodo(self, parametro: str) -> bool:
        """Descrição do método.
        
        Args:
            parametro: Descrição do parâmetro
            
        Returns:
            Descrição do retorno
        """
        return True
```

### **Commits**
```bash
# Formato: tipo: descrição
feat: adiciona funcionalidade X
fix: corrige bug Y
docs: atualiza documentação Z
style: melhora formatação
refactor: refatora código
test: adiciona testes
```

## 🧪 **Testes**

Antes de enviar seu Pull Request:

```bash
# Executar sistema
python main.py

# Testar funcionalidades afetadas
# Verificar se não quebrou nada existente
```

## 🔧 **Ambiente de Desenvolvimento**

### **Estrutura do Projeto**
```
src/
├── gui/           # Interface gráfica
├── models/        # Modelos de dados
├── database/      # Banco de dados
├── services/      # Serviços
└── utils/         # Utilitários
```

### **Dependências Principais**
- PyQt6: Interface gráfica
- SQLite3: Banco de dados
- Matplotlib: Gráficos
- ReportLab: PDFs

## 📋 **Checklist do Pull Request**

- [ ] Código testado e funcionando
- [ ] Segue padrões do projeto
- [ ] Documentação atualizada se necessário
- [ ] Commit com mensagem clara
- [ ] Sem arquivos desnecessários
- [ ] Compatível com versão atual

## 🎯 **Áreas que Precisam de Ajuda**

### **Alta Prioridade**
- Testes automatizados
- Melhorias de performance
- Documentação de APIs
- Validação de dados

### **Média Prioridade**
- Novos relatórios
- Melhorias de UI
- Tradução/i18n
- Configurações avançadas

### **Baixa Prioridade**
- Temas personalizados
- Plugins
- Integrações externas
- Mobile/Web

## 💬 **Comunicação**

- **Issues**: Para bugs e sugestões
- **Discussions**: Para dúvidas gerais
- **Pull Requests**: Para contribuições de código

## 🎉 **Reconhecimento**

Todos os contribuidores serão listados no README e releases do projeto.

---

**Obrigado por contribuir com o TNC GESTÃO!** 🙏
