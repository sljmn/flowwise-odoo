# Bol.com Connector by Flowwise

Odoo module for [Flowwise](https://flowwise.dev/koppelingen/bol-com/odoo/). It adds a Bol.com tab to products (a bol.com price and delivery time that Flowwise sends to the offer) and a Flowwise menu item. Flowwise itself connects through Odoo's external API: bol.com orders become sales orders in Odoo, tracking goes back to bol.com, and stock, price and delivery time go from Odoo to bol.com.

The module holds data only (two product fields, a form view, a menu item and a URL action), so Odoo Online can install it. Flowwise needs Odoo Online on the Custom plan, Odoo.sh or a self-hosted Odoo, because Odoo Online Standard and One App Free have no external API access.

One branch per Odoo version: `18.0`, `19.0`.

License: LGPL-3. Support: flowwise@newcraft.dev
