{
    "name": "Flowwise Bol.com Sync",
    "summary": "Flowwise connects bol.com to Odoo: orders as sales orders, tracking back to bol.com, and stock, prices and offers from Odoo. Needs a Flowwise subscription.",
    "version": "18.0.1.5.3",
    "category": "Sales/Sales",
    "author": "NewCraft",
    "website": "https://flowwise.dev/koppelingen/bol-com/odoo/",
    "support": "flowwise@newcraft.dev",
    "license": "LGPL-3",
    "depends": ["product"],
    "data": [
        "data/product_fields.xml",
        "views/product_views.xml",
        "views/flowwise_menu.xml",
    ],
    "images": ["static/description/banner.png"],
    "application": True,
    "installable": True,
}
