# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:06:34 2022

@author: W
"""

import cv2
import sys
from tqdm import tqdm


#path = "C:/workspace/workspace-spider/VR2/"
#imagePath = path + "source.png"
#distanceFilePath = path + "point.txt"

input_file_path = "C:/workspace/workspace-spider/VR2/source.png"
output_file_path = "C:/workspace/workspace-spider/VR2/point.txt"

#높을수록 거리 밀집도가 떨어짐
distancePrecisionRatio = "auto"


#높을수록 소수점 정확도가 높아짐
decimalPointPrecisionRatio = 3

argv_length = len(sys.argv)

if argv_length < 3:
    print("<argv is not correct>")
    print("argv1 : source image file input path")
    print("argv2 : point text file output path")
    print("argv3 : precision ratio (default : auto)", sep="")
    print("argv4 : decimal point precision ratio (default : ", decimalPointPrecisionRatio, ")", sep="")
    print("your input argv is ", len(sys.argv))
    sys.exit()
else:
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    if argv_length >= 4 : distancePrecisionRatio = float(sys.argv[3])
    if argv_length == 5 : decimalPointPrecisionRatio = int(sys.argv[4])
    
image = cv2.imread(input_file_path)
   
if image is None:
    print("argv1 is wrong path")
    sys.exit()

h, w, c = image.shape
b, g, r = cv2.split(image)

if distancePrecisionRatio == "auto" : distancePrecisionRatio = round(h / 200.0, 0)

print("")
print("input path                 :", input_file_path)
print("output path                :", output_file_path)
print("distancePrecisionRatio     :", distancePrecisionRatio)
print("decimalPointPrecisionRatio :", decimalPointPrecisionRatio, "\n")

distanceFile = open(output_file_path, "w")

count = 0;

for i in tqdm(range(h)):
    
    if i % distancePrecisionRatio != 0: continue    
    for j in range(w):
        if j % distancePrecisionRatio != 0: continue
        data = (1 - round((b[i,j])/255, decimalPointPrecisionRatio))
        distanceFile.write(f"{data}")
        count += 1;
        if j < w - distancePrecisionRatio:
            distanceFile.write(",")
    if i < h - distancePrecisionRatio:
        distanceFile.write("\n")
    
distanceFile.close()
print(count);