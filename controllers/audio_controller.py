from flask import Blueprint, request, jsonify
from services.gcs_service import upload_audio_file
from services.whisper_service import process_audio_with_whisper
from services.firestore_service import save_recording_to_firestore
from services.ml_service import predict_confidence
from config import Config
from utils.audio_extract import get_audio_duration
import time

audio_bp = Blueprint('audio', __name__)

@audio_bp.route('/process-audio', methods=['POST'])
def process_audio():
    # Ambil userId dan audioFile dari request
    user_id = request.form.get('userId')
    recordingTitle = request.form.get('recordingTitle')

    if not user_id or not isinstance(user_id, str):
        return jsonify({'message': 'Invalid or missing userId'}), 400
    
    if 'audioFile' not in request.files:
        return jsonify({'message': 'No audio file part'}), 400
    file = request.files['audioFile']
    if file.filename == '':
        return jsonify({'message': 'No selected audio file'}), 400

    file_extension = file.filename.split('.')[-1].lower()
    if file_extension not in Config.ALLOWED_EXTENSIONS:
        return jsonify({'message': f'Invalid file type. Only {", ".join(Config.ALLOWED_EXTENSIONS)} are allowed.'}), 400

    # Generate nama file unik
    filename = f'audio/{user_id}-{int(time.time())}.{file_extension}'

    # get audio duration from audioFile file

    try:
        # Upload file ke GCS
        audio_url = upload_audio_file(file, filename) #return: audio_url

        # Proses file menggunakan Whisper
        transcribe = process_audio_with_whisper(audio_url) #return: transcribe, duration

        # Prediksi confidence menggunakan TensorFlow
        prediction_result = predict_confidence(transcribe[0], transcribe[1]) #return: prediction_result

        # Simpan hasil ke Firestore: userId, audioUrl, transcribe, fillers_count, duration, word_count, wpm, confidence, confident
        firestore_response = save_recording_to_firestore(
            user_id, recordingTitle, audio_url, transcribe[0], prediction_result['fillers_count'], transcribe[1], prediction_result['word_count'], prediction_result['wpm'], prediction_result['pace'],prediction_result['confidence'], prediction_result['confidence_label']
        )
        print(recordingTitle)

        return jsonify({
            'message': 'Audio file processed and saved successfully',
            'firestoreResponse': firestore_response
        })
    except Exception as e:
        return jsonify({'message': str(e)}), 500
