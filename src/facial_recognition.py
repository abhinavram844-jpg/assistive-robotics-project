import face_recognition
import cv2
import numpy as np
from picamera2 import Picamera2
import pickle

print("Loading encodings...")
with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)
    
known_face_encodings = data["encodings"]
known_face_names = data["names"]

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

print("Face recognition running. Press Q to quit")

while True:
    frame = picam2.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    #detecting faces
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    
    for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        #compare faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            
        #Draw the box and name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        
        if name == "ABHINAV":
            print("Abhinav Detected! Wohooo")
        
    cv2.imshow("PROMPTOPAL", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
picam2.stop()
    
