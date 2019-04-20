# python real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel
# cd Sohom\Programming_Data\Individual_Project

from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import imutils
import time
import cv2
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
import threading
import sys


#classes that we can detect
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]
#random colors for fun
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
#read model
print("getting model")
net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")
#get video stream
print("starting stream")
vs = VideoStream(1).start()
#vs = cv2.VideoCapture(0)
time.sleep(5)
fps = FPS().start()
#threshold for destance to report error
distance_threshold = 60
#text scaling and thickness
text_scale = 1
text_thickness = 3
#set to true if we only want to detect people
only_people = True


threadLock = threading.Lock()
tracked_detections_new = {}
tracked_detections_old ={}
spoken_detections = {}

z_error = 0


class trackingThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):

        global z_error
        while True:
            tracked_detections_new = {}
            # get frame and process detections
            frame = vs.read()
            frame = imutils.resize(frame, width=800)

            (h, w) = frame.shape[:2]

            blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                                         0.007843, (300, 300), 127.5)
            net.setInput(blob)
            detections = net.forward()

            for i in np.arange(0, detections.shape[2]):

                confidence = detections[0, 0, i, 2]

                if confidence > .2:

                    idx = int(detections[0, 0, i, 1])
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    # continue if we only want people
                    if (CLASSES[idx] != "person") and only_people:
                        continue
                    # find "center" of detection (1/3 from top because follows toso/face)
                    # do some math
                    center_rect = int((startX + endX) / 2), int((startY + endY) / 3)
                    height, width, channels = frame.shape
                    center_frame = (int(width / 2), int(height / 2))
                    distance = int(
                        np.sqrt([(center_rect[0] - center_frame[0]) ** 2 + (center_rect[0] - center_frame[0]) ** 2]))
                    x_distance = (center_rect[0] - center_frame[0])
                    y_distance = (center_rect[1] - center_frame[1])

                    # check if centered
                    centered = True if distance < distance_threshold else False

                    centered_or_not = "centered" if centered else "not centered"
                    label = "{}: {:.2f}% {} {}".format(CLASSES[idx],
                                                       confidence * 100, distance, centered_or_not)
                    # draw on frame to give info
                    cv2.rectangle(frame, (startX, startY), (endX, endY),
                                  COLORS[idx], 2)
                    y = startY - 15 if startY - 15 > 15 else startY + 15
                    cv2.putText(frame, label, (startX, y),
                                cv2.FONT_HERSHEY_SIMPLEX, text_scale, COLORS[idx], text_thickness)
                    # draw circle to represent "center" of frame and circle to represent threshold
                    cv2.circle(frame, center_rect, 4, COLORS[idx], thickness=4)
                    cv2.circle(frame, center_frame, distance_threshold, (0, 255, 0), thickness=1)
                    tracked_detections_new[str(CLASSES[idx])] = (int((startX + endX) / 2), int((startY + endY) / 2))
                    z_error = center_frame[0]-center_rect[0]


            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

            fps.update()
        sys.exit()

class speakingThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        while True:
            #print("yeet")
            #threadLock.acquire()
            global spoken_detections
            for key, value in spoken_detections.items():
                if value != "not moving":
                    speak.Speak(key + " " + value+",")
                    time.sleep(.2)
                #print(key + " " + value)
                #speak.Speak(key + " " + value + ",")

            if (tracking_thread.isAlive()):
                pass
            else:
                sys.exit()
            #threadLock.release()
import paramiko
import time
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn = s.connect("169.254.231.124", username ='pi', password='Greeny25448', port=22)


command = 'cd /home/pi/Desktop/IndividualProject/teststesteststsew \n echo "' +str(z_error)+ '" > file.txt'
#print(x_error)
(stdin, stdout, stderr) = s.exec_command(command)



class stabalizeThread (threading.Thread):
    def __init__(self, threadID, name, tracker_thread):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadID = threadID
        self.name = name
        self.tracker_thread = tracker_thread
    def run(self):
        #global x_error
        while self.tracker_thread.is_alive():
            command = 'cd /home/pi/Desktop/IndividualProject/teststesteststsew \n echo "' +str(int(z_error/30))+ '" > file.txt'
            print(z_error/10)
            (stdin, stdout, stderr) = s.exec_command(command)
            time.sleep(1 / 12)
        command = 'cd /home/pi/Desktop/IndividualProject/teststesteststsew \n echo "' + "done" + '" > file.txt'
        print(z_error)
        (stdin, stdout, stderr) = s.exec_command(command)


tracking_thread = trackingThread(1, "tracking")
#speaking_thread = speakingThread(1, "speaking")
tracking_thread.start()
stabalize = stabalizeThread(1, "stabalize", tracking_thread)
stabalize.start()
#speaking_thread.start()
#speaking_thread.join()
tracking_thread.join()
fps.stop()
print("time: {:.2f}".format(fps.elapsed()))
print("fps: {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()
#vs.stop()
