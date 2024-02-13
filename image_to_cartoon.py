import cv2
import matplotlib.pyplot as plt

# Load the image using cv2
img = cv2.imread("C:/Dhruvin/Projects/Image to Cartoon/testing folder/original.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Convert to grayscale and apply median blur to reduce image noise
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayimg = cv2.medianBlur(grayimg, 5)

#Get the edges 
edges = cv2.adaptiveThreshold(grayimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)

#Convert to a cartoon version
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

#Display original image
plt.figure(figsize=(2,2))
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")
plt.show()

#Display cartoon image
plt.figure(figsize=(2,2))
plt.imshow(cartoon)
plt.axis("off")
plt.title("Cartoon Image")
plt.show()


img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.imshow("Original Image", img)

#Display cartoon image

cv2.imshow("Cartoon", cv2.cvtColor(cartoon, cv2.COLOR_RGB2BGR))

#To keep the window open until the user closes it we can use 
# the cv2.waitKey method passing 0 as parameter
cv2.waitKey (0)

#Remove the window from screen and memory after exiting the script
cv2.destroyAllWindows()