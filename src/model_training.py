import face_recognition
import pickle
import os
import cv2

print("Training Model....")

dataset_path = "/home/aram/dataset"
known_encodings = []
known_names = []

for person_name in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person_name)
    
    if not os.path.isdir(person_path):
        continue
    
    print(f"Processing: {person_name}")
    
    for image_file in os.listdir(person_path):
        if not image_file.endswith(('.jpg', '.png', '.jpeg')):
            continue
        
        image_path = os.path.join(person_path, image_file)
        image = cv2.imread(image_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        boxes = face_recognition.face_locations(rgb, model='hog')
        encodings = face_recognition.face_encodings(rgb, boxes)
        
        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(person_name)
            
data = {"encodings": known_encodings, "names": known_names}
with open("encodings.pickle", "wb") as f:
    pickle.dump(data, f)
    
print(f"Done! Processed {len(known_names)} faces")
    
