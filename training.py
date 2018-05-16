import face_recognition
import json
import pickle
import FaceRecognition
import glob
 
#Input
# inputPictures = ["unknow_image/12828502_1005842369534847_7136850454606854375_o.jpg",
#                  "unknow_image/25438871_1565928383526240_8675585191151944587_o.jpg",
#                  "unknow_image/10981161_695207507265003_5104416470050938630_n.jpg",
#                  "unknow_image/25358342_1566786296773782_5191830380202574644_o.jpg"]a

#Get from training_picture dir
inputPictures = glob.glob("training_picture/*.jpg")
 
encodeReresult = {}
photoId = 0    
for path in inputPictures:
    encodeReresult[path] = FaceRecognition.getEncodePicture(path)
with open('dataset_faces.dat', 'wb') as f:
    pickle.dump(encodeReresult, f)

exit()


 
 
#textFile = open("Existing.txt","w")
#textFile.write(inputPictureEncoding) 
#textFile.close() 
#Existing Picture
