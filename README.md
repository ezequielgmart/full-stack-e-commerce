# Full Stack E-Commerce Platform [In progress]
Full stack E-Commerce platform for a tech shop. Powered by React, Python. 

## Product Management
Product Catalog: The store needs a system to create, edit, and delete products. Each product should have attributes such as name, description, images, price, category, and status (e.g., available, out of stock).

Inventory: The system must track the quantity of each product available. When a customer buys a product, the inventory is automatically updated. If the inventory reaches zero, the product is marked as "out of stock" and cannot be sold.

## Shopping Cart
Add/Remove Products: Customers can add, modify, or remove products from their shopping cart before completing the order.

Cost Calculation: The cart should calculate the subtotal, taxes, shipping costs, and the final total. It must also apply any discounts or promotional codes.

## Checkout Process
Customer Information: Customer data, such as name, shipping and billing address, and email, is collected.

Payment Methods: The system must integrate various payment gateways (credit card, PayPal, etc.) to securely process transactions.

Final Verification: Product availability is checked one last time before payment is processed to prevent selling items that are no longer in stock.

## Order Management
Creation and Statuses: Every successful purchase creates an order with a unique ID. The order progresses through different statuses: "Pending Payment," "Processing," "Shipped," "Delivered," and "Canceled."

No Customer Edits: Customers cannot edit, add, or delete products after the order is placed.

Processing: Once a purchase is confirmed, a unique tracking number must be assigned to the order. This is how the customer will be able to track their shipment.

Notifications: Customers are sent email notifications about the status of their order.

## Shipping and Logistics
Rate Calculation: The system calculates shipping costs based on the customer's address, including city, state, and ZIP code, as well as the weight and size of the products.

Label Generation: Shipping labels containing the customer's information are generated and provided to the courier company.

Tracking: The customer receives a tracking number to follow their shipment's progress.

## Customer Service
Returns and Refunds: The system must include a process for handling product return requests, verifying conditions, and processing refunds.

Order History: Customers can view their order history and the current status of their purchases.

## Access and Permissions
Admin and Store Views: The platform must have two distinct views. Your access level determines what you can do and see. For example, the admin view can only be accessed by users with an admin profile, while the store view is for customers.

# // start the development server

```bash
uvicorn main:app --reload
```

```bash
py \backend\server.py
```


## Migrations
In order to import and create the GEM models for the repository, you need to go to the root (where your main file is located) and run 

```bash
py migrate.py
```

## API 

### profiles

* **Post**
`[Expected json body]`

```javascript

{
  "first_name":"Jon",
  "last_name":"Doe",  
  "gender":"Male"
  }

```


### Shipping addresses

* **Post**
`[Expected json body]`

```javascript

{
    "recipient_name":"jon doe",
    "street_address":"Central Street 1556",
    "city":"New York",
    "state_province":"New York",
    "country":"USA",
    "postal_code":"11111",
    "phone_number":"555-111-9999",
    "is_default":true
}

```

### Register new user
```javascript
{
  "username":"Jon",
  "email":"Doe",  
  "password":"Male"
  }
```