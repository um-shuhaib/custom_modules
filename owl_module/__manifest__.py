# -*- coding: utf-8 -*-
{
    "name": "Owl Counter Module",
    "author": "tecfuge",
    "license": "LGPL-3",
    "version": "19.0.1.0.0",
    "summary": "Custome module for learning the owl framework",
    "category": "Education",
    "website": "https://www.tecfuge.com",
    "assets":{
        'web.assets_backend':[
            'owl_module/static/src/js/components/counter.js',
            'owl_module/static/src/js/components/counter.xml',
            
        ]
    },
    "depends": ['base','stock'],
    "data": [
        "security/ir.model.access.csv",
        "views/owl_view.xml",
        "views/menus.xml",
        
        
       
    ],
    # "installable": True,
    # "application": True,
}