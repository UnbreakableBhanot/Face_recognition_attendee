# CODE for FACE-RECOGNITION
# Haar cascade to separate images and then face recognition library to compare images
# That's it for now DATE-10 September


import pymysql #here we go with mysql time01:42 date 20/03
import cv2
import face_recognition
import os
import sys

conn = pymysql.connect(host='localhost', user='root', password='', db='Face_DataBase')

presentStudents=[]
imagePath = 'C:/Users/shubh/PycharmProjects/Face/ImagesBasic/img.jpg'

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
   gray,
   scaleFactor=1.3,
   minNeighbors=3,
   minSize=(30, 30)
)

print("Found {0} Faces from group image.".format(len(faces)))

for (x, y, w, h) in faces:
   cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
   roi_color = image[y:y + h, x:x + w]
   #print("[INFO] Object found. Saving locally.")
   #To see object means faces found and are saved.
   path = 'C:/Users/shubh/PycharmProjects/Face/cascaded images'
   cv2.imwrite('C:/Users/shubh/PycharmProjects/Face/cascaded images/' + str(w) + str(h) + '_faces.jpg', roi_color)

status = cv2.imwrite('faces_detected.jpg', image)

#print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
#To see status is the file is written to folder or not.
for i in (os.listdir("C:/Users/shubh/PycharmProjects/Face/ImageAttendance")):
   for j in (os.listdir("C:/Users/shubh/PycharmProjects/Face/cascaded images")):
       predefineImg = face_recognition.load_image_file(f'C:/Users/shubh/PycharmProjects/Face/ImageAttendance/{i}')
       predefineImg = cv2.cvtColor(predefineImg, cv2.COLOR_BGR2RGB)
       imgCollected = face_recognition.load_image_file(f'C:/Users/shubh/PycharmProjects/Face/cascaded images/{j}')
       imgCollected = cv2.cvtColor(imgCollected, cv2.COLOR_BGR2RGB)

       faceLoc = face_recognition.face_locations(predefineImg)[0]
       encodeElon = face_recognition.face_encodings(predefineImg)[0]
       cv2.rectangle(predefineImg, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

       faceLocTest = face_recognition.face_locations(imgCollected)[0]
       encodeTest = face_recognition.face_encodings(imgCollected)[0]
       cv2.rectangle(imgCollected, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

       results = face_recognition.compare_faces([encodeElon], encodeTest)
       faceDis = face_recognition.face_distance([encodeElon], encodeTest)
        #print(results, faceDis) if want to see matching and with what distance
       cv2.putText(predefineImg, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)


       if (results==[True]):
           presentStudents.append(i)


for presenties in presentStudents:
    print(presenties)

cursor = conn.cursor()
try:
    cursor.execute("CREATE TABLE mytable (name VARCHAR(255))")
except:
    sql = "INSERT INTO mytable (name) VALUES (%s)"
for element in presentStudents:
    cursor.execute(sql, element)
conn.commit()
conn.close()