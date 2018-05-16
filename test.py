import face_recognition
import pickle
import numpy as np
import glob
import FaceRecognition



# Load face encodings
with open('dataset_faces.dat', 'rb') as f:
	all_face_encodings = pickle.load(f)

face_names     = list(all_face_encodings.keys())
face_encodings = np.array(list(all_face_encodings.values()))
 

testPictures = glob.glob("test_picture/*.jpg")
matchPhotoIds = []
for path in testPictures:
    pictureEncode     = FaceRecognition.getEncodePicture(path)
    result            = face_recognition.compare_faces(face_encodings, pictureEncode)
    namesWithResults  = list(zip(face_names, result))
    for trainingFile in namesWithResults:
        if trainingFile[1]:
            matchPhotoIds.append(trainingFile[0])

 
print(matchPhotoIds)





