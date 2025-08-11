from pygem.main import SingleGenericSchema
from pygem.pydantic_models import Field


_users_gem = SingleGenericSchema(
    table='users',
    primary_key='user_id',
    fields=[
        Field(is_primary_key=True, name='user_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='username', type='varchar', is_null=False),
        Field(is_primary_key=False, name='email', type='varchar', is_null=False),
        Field(is_primary_key=False, name='password', type='varchar', is_null=False),
        Field(is_primary_key=False, name='is_admin', type='boolean', is_null=False)
    ]
)


_profiles_gem = SingleGenericSchema(
    table='profiles',
    primary_key='user_id',
    fields=[
        Field(is_primary_key=True, name='user_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='first_name', type='varchar', is_null=False),
        Field(is_primary_key=False, name='last_name', type='varchar', is_null=False),
        Field(is_primary_key=False, name='city', type='varchar', is_null=False),
        Field(is_primary_key=False, name='state', type='varchar', is_null=False),
        Field(is_primary_key=False, name='country', type='varchar', is_null=False),
        Field(is_primary_key=False, name='zip_code', type='varchar', is_null=False),
        Field(is_primary_key=False, name='gender', type='varchar', is_null=True),
        Field(is_primary_key=False, name='phone_number', type='varchar', is_null=True),
        Field(is_primary_key=False, name='created_at', type='timestamp with time zone', is_null=True),
        Field(is_primary_key=False, name='updated_at', type='timestamp with time zone', is_null=True)
    ]
)


_orders_gem = SingleGenericSchema(
    table='orders',
    primary_key='status_id',
    fields=[
        Field(is_primary_key=True, name='order_id', type='uuid', is_null=False),
        Field(is_primary_key=True, name='user_id', type='uuid', is_null=False),
        Field(is_primary_key=True, name='status_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='total_cost', type='numeric', is_null=False),
        Field(is_primary_key=False, name='created_at', type='timestamp with time zone', is_null=True)
    ]
)


_order_statuses_gem = SingleGenericSchema(
    table='order_statuses',
    primary_key='status_id',
    fields=[
        Field(is_primary_key=True, name='status_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='status_name', type='varchar', is_null=False)
    ]
)


_products_gem = SingleGenericSchema(
    table='products',
    primary_key='product_id',
    fields=[
        Field(is_primary_key=True, name='product_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='name', type='varchar', is_null=False),
        Field(is_primary_key=False, name='description', type='text', is_null=False),
        Field(is_primary_key=False, name='unit_price', type='numeric', is_null=False)
    ]
)


_products_inventory_gem = SingleGenericSchema(
    table='products_inventory',
    primary_key='product_id',
    fields=[
        Field(is_primary_key=True, name='product_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='stock', type='integer', is_null=False)
    ]
)


_order_items_gem = SingleGenericSchema(
    table='order_items',
    primary_key='product_id',
    fields=[
        Field(is_primary_key=True, name='order_id', type='uuid', is_null=False),
        Field(is_primary_key=True, name='product_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='quantity', type='integer', is_null=False),
        Field(is_primary_key=False, name='price_at_purchase', type='numeric', is_null=False)
    ]
)


_payments_gem = SingleGenericSchema(
    table='payments',
    primary_key='status_id',
    fields=[
        Field(is_primary_key=True, name='payment_id', type='uuid', is_null=False),
        Field(is_primary_key=True, name='order_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='amount', type='numeric', is_null=False),
        Field(is_primary_key=False, name='payment_method_id', type='uuid', is_null=False),
        Field(is_primary_key=True, name='status_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='created_at', type='timestamp with time zone', is_null=True)
    ]
)


_payment_methods_gem = SingleGenericSchema(
    table='payment_methods',
    primary_key='method_id',
    fields=[
        Field(is_primary_key=True, name='method_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='method_name', type='varchar', is_null=False)
    ]
)


_payment_statuses_gem = SingleGenericSchema(
    table='payment_statuses',
    primary_key='status_id',
    fields=[
        Field(is_primary_key=True, name='status_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='status_name', type='varchar', is_null=False)
    ]
)


_shopping_carts_gem = SingleGenericSchema(
    table='shopping_carts',
    primary_key='user_id',
    fields=[
        Field(is_primary_key=True, name='cart_id', type='uuid', is_null=False),
        Field(is_primary_key=True, name='user_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='created_at', type='timestamp with time zone', is_null=True)
    ]
)


_categories_gem = SingleGenericSchema(
    table='categories',
    primary_key='category_id',
    fields=[
        Field(is_primary_key=True, name='category_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='name', type='varchar', is_null=False)
    ]
)


_inventory_movement_types_gem = SingleGenericSchema(
    table='inventory_movement_types',
    primary_key='type_id',
    fields=[
        Field(is_primary_key=True, name='type_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='type_name', type='varchar', is_null=False)
    ]
)


_cart_items_gem = SingleGenericSchema(
    table='cart_items',
    primary_key='product_id',
    fields=[
        Field(is_primary_key=True, name='cart_id', type='uuid', is_null=False),
        Field(is_primary_key=True, name='product_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='quantity', type='integer', is_null=False)
    ]
)


_product_categories_gem = SingleGenericSchema(
    table='product_categories',
    primary_key='category_id',
    fields=[
        Field(is_primary_key=True, name='product_id', type='uuid', is_null=False),
        Field(is_primary_key=True, name='category_id', type='uuid', is_null=False)
    ]
)


_inventory_movements_gem = SingleGenericSchema(
    table='inventory_movements',
    primary_key='product_id',
    fields=[
        Field(is_primary_key=True, name='movement_id', type='uuid', is_null=False),
        Field(is_primary_key=True, name='product_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='movement_type_id', type='uuid', is_null=False),
        Field(is_primary_key=False, name='quantity_change', type='integer', is_null=False),
        Field(is_primary_key=False, name='reference_id', type='varchar', is_null=True),
        Field(is_primary_key=False, name='movement_date', type='timestamp with time zone', is_null=True)
    ]
)

