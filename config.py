import os
from dotenv import load_dotenv

# Memuat variabel-variabel dari file .env
load_dotenv()

class Config:
    """Mengatur konfigurasi untuk aplikasi Flask."""
    
    # Mengambil nilai variabel-variabel dari .env
    GOOGLE_PROJECT_ID = os.getenv("GOOGLE_PROJECT_ID")
    GOOGLE_PRIVATE_KEY_ID = os.getenv("GOOGLE_PRIVATE_KEY_ID")
    GOOGLE_PRIVATE_KEY = os.getenv("GOOGLE_PRIVATE_KEY")
    GOOGLE_CLIENT_EMAIL = os.getenv("GOOGLE_CLIENT_EMAIL")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_AUTH_URI = os.getenv("GOOGLE_AUTH_URI")
    GOOGLE_TOKEN_URI = os.getenv("GOOGLE_TOKEN_URI")
    GOOGLE_AUTH_PROVIDER_X509_CERT_URL = os.getenv("GOOGLE_AUTH_PROVIDER_X509_CERT_URL")
    GOOGLE_CLIENT_X509_CERT_URL = os.getenv("GOOGLE_CLIENT_X509_CERT_URL")
    
    # Nama bucket GCS
    GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME", "komura-audio-bucket") 

    # Kunci API OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Ekstensi file yang diperbolehkan
    ALLOWED_EXTENSIONS = set(os.getenv("ALLOWED_EXTENSIONS", "mp3,wav").split(','))

    # API URL
    API_URL = os.getenv("API_URL", "http://localhost:8080")
    
    @classmethod
    def get_google_credentials(cls):
        """Mengembalikan kredensial dalam bentuk dictionary untuk digunakan oleh Google Cloud."""
        return {
            "type": "service_account",
            "project_id": os.getenv("GOOGLE_PROJECT_ID"),
            "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
            "private_key": os.getenv("GOOGLE_PRIVATE_KEY"),
            "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
            "client_id": os.getenv("GOOGLE_CLIENT_ID"),
            "auth_uri": os.getenv("GOOGLE_AUTH_URI"),
            "token_uri": os.getenv("GOOGLE_TOKEN_URI"),
            "auth_provider_x509_cert_url": os.getenv("GOOGLE_AUTH_PROVIDER_X509_CERT_URL"),
            "client_x509_cert_url": os.getenv("GOOGLE_CLIENT_X509_CERT_URL")
        }
