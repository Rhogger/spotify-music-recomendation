#!/bin/bash

# Script para configurar filtros Git para notebooks Jupyter
# Este script configura o Git para limpar metadados dos notebooks durante diffs

echo "🔧 Configurando filtros Git para notebooks Jupyter..."

# Verifica se o nbstripout está instalado
if ! command -v nbstripout &> /dev/null; then
    echo "📦 Instalando nbstripout..."
    pip install nbstripout
fi

# Configura o filtro para notebooks
echo "⚙️  Configurando filtro jupyternotebook..."
git config filter.jupyternotebook.clean 'nbstripout --textconv'
git config filter.jupyternotebook.smudge cat
git config diff.jupyternotebook.textconv 'nbstripout --textconv'

# Aplica as configurações ao repositório atual
echo "✅ Aplicando configurações ao repositório..."
nbstripout --install --attributes .gitattributes

echo "🎉 Configuração concluída!"
echo ""
echo "ℹ️  O que foi configurado:"
echo "   - Metadados e outputs dos notebooks serão removidos dos diffs"
echo "   - Code reviews focarão apenas no código dos notebooks"
echo "   - Arquivos .ipynb continuarão funcionando normalmente no Jupyter"
echo ""
echo "💡 Para reverter: git config --unset filter.jupyternotebook.clean"