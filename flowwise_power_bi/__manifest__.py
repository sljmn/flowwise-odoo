{
    "name": "Power BI Connector",
    "summary": "Read-only access for Power BI reports on Odoo sales orders, invoices, products and customers, through Flowwise's OData feed. Needs a Flowwise subscription.",
    "version": "19.0.1.0.1",
    "category": "Productivity",
    "author": "NewCraft",
    "website": "https://flowwise.dev/koppelingen/odoo/power-bi/",
    "support": "flowwise@newcraft.dev",
    "license": "LGPL-3",
    "depends": ["sale_stock", "account"],
    "data": [
        "security/power_bi_security.xml",
        "security/ir.model.access.csv",
        "views/flowwise_menu.xml",
    ],
    "images": ["static/description/banner.png"],
    "application": True,
    "installable": True,
}
