
import cv2
import time
from deepface import DeepFace

def detect_emotion():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    detected_emotion = None
    start_time = time.time()

    while True:
        # Check for timeout (60 seconds)
        if time.time() - start_time > 60:
            print("Timeout: No emotion detected within 60 seconds.")
            break

        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            face_roi = frame[y:y+h, x:x+w]
            try:
                obj = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
                detected_emotion = obj[0]['dominant_emotion']
                break
            except Exception as e:
                print(f"Error detecting emotion: {str(e)}")
                detected_emotion = None

    cap.release()
    cv2.destroyAllWindows()
    return detected_emotion



