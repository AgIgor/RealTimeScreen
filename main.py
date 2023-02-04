import datetime
from PIL import ImageGrab
import numpy as ny
import cv2

# img = ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=False, xdisplay=None)
# print(img)


# height = 720  # passing 1 and getting the screen height
# width = 1280   # passing 0 and getting the screen width
# time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')  # Getting the exact time the screen is being recorded
# file_name = f'{time_stamp}.mp4'  # Getting a new value based on the time fo screen recording
# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # Declaring our encoding format
# final_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))


while True:
    img = ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=False, xdisplay=None)
    img_ny = ny.array(img)
    print(img_ny)
    img_final = cv2.cvtColor(img_ny, cv2.COLOR_BGR2RGB)
    img_final = cv2.resize(img_final, (1280, 720))
    cv2.imshow('Section screen capture', img_final)

    # final_video.write(img_final)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break