import os
import uuid
import requests
from openai import OpenAI
from utils.audio_extract import get_audio_duration

# Inisialisasi OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TEMP_AUDIO_FOLDER = "temp-audio"

def process_audio_with_whisper(public_url):
    """
    Menggunakan Whisper API untuk memproses file audio dari URL publik GCS.
    """
    os.makedirs(TEMP_AUDIO_FOLDER, exist_ok=True)
    unique_filename = f"{uuid.uuid4()}.mp3"
    temp_audio_file = os.path.join(TEMP_AUDIO_FOLDER, unique_filename)

    try:
        # Unduh file audio dari URL publik
        audio_data = requests.get(public_url)
        audio_data.raise_for_status()  # Pastikan file berhasil diunduh
        
        # Simpan file audio ke sistem lokal
        with open(temp_audio_file, "wb") as f:
            f.write(audio_data.content)

        # Kirim file ke OpenAI Whisper API
        with open(temp_audio_file, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                prompt=(
                    "Transcribe the audio verbatim and include filler words like "
                    "'um', 'uh', and 'like'. If there is a pause in the audio, add [pause]."
                ),
            )

        # panggil get_audio_duration
        duration = get_audio_duration(temp_audio_file)
        
        # Kembalikan hasil transkripsi dan durasi audio
        return transcription.text, duration
    except Exception as e:
        raise Exception(f"Failed to process audio with Whisper: {str(e)}")
    finally:
        # Hapus file audio sementara
        if os.path.exists(temp_audio_file):
            os.remove(temp_audio_file)
