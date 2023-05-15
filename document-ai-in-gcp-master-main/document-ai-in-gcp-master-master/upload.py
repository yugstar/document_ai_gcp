import cv2
import requests
from subprocess import run
from PIL import Image

cam = cv2.VideoCapture(1,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

cv2.namedWindow("MINI PROJECT EVALUATION")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame") 
        break
    cv2.imshow("MINI PROJECT EVALUATION", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        image_1 = Image.open(r'opencv_frame_{}.png'.format(img_counter))
        im_1 = image_1.convert('RGB')
        im_1.save(r'opencv_frame_{}.pdf'.format(img_counter))
        url = "https://frontend-app-uyhj4kfzdq-uc.a.run.app/upload"
        payload={}
        files=[
          ('file',('opencv_frame_{}.pdf'.format(img_counter),open('opencv_frame_{}.pdf'.format(img_counter),'rb'),'application/pdf'))
        ]
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        print(response.text)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
