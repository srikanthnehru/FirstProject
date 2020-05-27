from PIL import Image
import face_recognition

image = face_recognition.load_image_file("faces.jpg")

facelocations = face_recognition.face_locations(image)

for facelocation in facelocations:
    top,right,bottom,left = facelocation

    faceimage = image[top:bottom,left:right]
    pilimage = Image.fromarray(faceimage)
    pilimage.show()