import cv2

# Open the webcam (0 for default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# Capture a frame
ret, frame = cap.read()

# If the frame was captured successfully, save it
if ret:
    cv2.imwrite("captured_image.jpg", frame)
    print("Image saved as 'captured_image.jpg'")
else:
    print("Error: Could not capture image")

# Release the camera
cap.release()
cv2.destroyAllWindows()

    
    