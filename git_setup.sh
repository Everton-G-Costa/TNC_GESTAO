#!/bin/bash
echo "🚀 Enviando TNC Gestão para GitHub..."
echo

# Verificar se é um repositório Git
if [ ! -d ".git" ]; then
    echo "📦 Inicializando repositório Git..."
    git init
    echo
fi

# Configurar usuário Git se necessário
if [ -z "$(git config --global user.name)" ]; then
    read -p "📝 Digite seu nome para Git: " git_name
    git config --global user.name "$git_name"
fi

if [ -z "$(git config --global user.email)" ]; then
    read -p "📧 Digite seu email para Git: " git_email
    git config --global user.email "$git_email"
fi

echo "📦 Adicionando arquivos..."
git add .

echo "💾 Fazendo commit..."
git commit -m "Sistema TNC Gestão - Versão Python funcional completa

✨ Funcionalidades:
- Interface PyQt6 completa
- Gestão de empresas (156+ cadastradas)
- Sistema TNC com workflow completo
- Dashboard com gráficos interativos
- Relatórios PDF personalizados
- Administração completa

🛠️ Tecnologias:
- Python 3.8+
- PyQt6
- SQLite3
- Matplotlib
- ReportLab

📊 Status: 100% funcional e testado"

echo "🔧 Configurando branch principal..."
git branch -M main

echo "✅ Repositório Git configurado!"
echo
echo "🌐 Próximos passos:"
echo "1. Crie um repositório no GitHub chamado 'tnc-gestao'"
echo "2. Execute os comandos:"
echo "   git remote add origin https://github.com/SEU_USUARIO/tnc-gestao.git"
echo "   git push -u origin main"
echo
echo "💡 Substitua SEU_USUARIO pelo seu nome de usuário do GitHub"
echo
echo "🎉 Projeto pronto para GitHub!"
