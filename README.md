# Flowwise modules for Odoo

## Bol.com Connector

Odoo module for [Flowwise](https://flowwise.dev/koppelingen/bol-com/odoo/). It adds a Bol.com tab to products (a bol.com price and delivery time that Flowwise sends to the offer) and a Flowwise menu item. Flowwise itself connects through Odoo's external API: bol.com orders become sales orders in Odoo, tracking goes back to bol.com, and stock, price and delivery time go from Odoo to bol.com.

The module holds data only (two product fields, a form view, a menu item and a URL action), so Odoo Online can install it. Flowwise needs Odoo Online on the Custom plan, Odoo.sh or a self-hosted Odoo, because Odoo Online Standard and One App Free have no external API access.

## Power BI Connector (`flowwise_power_bi`)

Odoo module for [Flowwise's Odoo Power BI connector](https://flowwise.dev/koppelingen/odoo/power-bi/). Flowwise reads sales orders, invoices, products and customers through Odoo's API and serves them to Power BI as an OData feed. The module adds a Power BI access right with one level, Read only, for the Odoo user whose API key Flowwise uses: read access to those records and the stock they need, and nothing else. It also adds a Power BI menu item for administrators. Data only, so Odoo Online can install it. Depends on Sales (`sale_stock`) and Invoicing.

The access right differs per series: Odoo 19 groups hang on a `res.groups.privilege`, Odoo 18 groups on an `ir.module.category`.

One branch per Odoo version: `18.0`, `19.0`.

License: LGPL-3. Support: flowwise@newcraft.dev
