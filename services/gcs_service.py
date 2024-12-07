from google.cloud import storage
from config import Config

def upload_audio_file(file, filename):
    try:
        # Inisialisasi client GCS dengan kredensial yang benar dari Config
        credentials = Config.get_google_credentials()  # Dapatkan kredensial dari Config
        client = storage.Client.from_service_account_info(credentials)  # Menggunakan kredensial
        
        # Dapatkan bucket dari config
        bucket = client.get_bucket(Config.GCS_BUCKET_NAME)

        # Buat blob dan upload file
        blob = bucket.blob(filename)
        blob.upload_from_file(file, content_type=file.content_type)

        # Kembalikan URL publik file
        return blob.public_url
    except Exception as e:
        raise Exception(f"Failed to upload file to GCS: {str(e)}")
