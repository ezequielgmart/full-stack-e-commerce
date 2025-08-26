
from pydantic import BaseModel

class Pagination(BaseModel):

    total_items:int
    total_pages:int
    per_page:int
