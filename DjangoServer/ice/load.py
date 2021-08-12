from django.apps import AppConfig
from tensorflow.keras.models import load_model
# import cv2

# class LoadConfig(AppConfig):
#     model = load_model('/root/ai_model/모델.h5')
#     haarcascade_dir = '/home/lab07/MTCNN HaarCascade'
#     nose_cascade = cv2.CascadeClassifier(haarcascade_dir + '/haarcascade_mcs_nose.xml')
#     detector = MTCNN()
#
#     net = cv2.dnn.readNet('/home/lab07/darknet/backup/yolov4_custom_last.weights',
#                           '/home/lab07/darknet/custom/yolov4_custom.cfg')
#     # 파일 주소 확인
#     classes = []
#     with open("/home/lab07/darknet/custom/custom.name", "r") as f:
#         # 파일 주소 확인
#         classes = f.read().splitlines()