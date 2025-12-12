# Hand Gesture Mouse Pointer

A Python application that allows you to control your mouse pointer using hand gestures captured through your webcam. This project uses MediaPipe for hand tracking and PyAutoGUI for mouse control.

## Features

- Control mouse cursor movement with your index finger
- Click functionality using pinch gesture
- Smooth cursor movement
- Real-time hand tracking
- Visual feedback with hand landmarks

## Requirements

- Python 3.7 or higher
- Webcam
- The following Python packages:
  - OpenCV (opencv-python)
  - MediaPipe
  - PyAutoGUI

## Installation

1. Clone this repository:
```bash
git clone https://github.com/PasinduGunathilake/a-Hand_Gesture_Mouse_pointer_r-.git
cd a-Hand_Gesture_Mouse_pointer_r-
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script:
```bash
python hand_gesture_mouse.py
```

- Hold your hand in front of the webcam
- Move your index finger to control the cursor
- Pinch your thumb and index finger together to click
- Press 'q' to quit the application

## How it Works

The application uses MediaPipe's hand tracking solution to detect hand landmarks in real-time. It then maps the position of your index finger to screen coordinates and uses PyAutoGUI to control the mouse cursor.

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome!

## Author

PasinduGunathilake
