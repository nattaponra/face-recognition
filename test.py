import face_recognition
import pickle
import numpy as np
import glob,sys
import FaceRecognition


if len(sys.argv) == 1 :
    print("Please enter activity_id argument")
    exit()


dataSetPath = 'datasets/dataset_'+sys.argv[1]+'.dat'
# Load face encodings
with open(dataSetPath, 'rb') as f:
	all_face_encodings = pickle.load(f)
 

face_names     = list(all_face_encodings.keys())
face_encodings = np.array(list(all_face_encodings.values()))
 

testPictures = glob.glob("test_picture/*.png")
matchPhotoIds = []

for path in testPictures:
    pictureEncode     = FaceRecognition.getEncodePicture(path)
    result            = face_recognition.compare_faces(face_encodings, pictureEncode)
    namesWithResults  = list(zip(face_names, result))
    for trainingFile in namesWithResults:
        if trainingFile[1]:
            matchPhotoIds.append(trainingFile[0])
            print(trainingFile[0])





