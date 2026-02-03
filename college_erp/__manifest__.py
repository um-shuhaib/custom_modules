# -*- coding: utf-8 -*-
{
    "name": "Academy (Odoo 19 Demo)",
    "summary": "Starter custom module for Odoo 19 — simple Academy app",
    "version": "19.0.1.0.0",
    "category": "Education",
    "author": "tecfuge",
    "website": "https://www.tecfuge.com",
    "license": "LGPL-3",
    "depends": ["base","mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/student_details_view.xml",
        "views/student_pivot_view.xml",
        "views/course_views.xml",
        "views/academy_menu.xml",
       
    ],
    "installable": True,
    "application": True,
}