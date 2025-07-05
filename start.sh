#!/bin/bash
clear
echo "🎬 Viva Media - Odoo 18 Starting..."
echo "======================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+"
    exit 1
fi

echo "📦 Installing requirements..."
python3 -m pip install --user -r requirements.txt

echo ""
echo "🚀 Starting Odoo 18 with Viva Media..."
echo "======================================"
echo "📧 Login Email: admin@vivamedia.com"
echo "🔑 Password: admin123"
echo "🌐 Open: http://localhost:8069"
echo "======================================"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start Odoo
python3 odoo-bin --config=odoo.conf --addons-path=addons --dev=all

echo ""
echo "✅ Viva Media stopped. Thank you!"
