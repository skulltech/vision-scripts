from scipy.spatial import distance
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import cv2 as cv



def midpoint(ptA, ptB):
    return (ptA[0] + ptB[0]) / 2, (ptA[1] + ptB[1]) / 2


def main():
    parser = argparse.ArgumentParser
    parser.add_argument('-i', '--image', required=True, help='Path to input image')
    parser.add_argument('-w', '--width', required=True, help='Width of left-most object in the image')
    args = parser.parse_args()



if __name__=='__main__':
    main()
