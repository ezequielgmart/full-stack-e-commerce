# from features.shipping_addresses.repository import ShippingAddressesRepository
# from entities.migrations import _shipping_addresses_gem

# from entities.shipping_addresses import ShippingAddress

# from pygem.main import SingleQueries

# import uuid


# def test_insert():

#     USER_ID = "b370a256-4b9e-4b2a-a9e9-d757d54402b1"
            
#     data_for_service = {
        
#         "address_id":uuid.uuid4(),
#         "user_id": USER_ID,
#         "recipient_name":"jon doe",
#         "street_address":"Central Street 1556",
#         "city":"New York",
#         "state_province":"New York",
#         "country":"USA",
#         "postal_code":"11111",
#         "phone_number":"555-111-9999",
#         "is_default":True

#     }

#     # repo = ShippingAddressesRepository(create_db_pool(DB_CONFIG))
    
#     new_data = _shipping_addresses_gem.queries.insert_query()

#     assert new_data == "INSERT"



