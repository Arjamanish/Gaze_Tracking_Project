# Real-time Eye Tracking Application

This project implements real-time eye tracking using Python and OpenCV. It can detect faces and eyes in real-time using your webcam.

## Features

- Real-time webcam feed with eye tracking overlay
- Face detection with blue rectangle highlighting
- Eye detection with green rectangle highlighting
- FPS counter
- User-friendly interface

## Requirements

- Python 3.7 or higher
- Webcam
- Required Python packages:
  - opencv-python
  - numpy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/eye-tracking.git
   cd eye-tracking
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python gaze_tracker.py
   ```

2. Position yourself in front of your webcam
3. The application will show:
   - Your webcam feed with face and eye detection overlay
   - FPS counter in the top-left corner
4. Press 'q' to quit the application

## Tips for Best Results

- Ensure good lighting conditions
- Position yourself directly in front of the webcam
- Keep your face clearly visible
- Adjust the window size as needed

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenCV for computer vision capabilities
- Haarcascade classifiers for face and eye detection 
