# Sign Language Recognition using YOLO

## 📌 Project Overview

This project recognizes hand gestures (sign language) using a YOLO-based object detection model.

Instead of traditional classification, the system detects and classifies hand gestures directly from images by predicting bounding boxes with corresponding gesture labels.

---

## 🎯 Objective

* Detect and classify hand gestures in images
* Build a scalable sign language recognition system
* Enable real-time gesture detection (extendable)

---

## 🚀 Key Features

* YOLO-based gesture detection
* Simultaneous localization and classification
* Works on custom labeled dataset
* Fast and efficient inference

---

## 🧠 Model & Approach

* Model: YOLO (Ultralytics)
* Framework: PyTorch
* Task: Object Detection (gesture detection + classification)
* Labels: Each gesture is treated as a class

---

## ⚙️ Workflow / Pipeline

1. Input image is captured or loaded
2. Image is passed to trained YOLO model
3. Model detects hand gesture(s)
4. Bounding boxes and class labels are predicted
5. Output image with labels is saved in `outputs/`

---

## 🛠️ Tech Stack

* Python
* OpenCV
* Ultralytics YOLO
* PyTorch
* NumPy

---

## 📂 Project Structure

```id="signstruct2"
sign-language-recognition/
│
├── sample_data/
├── outputs/
├── models/
│
├── train.py
├── predict.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash id="signrun3"
pip install -r requirements.txt
```

### 2. Run prediction

```bash id="signrun4"
python predict.py
```

---

## 📊 Results

* Detects and classifies hand gestures in images
* Outputs images with bounding boxes and labels
* Results available in `outputs/` folder

---

## ⚠️ Limitations

* Accuracy depends on dataset quality and diversity
* Complex backgrounds may affect detection
* Limited gesture classes

---

## 🔮 Future Improvements

* Real-time webcam-based recognition
* Expand gesture vocabulary
* Convert gestures to text/audio output
* Deploy as mobile/web application

---

## 📌 Note

Dataset is not included in this repository due to size constraints.
Sample inputs are provided for demonstration.

---

## 👨‍💻 Author

Raviteja
