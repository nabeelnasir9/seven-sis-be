from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class Product(BaseModel):
    equipment_id: str
    data: Dict[str, str]
    qr_code_url: str
    created_at: datetime = datetime.now()
