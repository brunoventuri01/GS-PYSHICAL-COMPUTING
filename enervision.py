
import cv2
import mediapipe as mp
import time
from PIL import ImageFont, ImageDraw, Image
import numpy as np

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

status = False
ultimo_toggle = time.time()
fonte = ImageFont.truetype("Montserrat-Bold.ttf", 48)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    frame = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        landmarks = results.pose_landmarks.landmark
        mao_direita = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
        mao_esquerda = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]

        distancia_x = abs(mao_direita.x - mao_esquerda.x)
        distancia_y = abs(mao_direita.y - mao_esquerda.y)
        tempo_atual = time.time()

        if distancia_x < 0.1 and distancia_y < 0.1 and (tempo_atual - ultimo_toggle) > 2:
            status = not status
            ultimo_toggle = tempo_atual

    texto_status = "LIGADA" if status else "DESLIGADA"
    cor_status = (0, 255, 0) if status else (255, 0, 0)

    frame_pil = Image.fromarray(frame)
    draw = ImageDraw.Draw(frame_pil)

    texto_base = "LUZ DE EMERGÊNCIA: "
    texto_completo = texto_base + texto_status

    draw.text((30, 30), texto_completo, font=fonte, fill=(255, 255, 255))

    bbox = draw.textbbox((0, 0), texto_base, font=fonte)
    largura_base = bbox[2] - bbox[0]
    draw.text((30 + largura_base, 30), texto_status, font=fonte, fill=cor_status)

    frame = np.array(frame_pil)
    cv2.imshow('EnerVision - Texto Corrigido', frame)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
