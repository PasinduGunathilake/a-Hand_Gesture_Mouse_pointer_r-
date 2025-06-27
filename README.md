# Hand Gesture Mouse Pointer

This project allows you to control your mouse pointer using hand gestures, utilizing your computer's webcam. It is implemented in Python with the help of OpenCV, MediaPipe, and PyAutoGUI.

## Features

- **Hand Detection:** Uses MediaPipe to detect hand landmarks in real-time.
- **Mouse Control:** Move your mouse pointer by showing your hand to the webcam.
- **Gesture Actions:**
  - Move the index fingertip to move the mouse pointer.
  - Use different hand labels (right/left) to trigger mouse actions (move/click).

## Requirements

- Python 3.x
- [OpenCV](https://pypi.org/project/opencv-python/)
- [MediaPipe](https://pypi.org/project/mediapipe/)
- [PyAutoGUI](https://pypi.org/project/pyautogui/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/PasinduGunathilake/a-Hand_Gesture_Mouse_pointer_r-.git
   cd a-Hand_Gesture_Mouse_pointer_r-
   ```

2. **Install Python dependencies:**

   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

## Usage

1. **Run the script:**

   ```bash
   python hgp.py
   ```

2. **Control the Mouse:**
   - Show your hand to the webcam.
   - Moving your index finger (tip) will move the mouse pointer.
   - If your right hand is detected, the pointer will move.
   - If your left hand is detected, a mouse click will be triggered.

3. **Exit:**
   - Press `x` on your keyboard to exit the application.

## Notes

- Make sure your webcam is connected and accessible.
- For best results, use the application in a well-lit environment.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [MediaPipe by Google](https://mediapipe.dev/)
- [OpenCV](https://opencv.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
