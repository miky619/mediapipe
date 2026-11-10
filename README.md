[README-2.md](https://github.com/user-attachments/files/34649535/README-2.md)
# MediaPipe Hand Tracking & Gesture Control

A collection of Python computer-vision experiments that use **MediaPipe Hands** and **OpenCV** to detect hand landmarks, count raised fingers, recognize a small set of gestures, and control Windows system volume with hand gestures.

The repository contains four standalone scripts. Each script demonstrates a different step in building webcam-based hand interaction.

## Features

- Real-time webcam input through OpenCV.
- Hand landmark detection with MediaPipe.
- Finger counting using hand landmark positions.
- On-screen display of the detected finger count or gesture label.
- A basic victory-gesture snapshot experiment.
- Windows speaker volume and mute control through `pycaw` (in `app4.py`).

## Project Files

| File | Description |
| --- | --- |
| `app.py` | Detects a hand and displays an estimated raised-finger count. |
| `app2.py` | Maps the detected count to text labels (`mosht`, `one`, `two`, `three`, `four`, `baz`) and attempts to print a numeric result when the program exits. |
| `app3.py` | Adds a basic victory-gesture condition and saves the current frame as `victory.jpg` when that condition is met. |
| `app4.py` | Uses one detected hand to control Windows speaker mute and volume levels. |
| `requirements.txt` | Dependency list. It is currently empty. |

## How It Works

1. Open the default webcam with `cv2.VideoCapture(0)`.
2. Read a frame and convert it from BGR to RGB.
3. Pass the RGB frame to MediaPipe Hands.
4. Read the detected hand landmarks.
5. Estimate which fingers are raised by comparing the vertical positions of fingertip and lower-joint landmarks.
6. Display the result in the webcam window, or use the count to trigger an action.

The scripts use the standard MediaPipe hand landmark indices. The four non-thumb fingers are checked using landmarks `8`, `12`, `16`, and `20`; the thumb is handled separately.

## Requirements

- Python
- A working webcam
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)
- For `app4.py` on Windows: `pycaw` and its Windows audio dependencies

> `requirements.txt` is empty in the current repository. The packages above are identified from the imports in the source files; no pinned package versions are specified.

## Installation

It is recommended to create and activate a virtual environment.

```bash
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

Install the packages used by the scripts:

```bash
pip install opencv-python mediapipe
```

For the Windows volume-control script (`app4.py`), also install:

```bash
pip install pycaw comtypes
```

## Run

Run one script at a time from the repository directory:

```bash
python app.py
```

Or choose another experiment:

```bash
python app2.py
python app3.py
python app4.py
```

A webcam window should open. Press **Q** to close it.

### Script notes

- **`app.py`** — Displays the estimated number of raised fingers.
- **`app2.py`** — Displays a text label for the detected count. Its final numeric output is experimental and may not represent the intended count correctly.
- **`app3.py`** — Saves a frame as `victory.jpg` when its victory condition is detected. The saved image is written to the current working directory.
- **`app4.py`** — Maps zero raised fingers to mute, and one through five fingers to volume levels from 20% to 100%. This script is intended for Windows because it uses `pycaw`.

## Known Limitations

This repository is an experimental project rather than a production-ready hand-tracking application.

- Finger counting is based on simple landmark-coordinate comparisons and may be less reliable for rotated hands, unusual camera angles, or partially hidden fingers.
- The scripts process webcam frames continuously and require a working camera.
- The gesture rules are basic and may need calibration for different hands and camera orientations.
- `app2.py` duplicates the numeric label string before converting it to an integer, so its printed result can be incorrect.
- `app4.py` currently contains a misspelled method name in the 80% volume branch (`SetMasterVoluضmeLevelScalar`). As written, that branch will raise an error instead of setting the volume to 80%. Replace it with `SetMasterVolumeLevelScalar` to correct the typo.
- The current `requirements.txt` does not declare any dependencies.

## Possible Improvements

- Add a complete and tested `requirements.txt`.
- Draw hand landmarks and connections on the webcam frame.
- Improve finger-state detection for both hands and different orientations.
- Refactor the repeated tracking code into reusable functions.
- Add robust camera-read and hand-detection error handling.
- Correct the issues noted above and add clear on-screen feedback.

## Technologies

- **Python** — Application logic
- **MediaPipe Hands** — Hand landmark detection
- **OpenCV** — Webcam capture, image processing, and display
- **pycaw** — Windows audio endpoint and volume control (`app4.py`)

## Author

**Miky**  
GitHub: [@miky619](https://github.com/miky619)

## Repository

[github.com/miky619/mediapipe](https://github.com/miky619/mediapipe)
