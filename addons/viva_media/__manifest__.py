# -*- coding: utf-8 -*-
{
    'name': 'Viva Media Production Management',
    'version': '18.0.1.0.0',
    'category': 'Industries/Media & Entertainment',
    'summary': 'Complete Film & TV Production Management System',
    'description': '''
🎬 Viva Media Production Management
==================================

نظام شامل لإدارة إنتاج الأفلام والمسلسلات والإعلانات

الميزات الرئيسية:
• 📋 إدارة المشاريع - دورة حياة كاملة للمشاريع
• 👥 إدارة العملاء - نظام CRM للعملاء
• 💰 إدارة الميزانيات - تتبع مالي دقيق
• 🎯 إدارة المهام - تعاون الفريق
• 📊 التقارير والتحليلات - رؤى الأداء
• 🎨 إدارة الأصول - تنظيم المحتوى الرقمي
• ⏰ تتبع الوقت - إدارة الوقت والفواتير

مناسب لـ:
✓ شركات إنتاج الفيديو
✓ وكالات الإعلان
✓ الاستوديوهات الإبداعية
✓ دور الإعلام
✓ المنتجين المستقلين

يحول Odoo إلى مركز قوي لإدارة الإنتاج الإعلامي
    ''',
    'author': 'Viva Media Team',
    'website': 'https://github.com/ziyadtareq/viva-media-odoo18',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
        'mail',
        'contacts',
        'project',
        'hr',
        'account',
        'calendar'
    ],
    'data': [
        # Security
        'security/viva_media_security.xml',
        'security/ir.model.access.csv',
        
        # Data
        'data/project_stages.xml',
        'data/demo_data.xml',
        
        # Views
        'views/viva_menus.xml',
        'views/viva_project_views.xml',
        'views/viva_client_views.xml',
        'views/viva_budget_views.xml',
        'views/viva_team_views.xml',
    ],
    'demo': [
        'data/demo_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'viva_media/static/src/css/viva_media.css',
            'viva_media/static/src/js/viva_media.js',
        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': 10,
}
