from pydub import AudioSegment

def get_audio_duration(audio_file):
    """
    Mengembalikan durasi audio dalam detik.
    """
    try:
        # Baca file audio dari file-like object
        audio = AudioSegment.from_file(audio_file)
        duration = len(audio) / 1000.0  # Durasi dalam detik
        return duration
    except Exception as e:
        raise Exception(f"Failed to get audio duration: {str(e)}")
