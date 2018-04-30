import os
import argparse
import cv2 as cv



def display(name, camera=True):
	if camera:
		cap = cv.VideoCapture(0)
		title = 'webcam'
	else:
		cap = cv.VideoCapture(name)
		title = os.path.basename(name)

	gray, mirror = False, False
	while True:
		ret, frame = cap.read()
		if mirror:
			frame = cv.flip(frame, 1)
		if gray:
			frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
		cv.imshow(title, frame)
		
		key = cv.waitKey(1)
		if key in [27, 81, 113]:
			break
		if key in [71, 103]:
			gray = not gray
		if key in [77, 109]: 
			mirror = not mirror
	
	cap.release()
	cv.destroyAllWindows()


def main():
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-c', '--camera', action='store_true', help='Whether to use display feed from webcam.')
	group.add_argument('-f', '--file', type=str, help='Filename of video to display.')
	args = parser.parse_args()
	
	display(args.file, args.camera)



if __name__=='__main__':
	main()
