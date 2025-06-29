# 🤖 AI Hand Gesture Interface for Video Applications

Control any media player with your hands using this real-time AI-powered gesture recognition system.  
Leverages **MediaPipe**, **OpenCV**, and **PyAutoGUI** to simulate keyboard shortcuts through hand tracking — no touch required!

---

## 🎥 Demo Video

> 📌 **Embed your YouTube video or demo link here**

> 📂 [Click here to download or view the demo video](./assest/Screen%20Recording%202025-06-29%20030734.mp4)




---

## ✨ Features

- 🔴 Real-time webcam-based gesture detection
- 🖐️ Detects all 5 fingers using MediaPipe landmarks
- 🎮 Maps finger counts to media player controls
- 💻 Works across YouTube, VLC, and any software using standard keyboard shortcuts

---

## 🕹️ Gesture Mappings

| Finger Count | Key Simulated | Action              |
|--------------|----------------|---------------------|
| 5            | `Space`        | Play / Pause        |
| 2            | `Right Arrow`  | Seek Forward        |
| 3            | `Left Arrow`   | Seek Backward       |
| 1            | `Up Arrow`     | Volume Up           |
| 4            | `Down Arrow`   | Volume Down         |
| 0 (Fist)     | `M`            | Mute / Unmute       |

---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Create and activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install opencv-python mediapipe pyautogui
