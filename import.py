from app.services.excel_qr_service import process_excel

if __name__ == "__main__":
    process_excel()
    print("Excel processing complete and data stored to MongoDB Atlas.")
