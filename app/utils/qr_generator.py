import qrcode, os

def generate_qr(data: str, equipment_id: str, save_path: str):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    qr_img = qrcode.make(data)
    qr_file_path = os.path.join(save_path, f"{equipment_id}.png")
    qr_img.save(qr_file_path)
    return qr_file_path
