import os
from flask import Flask
from controllers.audio_controller import audio_bp  # Import blueprint
from config import Config 

app = Flask(__name__)

# Mengatur konfigurasi Flask menggunakan class Config
app.config.from_object(Config)

@app.route('/')
def index():
    return "Welcome to the Komura Audio Processing API!"

# Register Blueprint untuk endpoint audio
app.register_blueprint(audio_bp, url_prefix='/audio')

if __name__ == '__main__':
    # Gunakan PORT dari environment variable atau default ke 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)  # Host harus 0.0.0.0 untuk Cloud Run
