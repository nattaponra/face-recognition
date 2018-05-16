import face_recognition
import json
import pickle
import FaceRecognition
#Input
inputPictures = ["unknow_image/12828502_1005842369534847_7136850454606854375_o.jpg",
                 "unknow_image/25438871_1565928383526240_8675585191151944587_o.jpg",
                 "unknow_image/10981161_695207507265003_5104416470050938630_n.jpg",
                 "unknow_image/25358342_1566786296773782_5191830380202574644_o.jpg"]
def getEncodePicture(path):
    pictureInput         = face_recognition.load_image_file(path)
    inputPictureEncoding = face_recognition.face_encodings(pictureInput)[0]
    return inputPictureEncoding 

encodeReresult = {}
photoId = 0    
for i in inputPictures:
    encodeReresult[photoId] = getEncodePicture(i)
    photoId=photoId+1
with open('dataset_faces.dat', 'wb') as f:
    pickle.dump(encodeReresult, f)

exit()


 
 
#textFile = open("Existing.txt","w")
#textFile.write(inputPictureEncoding) 
#textFile.close() 
#Existing Picture
