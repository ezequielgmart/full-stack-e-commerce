from pydantic import BaseModel
import uuid

class ShippingAddress(BaseModel):
    address_id: uuid.UUID
    user_id: uuid.UUID
    recipient_name: str
    street_address: str
    city: str
    state_province: str
    # Orden corregido para coincidir con el gem
    postal_code: str
    country: str
    phone_number: str
    # --
    is_default: bool


class ShippingAddressRegister(BaseModel):
    recipient_name: str
    street_address: str
    city: str
    state_province: str
    # Orden corregido para coincidir con el gem
    postal_code: str
    country: str
    phone_number: str
    # --
    is_default: bool