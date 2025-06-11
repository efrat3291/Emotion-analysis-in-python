
import cv2
from deepface import DeepFace

image_path = "img1.png"
img = cv2.imread(image_path)
result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
emotion = result[0]['dominant_emotion']

print("the dominant emotion is:", emotion)
