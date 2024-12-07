import requests

def save_recording_to_firestore(user_id, recordingTitle, audio_url, transcribe, fillers_count, duration, word_count, wpm, pace, confidence, confidentLabel):
    """
    Mengirim data hasil transkripsi ke Firestore melalui API lokal.
    """
    api_url = "http://127.0.0.1:8080/save-recording"

    # Payload untuk dikirim ke Firestore
    payload = {
        "userId": user_id,
        "recordingTitle": recordingTitle,
        "audioUrl": audio_url,
        "transcribe": transcribe,
        "fillers_count": fillers_count,
        "duration": duration,
        "word_count": word_count,
        "wpm": wpm,
        "pace": pace,
        "confidence": confidence,
        "confidentLabel": confidentLabel
    }

    print(f"Sending data to Firestore: {payload}, {recordingTitle}")

    try:
        # Kirim data ke API lokal
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Pastikan tidak ada error dari server
        return response.json()  # Kembalikan hasil dari API Firestore
    except Exception as e:
        raise Exception(f"Failed to save recording to Firestore: {str(e)}")
