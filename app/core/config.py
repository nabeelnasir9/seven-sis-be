class Settings:
    DATABASE_URL = "mongodb+srv://codseed2:Nabeelnasir123@sevenqr.s0z6j.mongodb.net/"
    DATABASE_NAME = "sevenqr"
    COLLECTION_NAME = "products"
    EXCEL_FILE_PATH = "data/Nabeel.xlsx"
    QR_CODE_PATH = "app/static/qrcodes"
    BASE_URL = "http://192.168.0.103:3000/product"
    tlsAllowInvalidCertificates=True

settings = Settings()


