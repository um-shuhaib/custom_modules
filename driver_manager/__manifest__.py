# -*- coding: utf-8 -*-
{
    "name": "Driver Management System",
    "author": "tecfuge",
    "license": "LGPL-3",
    "version": "19.0.1.0.0",
    "summary": "All in one Driver Management System",
    "category": "Transportation",
    "website": "https://www.driverManage.com",
    "depends": [
        "sale_management","mail"
        ],
    "data": [
        "security/ir.model.access.csv",
        "views/customfields.xml",
        "views/test_kanban_view.xml",
        "views/driver_view.xml",
        # "views/wizard_view.xml",
        "views/menu.xml",
       
    ],
    # "installable": True,
    # "application": True,
}