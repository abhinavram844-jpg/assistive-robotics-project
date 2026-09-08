import cv2
from picamera2 import Picamera2
import os

PERSON_NAME = "ABHINAV"

if not os.path.exists("dataset"):
    os.makedirs("dataset")

person_folder = os.path.join("dataset", PERSON_NAME)
if not os.path.exists(person_folder):
    os.makedirs(person_folder)

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

print(f"Taking photos for: {PERSON_NAME}")
print("Press SPACE to take photo, Q to quit")

photo_count = 0

while True:
    frame = picam2.capture_array()
    cv2.imshow("Press SPACE to take photo", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord(' '):
        photo_count += 1
        filename = os.path.join(person_folder, f"{PERSON_NAME}_{photo_count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
    elif key == ord('q'):                      
        break
    
cv2.destroyAllWindows()
picam2.stop()
print(f"Done! Saved {photo_count} photos")

