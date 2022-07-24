#recognize the atm interface
#find the number/character we want to click
#locate the number/character in the options 
#locate the box and wait for the box to illumnate and click when
#repeat untill all number/character is found and clicked.

import cv2 as cv
import numpy as np

atm = cv.imread(r"C:\Users\shakt\ERLC\Emergency-Response-Liberty-County-ATM-hack\atm2.jpg")
title = cv.imread(r'C:\Users\shakt\ERLC\Emergency-Response-Liberty-County-ATM-hack\breaching_firewall.jpg')

result = cv.matchTemplate(title, atm, cv.TM_SQDIFF_NORMED)

cv.imshow('Result', result)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
title_w = title.shape[1]
title_h = title.shape[0]
top_left = max_loc
bottom_right = (top_left[0] + title_w, top_left[1] + title_h)
cv.rectangle(atm, top_left, bottom_right, 
color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
cv.imwrite('result.jpg', atm)
cv.waitKey()

#C:\Users\shakt\ERLC\Emergency-Response-Liberty-County-ATM-hack\breaching_firewall.png