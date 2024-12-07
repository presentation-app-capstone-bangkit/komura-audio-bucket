# from pydub import AudioSegment

# def get_audio_duration(audio_file):
#     """
#     Mengembalikan durasi audio dalam detik.
#     """
#     try:
#         # Baca file audio dari file-like object
#         audio = AudioSegment.from_file(audio_file)
#         duration = len(audio) / 1000.0  # Durasi dalam detik
#         return duration
#     except Exception as e:
#         raise Exception(f"Failed to get audio duration: {str(e)}")

from mutagen.mp3 import MP3
from mutagen.wave import WAVE

def get_audio_duration(file_path):
    try:
        if file_path.endswith(".mp3"):
            audio = MP3(file_path)
        elif file_path.endswith(".wav"):
            audio = WAVE(file_path)
        else:
            raise Exception("Unsupported file format")
        
        return audio.info.length  # Durasi dalam detik
    except Exception as e:
        raise Exception(f"Failed to get audio duration: {str(e)}")