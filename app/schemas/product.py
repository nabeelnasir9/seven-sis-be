from pydantic import BaseModel
from typing import Dict

class ProductResponse(BaseModel):
    equipment_id: str
    data: Dict[str, str]
    qr_code_url: str
