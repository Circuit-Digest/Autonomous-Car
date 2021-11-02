import cv2
import numpy as np
# from version1.histogram import hists



def findCenter(p1,p2):
    center = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
    return center

def minmax_centerPoints(tergetList,pos):

    if len(tergetList) > 0:
        maximum = max(tergetList, key = lambda i: i[pos])
        minimum = min(tergetList, key = lambda i: i[pos])
        return [maximum,minimum]
    else:
        return None


def resizeWindow(windowName1,width=640,height=480):
    cv2.resizeWindow(windowName1,width,height)
global    count
def detectedlane1(imageFrame):
    center1= 0
    center2 = 0

    resultWidth = 570
    resultHeight = 480
    points = [[55, 200], [165, 60], [505, 60], [620, 200]]

    pts2 = [[0,resultHeight], [0, 0], [resultWidth, 0], [resultWidth, resultHeight]]
    terget = np.float32(points)
    destination = np.float32(pts2)

    # Apply Perspective Transform Algorithm

    matrix = cv2.getPerspectiveTransform(terget, destination)
    result = cv2.warpPerspective(imageFrame, matrix, (resultWidth, resultHeight))
   # cv2.line(imageFrame, (points[0][0],points[0][1]), (points[1][0],points[1][1]), (0, 255, 0), 1)
   # cv2.line(imageFrame, (points[1][0],points[1][1]), (points[2][0],points[2][1]), (0, 255, 0), 1)
    #cv2.line(imageFrame, (points[2][0],points[2][1]), (points[3][0],points[3][1]), (0, 255, 0), 1)
    #cv2.line(imageFrame, (points[3][0], points[3][1]), (points[0][0], points[0][1]), (0, 255, 0), 1)
    #cv2.imshow('Main Image Window', imageFrame)
    #resizeWindow('Main Image Window')

    # cv2.waitKey(0)
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Grayscale Window', gray)
    # resizeWindow('Grayscale Window',resultWidth, resultHeight)

    threshold = cv2.inRange(gray, 80, 200)      # THRESHOLD IMAGE OF GRAY IMAGE
    # cv2.imshow('Threshold Window', threshold)
    # resizeWindow('Threshold Window',resultWidth, resultHeight)


    edges = cv2.Canny(gray, 1, 100, apertureSize=3)
    # cv2.imshow('CannyEdgeWindow',edges)
    # resizeWindow('CannyEdgeWindow',resultWidth, resultHeight)

    mergedImage = cv2.add(threshold,edges)
    #cv2.imwrite('mergedimage_'+str(count)+'.jpg',mergedImage)
    # cv2.imshow('MergedImageWindow', mergedImage)
    # resizeWindow('MergedImageWindow', resultWidth, resultHeight)
   # cv2.line(result, (pts2[0][0], pts2[0][1]), (pts2[1][0], pts2[1][1]), (0, 255, 0), 2)
    #cv2.line(result, (pts2[1][0], pts2[1][1]), (pts2[2][0], pts2[2][1]), (0, 255, 0), 2)
   # cv2.line(result, (pts2[2][0], pts2[2][1]), (pts2[3][0], pts2[3][1]), (0, 255, 0), 2)
    #cv2.line(result, (pts2[3][0], pts2[3][1]), (pts2[0][0], pts2[0][1]), (0, 255, 0), 2)
    firstSquareCenters1 = findCenter((pts2[1][0], pts2[1][1]), (pts2[2][0], pts2[2][1]))
    firstSquareCenters2 = findCenter((pts2[3][0], pts2[3][1]), (pts2[0][0], pts2[0][1]))
    print(firstSquareCenters1,firstSquareCenters2)
    #cv2.line(result, firstSquareCenters1, firstSquareCenters2, (0, 255, 0), 1)
    mainFrameCenter = findCenter(firstSquareCenters1,firstSquareCenters2)

    lines = cv2.HoughLinesP(mergedImage,1,np.pi/180,10,minLineLength=120,maxLineGap=250)

    centerPoints = []
    left = []
    right = []
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            if 0<=x1 <=resultWidth and 0<= x2 <=resultWidth :

                center = findCenter((x1,y1),(x2,y2))
              #  cv2.circle(result,center,2,(0,0,255),2)
                # cv2.line(result,(x1,y1),(x2,y2),(0,255,0),2)

                if center[0] < (resultWidth//2):
                    center1 = center
                    left.append((x1, y1))
                    left.append((x2,y2))
                else:
                    center2 = center
                    right.append((x1, y1))
                    right.append((x2,y2))
                if center1 !=0 and center2 !=0:
                    centroid1 = findCenter(center1,center2)
                    centerPoints.append(centroid1)
                    # cv2.line(result, center1, center2, (0, 255, 0), 2)


                # cv2.imshow('HoughWindow', result)
                # resizeWindow('HoughWindow',width=570,height=480)


        # lftminmax = minmax_centerPoints(left,1)
        # cv2.line(result, lftminmax[0], lftminmax[1], [0, 255, 0], 3)
        # leftCenter = findCenter(lftminmax[0],lftminmax[1])
        #
        # rtminmax = minmax_centerPoints(right, 1)
        # cv2.line(result, rtminmax[0], rtminmax[1], [0, 255, 0], 3)
        # rightCenter = findCenter(rtminmax[0], rtminmax[1])
        # print(rightCenter,leftCenter)
        # cv2.line(result, rightCenter, leftCenter, [0, 0,255], 1)
        #
        centers = minmax_centerPoints(centerPoints,1)
        laneCenters = 0
        mainCenterPosition = 0
        
        if centers is not None:
            laneframeCenter = findCenter(centers[0],centers[1])
            print(mainFrameCenter,laneframeCenter)
           # cv2.circle(result,mainFrameCenter,5,(0,0,255),-1)
           # cv2.circle(result, laneframeCenter, 5, (255, 0, 0), -1)
            mainCenterPosition = mainFrameCenter[0] - laneframeCenter[0]
            #Lines of center points of each center of the right lanes and left lanes
            # for index, item in enumerate(centerPoints):
            #     if index == len(centerPoints) - 1:
            #         break
         
           # cv2.line(result, centers[0], centers[1], [0, 255, 0], 2)
            laneCenters = centers
            print(centers)
        return [laneCenters,result,mainCenterPosition]

    # c = cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # if chr(c) == 'k':  # if 'q' is pressed then quit
    #     break


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    #count = 0
    #while True:
    while(cap.isOpened()):
        #inputString = input("EnterImageNumber: ")
    #     inputString = '1'
        #image = cv2.imread('trackImages/image_'+inputString+'.jpg')
        ret, frame = cap.read()

        if ret == True:
            # Display the resulting frame
            laneimage1 = detectedlane1(frame)
           # if laneimage1 is not None:
           #     cv2.putText(laneimage1[1],"Pos="+str(laneimage1[2]),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
           #     cv2.imshow('FinalWindow',laneimage1[1])
            print("Position-> "+str(laneimage[2]))
         #   else:
                #cv2.imshow('FinalWindow', image)
            #resizeWindow('FinalWindow',570, 480)
            # cv2.waitKey(0)

            #c = cv2.waitKey(1) % 256
            #if chr(c) == 'k':  # if 'q' is pressed then quit
             #   cv2.waitKey(0)
            #    cv2.destroyAllWindows()
             #   break
           # elif chr(c) == 'i':  # if 'q' is pressed then quit
              #  cv2.imwrite('calibratedImage_'+str(count)+'.jpg',laneimage1[1])
           # count += 1

        # points = [[30, 200], [150, 60], [520, 60], [640, 200]]
        #
        # cv2.line(imageFrame, (points[0][0],points[0][1]), (points[1][0],points[1][1]), (0, 255, 0), 3)
        # cv2.line(imageFrame, (points[1][0],points[1][1]), (points[2][0],points[2][1]), (0, 255, 0), 3)
        # cv2.line(imageFrame, (points[2][0],points[2][1]), (points[3][0],points[3][1]), (0, 255, 0), 3)
        # cv2.line(imageFrame, (points[3][0], points[3][1]), (points[0][0], points[0][1]), (0, 255, 0), 3)

        # detectedlane1(image)

        # (50, 283) (222, 18) first line
        # (530, 141) (639, 291) 2nd line
        # cv2.imshow('HoughWindow', imageFrame)

        # k = cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # (95, 479) (95, 0) line1
        # (508, 437)(508, 282) line2