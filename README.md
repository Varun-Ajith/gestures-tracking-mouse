# Hand Tracking Mouse

This Python script utilizes computer vision techniques and the MediaPipe library to create a virtual mouse control system using hand gestures captured through a webcam.

## Overview

This script allows you to control your computer's mouse cursor using hand gestures captured from the webcam. By tracking the position of your thumb and index finger, it enables actions like clicking, moving the cursor, and dragging objects on the screen.

## Dependencies

- OpenCV (cv2)
- MediaPipe
- PyAutoGUI

## Installation

1. Make sure you have Python installed on your system.
2. Install the required dependencies using pip: `pip install opencv-python mediapipe pyautogui`
   
## Usage

1. Clone this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using Python: `python Hand-tracking-mouse.py`
5. 5. Adjust your hand in front of the webcam to control the mouse cursor.
6. Use the following keyboard commands while the script is running:
- Press 'q' to quit the application.
- Press 'd' to toggle dragging mode.
- Press 'r' to toggle releasing of dragging mode.

## Customization

You can modify the script to suit your preferences or add additional functionality as needed. Some possible enhancements include:
- Adding more hand gestures for different actions.
- Fine-tuning the thresholds for click and move actions.
- Implementing additional keyboard shortcuts for specific tasks.

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


