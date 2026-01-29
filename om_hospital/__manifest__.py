# -*- coding: utf-8 -*-
{
    "name": "Hospital Management System",
    "author": "tecfuge",
    "license": "LGPL-3",
    "version": "19.0.1.0.0",
    # "summary": "Starter custom module for Odoo 19 — simple Academy app",
    # "category": "Education",
    # "website": "https://www.tecfuge.com",
    "assets":{
        'web.assets_backend':[
            'om_hospital/static/src/js/components/new_text_field.js',
            'om_hospital/static/src/js/components/newText.xml',
        ]
    },
    "depends": [
        "mail","product","portal","sale_management"
        ],
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/appoinment_view.xml",
        "views/patient_readonly_view.xml",
        "views/patient_view.xml",
        "views/widget_temp.xml",
        "views/menu.xml",
        "views/portal_template.xml",
        "views/widget_temp.xml",
        "reports/report.xml",
        "reports/patient_report_template.xml",
        
        # "wizards/wizard_view.xml",
        
       
    ],
    # "installable": True,
    # "application": True,
}