from ultralytics import YOLO
import cv2

# Load the YOLO model
model = YOLO('yolov8n')  # Use the appropriate model

def start_detection():
    """Start the object detection process using the webcam."""
    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)  # 0 is the default camera

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Run YOLO model on the frame
        results = model(frame)

        # Loop through the results and draw bounding boxes with labels
        for result in results[0].boxes:
            x1, y1, x2, y2 = map(int, result.xyxy[0])  # Bounding box (top-left and bottom-right coordinates)
            confidence = result.conf[0]
            label = result.cls[0]

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label_text = f"{model.names[int(label)]} {confidence:.2f}"
            cv2.putText(frame, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Show the frame with detections
        cv2.imshow("Object Detection", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
