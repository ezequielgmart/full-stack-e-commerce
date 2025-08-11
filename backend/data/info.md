Aqui en esta carpeta de data se encuentran las configuraciones iniciales de la base de datos para la aplicacion en caso de que necesite crear otra base de datos y llenarla dei nformacion

Dominios: 

auth
* login
* logout
users (profiles)
* register
* fill out profile 
* get profile information
* update personal information (shipping address, etc)
* delete account
products
*** users is not required to be logged in to review the products
* get products and with filters (paginated) 
* get by categorie
* get by LIKE function
cart
**** user must log in before get shopping cart info / edit it etc
* insert product on the shopping cart
* remove products from the shopping cart
* get the shopping cart status and products
orders
**** user must log in and the stock for each product on the order must be more than 1
* make a new order from shopping cart
* buy now (make an order without inserting the item on the shoppign cart before)
* change the order status ('proccesing','on delivery','delivered')

admin
* manage products
