import face_recognition

class FaceRecognition:

    def getEncodePicture(self, path):
        pictureInput         = face_recognition.load_image_file(path)
        inputPictureEncoding = face_recognition.face_encodings(pictureInput)[0]
        return inputPictureEncoding 