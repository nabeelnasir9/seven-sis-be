import pandas as pd
from app.utils.qr_generator import generate_qr
from app.core.config import settings
from app.core.database import product_collection

def process_excel():
    df = pd.read_excel(settings.EXCEL_FILE_PATH)

    for _, row in df.iterrows():
        equipment_id = str(row["Equipment"]).strip()

        if product_collection.find_one({"equipment_id": equipment_id}):
            continue

        qr_data = f"{settings.BASE_URL}/{equipment_id}"
        qr_path = generate_qr(qr_data, equipment_id, settings.QR_CODE_PATH)

        data_dict = row.fillna("").astype(str).to_dict()

        product = {
            "equipment_id": equipment_id,
            "data": data_dict,
            "qr_code_url": qr_path,
        }

        product_collection.insert_one(product)
