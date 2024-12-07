import re
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json

# Load model TensorFlow
model = tf.keras.models.load_model("model/text_model.h5")

# Load tokenizer
with open("services/tokenizer.json", "r") as f:
    tokenizer_data = f.read()
tokenizer = tokenizer_from_json(tokenizer_data)

# Konfigurasi model
max_length = 250  # Sesuaikan dengan panjang maksimal yang kamu gunakan saat melatih model

def preprocess_text(text):
    """
    Preprocessing teks sebelum prediksi.
    """
    text = re.sub(r'\([^)]*\)', '', text)  # Hapus teks dalam tanda kurung
    text = re.sub(r'[^A-Za-z0-9]+', ' ', text)  # Hapus karakter spesial
    text = re.sub(r'\s+', ' ', text).strip()  # Hapus spasi berlebih
    text = text.lower()  # Ubah ke huruf kecil
    return text

def get_fillers_count(transcribed_text):
    """
    Hitung jumlah filler words
    """
    # Preprocess teks
    clean_text = preprocess_text(transcribed_text)

    # Daftar filler words
    fillers = ['um', 'uh', 'ah', 'like', 'you know', 'okay']

    # Hitung filler words
    count = sum([clean_text.count(filler) for filler in fillers])

    return count

def predict_confidence(transcribed_text, duration):
    """
    Prediksi confidence dari teks hasil transkripsi.
    """
    # Preprocess teks
    clean_text = preprocess_text(transcribed_text)
    fillers_count = get_fillers_count(clean_text)

    # word count
    word_count = len(clean_text.split())

    # WPM (Words Per Minute)
    wpm = word_count / (duration / 60)

    if wpm < 120:
        pace = "slow"
    elif wpm < 150:
        pace = "good"
    else:
        pace = "fast"

    # Konversi teks ke sequence
    sequence = tokenizer.texts_to_sequences([clean_text])
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding='post', truncating='post')

    # Prediksi menggunakan model TensorFlow
    confidence = model.predict(padded_sequence)[0][0]
    confidence_label = int(confidence > 0.5)

    return {
        "fillers_count": fillers_count,
        "word_count": word_count,
        "wpm": wpm,
        "pace": pace,
        "confidence": float(confidence),
        "confidence_label": confidence_label
    }
