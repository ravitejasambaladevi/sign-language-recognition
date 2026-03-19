from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train/weights/best.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    results = model(frame)

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            label = model.names[cls_id]

            print(f"{label} ({conf:.2f})")

    annotated = results[0].plot()
    cv2.imshow("Detection", annotated)

    if cv2.waitKey(1) == 27:
        break