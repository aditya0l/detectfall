# Fall Detection System

## 📌 Overview
The **Fall Detection System** is a real-time AI-based solution that detects falls using a webcam, alerts users through an on-screen warning, and sends an email notification with a screenshot when a fall is detected. It utilizes **Mediapipe Pose Estimation, OpenCV, and Tkinter** for GUI-based control.

---

## 🛠️ Technologies Used
- **Python** (Primary Programming Language)
- **OpenCV** (Real-time video processing)
- **Mediapipe** (Pose estimation for human detection)
- **Tkinter** (Graphical User Interface for Start/Stop buttons)
- **smtplib & Email Modules** (Automated email alerts with fall images)
- **NumPy** (Numerical computations for landmark processing)

---

## ⚙️ Features
✅ **Real-time Fall Detection** using a webcam
✅ **Multiple human tracking** using Mediapipe Pose Estimation
✅ **On-screen alert** when a fall is detected
✅ **Automated email notification** with a screenshot of the detected fall
✅ **Graphical User Interface (GUI)** with Start/Stop buttons
✅ **Secure Email Integration** using Gmail SMTP with App Passwords

---

## 📥 Installation & Setup

### 1️⃣ Install Dependencies
Ensure Python is installed, then run:
```sh
pip install opencv-python mediapipe numpy
```

### 2️⃣ Configure Email Alerts
- Go to **[Google App Passwords](https://myaccount.google.com/apppasswords)**.
- Enable **2-Step Verification** (if not enabled).
- Generate a **16-character App Password**.
- Update the script with:
  ```python
  sender_email = "your_email@gmail.com"
  receiver_email = "receiver_email@gmail.com"
  app_password = "your_generated_app_password"
  ```

### 3️⃣ Run the Script
```sh
python fall_detection.py
```

---

## 🖥️ How It Works
1️⃣ **Start the application** using the Start Detection button.
2️⃣ The webcam will track **multiple people** using **Mediapipe Pose Estimation**.
3️⃣ If a fall is detected (**nose below both hips & knees**):
   - **An alert appears on the screen**.
   - **A screenshot is captured**.
   - **An email is sent** with the fall detection image.
4️⃣ Stop detection using the **Stop button or 'q' key**.

---

## 📝 Future Enhancements
🔹 Improve fall detection accuracy using deep learning models
🔹 Cloud storage for fall alerts and logs
🔹 SMS notification support for emergencies
🔹 Mobile app integration for remote monitoring

---

## 🤝 Contributing
Feel free to contribute by improving accuracy, UI, or integrating advanced detection models. Fork the repository, make changes, and submit a pull request!

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 📩 Contact
For any queries or collaboration, reach out to:
📧 Email: **adityajaif2004@gmail.com**

