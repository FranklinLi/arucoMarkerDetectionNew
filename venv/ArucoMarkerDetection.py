import cv2
import cv2.aruco

img = cv2.imread('13.jpg')
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)

parameters = cv2.aruco.DetectorParameters_create()

# Detect the markers.
corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(img,aruco_dict,parameters=parameters)

print(corners)
print(ids)
print(rejectedImgPoints)

out = cv2.aruco.drawDetectedMarkers(img, corners, ids)



cv2.imshow("out",out)
cv2.waitKey(0)
cv2.destroyAllWindows()