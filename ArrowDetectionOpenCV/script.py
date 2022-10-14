import cv2, sys
import numpy as np

# print(sys.argv)
lower = np.array([0, 0, 120]) # deepest red value
upper = np.array([100, 100, 255]) # brightest red value

try:
	cap = cv2.VideoCapture(sys.argv[1])
except:
	cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	# cv2.imshow("bgr", frame)
	mask = cv2.inRange(frame, lower, upper)
	masked = cv2.bitwise_and(frame, frame, mask = mask)
	# cv2.imshow("masked", masked)

	gray = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
	_, thresh = cv2.threshold(gray, 5, 255, cv2.THRESH_BINARY)

	cv2.erode(thresh, np.ones((1,1)), iterations = 100)
	cv2.dilate(thresh, np.ones((1,1)), iterations = 100)

	thresh = cv2.medianBlur(thresh, 3)

	ctrs, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for ctr in ctrs:
		approx = cv2.approxPolyDP(ctr, 0.03 * cv2.arcLength(ctr, True), True)
		pts = [(ary[0][0], ary[0][1]) for ary in approx]
		inc = []
		ang = []

		# print(len(approx), cv2.contourArea(ctr))
		if len(pts) == 7 and cv2.contourArea(ctr) > 1e3:
			for i in range(7):
				if i == 6: # if it's the last index, take first element
					theta = np.arctan2 (
						pts[i][1] - pts[0][1], # diff of their y-coord 
						pts[i][0] - pts[0][0] # diff of their x-coord
					)

				else: # else take consecutive elements
					theta = np.arctan2 (
						pts[i][1] - pts[i+1][1], 
						pts[i][0] - pts[i+1][0]
					)

				# limit the theta in 0..360 and append it to inclinations
				inc.append((theta * 180 / np.pi + 360) % 360)
			# print(inc)

			for i in range(7):
				if i == 6: # the same logic as in prev loop
					diff = abs(inc[i] - inc[0]) # diff of first and last
				else:
					diff = abs(inc[i] - inc[i+1]) # diff of consectutive elem

				# append the angles rounded to nearest multiple of 45 deg
				ang.append(round(diff / 45) * 45)

			deg = [a % 90 for a in ang] # take the angles in I quad
			# print(ang)

			if deg.count(45) == 2: # if only two 45 deg are there
				f = deg.index(45) # the first 45 deg
				l = 6 - deg[::-1].index(45) # the last 45 deg

				# the following if-else extract the index of 90deg when it's in between and when it's not
				if abs(f-l) == 2: # it's in between
					direc = inc[(f+l)//2]
				elif l == 5: # 90deg is at last
					direc = inc[6]
				elif f == 1: # 90deg is at first
					direc = inc[0]

				direc = ((direc - 45) + 360) % 360 
				# remove the extra 45deg inclination which the arrow head has, and limit it in 0..360

				print(direc) # print IT!!

	cv2.imshow("thresh", thresh)
	if cv2.waitKey(1) == 27: # check for Esc press
		break

cap.release()
