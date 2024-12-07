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
    app.run(debug=True)
