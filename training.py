import face_recognition
import json
import pickle
import FaceRecognition
import glob,sys
 
#Input
# inputPictures = ["unknow_image/12828502_1005842369534847_7136850454606854375_o.jpg",
#                  "unknow_image/25438871_1565928383526240_8675585191151944587_o.jpg",
#                  "unknow_image/10981161_695207507265003_5104416470050938630_n.jpg",
#                  "unknow_image/25358342_1566786296773782_5191830380202574644_o.jpg"]a

#Get from training_picture dir
 
 


if len(sys.argv) != 3 :
    print("Please enter activity_id argument")
 


arguments     = sys.argv
types         = ('*.jpg', '*.JPG') 
inputPictures = []

for files in types:
        inputPictures.extend(glob.glob(arguments[2]+'/'+files))


#inputPictures = glob.glob("training_picture/*.jpg")
 
encodeReresult = {}

for path in inputPictures:
    print("Start File:",path)
    bufferEncodeing = FaceRecognition.getEncodePicture(path)
    index = 0    
    for i in bufferEncodeing:
            encodeReresult[path+"_"+str(index)] = i
            index += 1
    countFace = len(bufferEncodeing)
    print("Finish:",path,countFace)
print("All Face:",len(encodeReresult))
with open('datasets/dataset_'+arguments[1]+'.dat', 'wb') as f:
    pickle.dump(encodeReresult, f)

exit()


 
 
#textFile = open("Existing.txt","w")
#textFile.write(inputPictureEncoding) 
#textFile.close() 
#Existing Picture
