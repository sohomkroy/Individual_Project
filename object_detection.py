
import numpy as np
import cv2

import time

# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

COLORS[7] = (0, 0, 255)

COLORS[15] = (255, 0, 0)

# load our serialized model from disk
print("getting model")
net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")


frame = cv2.imread("Capture.png")



(h, w) = frame.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                                 0.007843, (300, 300), 127.5)

# pass the blob through the network and obtain the detections and
# predictions
time.sleep(10)
print("done waiting")
start = time.clock()
net.setInput(blob)
detections = net.forward()
middle = time.clock()

count = 1

for i in np.arange(0, detections.shape[2]):
    # extract the confidence (i.e., probability) associated with
    # the prediction
    confidence = detections[0, 0, i, 2]

    # filter out weak detections by ensuring the `confidence` is
    # greater than the minimum confidence
    if confidence > .2:
        print(detections[0, 0, i, 3:7])
        # extract the index of the class label from the
        # `detections`, then compute the (x, y)-coordinates of
        # the bounding box for the object
        idx = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        if CLASSES[idx] != "person":
            # continue
            pass



        #label = "{}: {:.2f}% {} {}".format(CLASSES[idx],
        #                                   confidence * 100)

        label = "{}".format(CLASSES[idx])
        if count in (1, 5):
            label = label + "; left "
        if count in (0, 3):
            label = label + "; none "
        if count in (2, 4):
            label = label + "; right "
        count = count + 1

        cv2.rectangle(frame, (startX, startY), (endX, endY),
                      COLORS[idx], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15

        size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, .5, 1)
        cv2.rectangle(frame, (startX-3, y-13), (startX+size[0][0]+6, y+size[0][1]-5), (255, 255, 255), -1)
        #cv2.rect
        #cv2.rectangle(frame, startX, y, (255, 255, 255))
        cv2.putText(frame, label, (startX, y),
                    cv2.FONT_HERSHEY_COMPLEX, .5, COLORS[idx], 1)


        # break

# show the output frame
# frame = cv2.resize(frame, (width*2, height*2))
end = time.clock()


#frame = cv2.resize(frame,(960,540))
cv2.imshow("Frame", frame)
#print("start to middle: {}".format(middle-start))
#print("middle to end: {}".format(end-middle))
#print("total time: {} seconds".format(end-start))
#img = cv2.imread('final_image.png',0)
cv2.imwrite('final_image.png',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()


