@echo off
title Viva Media - Odoo 18
cls
echo 🎬 Viva Media - Odoo 18 Starting...
echo ======================================
echo.

echo 📦 Installing requirements...
python -m pip install --user -r requirements.txt

echo.
echo 🚀 Starting Odoo 18 with Viva Media...
echo ======================================
echo 📧 Login Email: admin@vivamedia.com
echo 🔑 Password: admin123
echo 🌐 Open: http://localhost:8069
echo ======================================
echo.
echo Press Ctrl+C to stop the server
echo.

python odoo-bin --config=odoo.conf --addons-path=addons --dev=all

echo.
echo ✅ Viva Media stopped. Thank you!
pause
