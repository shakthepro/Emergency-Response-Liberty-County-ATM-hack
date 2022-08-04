#locate the number/character in the options 
#locate the box and wait for the box to illumnate and click when
#repeat untill all number/character is found and clicked.
from mss import mss
from PIL import Image
import cv2 as cv
import numpy as np
import pyautogui as py

atm = cv.imread(r"C:\Users\shakt\ERLC\Emergency-Response-Liberty-County-ATM-hack\atm2.jpg")
title = cv.imread(r'C:\Users\shakt\ERLC\Emergency-Response-Liberty-County-ATM-hack\breaching_firewall.jpg')
selectCode = cv.imread(r"C:\Users\shakt\ERLC\Emergency-Response-Liberty-County-ATM-hack\SelectCode.png")

#recognize the atm interface
result = cv.matchTemplate(title, atm, cv.TM_CCOEFF)

#draw box from the result
def draw_box(image):
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print(max_loc)
    title_w = title.shape[1]
    print(title_w)
    title_h = title.shape[0]
    print(title_h)
    top_left = max_loc
    global bottom_right
    bottom_right = (top_left[0] + title_w, top_left[1] + title_h)
    cv.rectangle(image, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
    return cv.imshow("image", image)

# show results
draw_box(atm)
cv.imwrite('result.jpg', atm)
cv.waitKey()

#find the number/character we want to click

codeRead = cv.imread(r"C:\Users\shakt\ERLC\Emergency-Response-Liberty-County-ATM-hack\SelectCode.png")
result =  cv.matchTemplate(codeRead, atm, cv.TM_SQDIFF_NORMED)
draw_box(codeRead)
cv.imwrite('codeRead.jpg', codeRead)
cv.waitKey()

#get the location of the box and look right 160 pixels and 35 down from the top right corner 
selectCode = cv.imread(r"C:\Users\shakt\ERLC\Emergency-Response-Liberty-County-ATM-hack\fullcode.png")
code_number = cv.rectangle(selectCode, (bottom_right[0] + 160, bottom_right[1] + 35), (bottom_right[0] + 160 + 20, bottom_right[1] + 35 + 20), color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
cv.imwrite('code_number.jpg', code_number)




#recording
size = py.size()
x = size[0]
y = size[1]

bounding_box = {'top': 100, 'left': 0, 'width': x, 'height': y}

sct = mss()

while True:
    sct_img = sct.grab(bounding_box)
    cv.imshow('screen', np.array(sct_img))


    if (cv.waitKey(1) & 0xFF) == ord('q'):
        cv.destroyAllWindows()
        break
    



#C:\Users\shakt\ERLC\Emergency-Response-Liberty-County-ATM-hack\breaching_firewall.png