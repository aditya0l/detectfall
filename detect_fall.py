import cv2
import mediapipe as mp
import numpy as np
import smtplib
import tkinter as tk
from tkinter import Button
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Initialize Mediapipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Initialize Tkinter UI
root = tk.Tk()
root.title("Fall Detection System")
root.geometry("200x100")

# Start/Stop Button Variables
running = False
cap = None

def send_email(image_path):
    """Send an email with a fall detection alert and attached image."""
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    app_password = "your_app_password"
    
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Fall Detected Alert"
        
        with open(image_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={image_path}")
            msg.attach(part)
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def detect_fall(landmarks):
    """Detect fall based on multiple human poses."""
    for landmark in landmarks:
        nose = landmark[mp_pose.PoseLandmark.NOSE.value].y
        left_hip = landmark[mp_pose.PoseLandmark.LEFT_HIP.value].y
        right_hip = landmark[mp_pose.PoseLandmark.RIGHT_HIP.value].y
        left_knee = landmark[mp_pose.PoseLandmark.LEFT_KNEE.value].y
        right_knee = landmark[mp_pose.PoseLandmark.RIGHT_KNEE.value].y
        
        avg_hip_y = (left_hip + right_hip) / 2
        avg_knee_y = (left_knee + right_knee) / 2
        
        if nose > avg_hip_y and nose > avg_knee_y:
            return True
    return False

def start_detection():
    global running, cap
    if not running:
        running = True
        cap = cv2.VideoCapture(0)
        process_frame()

def stop_detection():
    global running, cap
    running = False
    if cap:
        cap.release()
        cap = None
    cv2.destroyAllWindows()

def process_frame():
    global cap
    if running and cap and cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            return
        
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)
        
        fall_detected = False
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, 
                                      mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2))
            
            if detect_fall([results.pose_landmarks.landmark]):
                fall_detected = True
                cv2.putText(frame, "FALL DETECTED!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                print("FALL DETECTED!")
                image_path = "fall_detected.jpg"
                cv2.imwrite(image_path, frame)
                send_email(image_path)
        
        cv2.imshow("Fall Detection", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_detection()
            return
        
        if running:
            root.after(10, process_frame)

# UI Buttons
start_btn = Button(root, text="Start Detection", command=start_detection)
start_btn.pack()
stop_btn = Button(root, text="Stop Detection", command=stop_detection)
stop_btn.pack()

root.mainloop()
