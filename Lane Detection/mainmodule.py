import cv2
import time
import threading
from lanedetection import detectedlane1 as laneDetected
import motors as mot




def resultantLane():
    # global points
    
    cap = cv2.VideoCapture(0)
    count = 0
    # while True:
    while (cap.isOpened()):
        #inputString = input("EnterImageNumber: ")
        #     inputString = '1'
        #image = cv2.imread('trackImages/image_' + inputString + '.jpg')
        ret, frame = cap.read()
        LIMITDIR = 17
        if ret == True:
        # Display the resulting frame
            laneimage1 = laneDetected(frame)
            if laneimage1 is not None:
                #cv2.putText(laneimage1[1], "Pos=" + str(laneimage1[2]), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                         #   (0, 255, 0))
               # cv2.imshow('FinalWindow', laneimage1[1])
                direction = laneimage1[2]
                if direction >LIMITDIR:
                    mot.fright(40,0.2)
                elif direction<-LIMITDIR:
                    mot.fleft(40,0.2)

                elif -LIMITDIR<= direction <= LIMITDIR:
                    mot.forward(30,0.2)
                else:
                    mot.stop()
                
            #else:
                #cv2.imshow('FinalWindow', image)
            #cv2.resizeWindow('FinalWindow', 570, 480)
            # cv2.waitKey(0)

           # c = cv2.waitKey(1) % 256
           # if chr(c) == 'k':  # if 'q' is pressed then quit
          #      cv2.waitKey(0)
          #      cv2.destroyAllWindows()
           # elif chr(c) == 'i':  # if 'q' is pressed then quit
           #     cv2.imwrite('calibratedImage_' + str(count) + '.jpg', laneimage1[1])
          #  count += 1
                time.sleep(0.1)
            

#def motorsControl():
    # c = cv2.waitKey(1) % 256


    

threads = []



def main():

    


    t1 = threading.Thread(target=resultantLane)
    #t2 = threading.Thread(target=motorsControl)
    t1.start()
    #t2.start()
    threads.append(t1)
    #threads.append(t2)
    #

    for t in threads:
        t.join()

    print("Threading Done!")


if __name__ == '__main__':
    main()
