'''
Implementing the following tutorial from pyimagesearch.com.
https://www.pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/
'''
from scipy.spatial import distance
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import cv2 as cv



def midpoint(ptA, ptB):
    return (ptA[0] + ptB[0]) / 2, (ptA[1] + ptB[1]) / 2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', required=True, type=str, help='Path to input image')
    parser.add_argument('-w', '--width', type=int, help='Width of left-most object in the image')
    args = parser.parse_args()

    img = cv.imread(args.image, cv.IMREAD_COLOR)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Image', gray)
    cv.waitKey(0)



if __name__=='__main__':
    main()
