{
    "name": "Bol.com Connector",
    "summary": "Bol.com orders as sales orders in Odoo, tracking back to bol.com, and stock, price and delivery time per product from Odoo. Runs with a Flowwise subscription.",
    "version": "18.0.1.1.0",
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
