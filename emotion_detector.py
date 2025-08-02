
import cv2
from fer import FER
from pyAudioAnalysis import audioSegmentation as aS
import tempfile

def detect_emotion_from_face():
    detector = FER(mtcnn=True)
    cap = cv2.VideoCapture(0)
    result_emotion = None
    for _ in range(20):
        ret, frame = cap.read()
        if not ret:
            break
        result = detector.detect_emotions(frame)
        if result:
            result_emotion, score = detector.top_emotion(frame)
            break
    cap.release()
    return result_emotion

def detect_emotion_from_voice(audio_file):
    # Save uploaded audio to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name
    # Fake classifier logic for now (demo purposes)
    return "Stressed"
