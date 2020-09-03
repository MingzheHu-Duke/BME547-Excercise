def user_input():
	print("please input the first point(x1, y1)  on the plane :")
	point_1 = (input().replace("(", "")).replace(")", "")
	point_1 = tuple(map(float, point_1.split(',')))
	print("please input the second point (x2, y2) on the plane :")
	point_2 = (input().replace("(", "")).replace(")", "")
	point_2 = tuple(map(float, point_2.split(',')))
	if point_1 == point_2:
		print("You entered the same point twice, please re-enter the second point")
		point_2 = (input().replace("(", "")).replace(")", "")
		point_2 = tuple(map(float, point_2.split(',')))
	if point_1[0] == point_2[0]:
		print("Warning! Vertical line, infinite y values! Program terminated!")
		quit()
	print("please choose a x coordinate that you like")
	print("We will give you the y value of it on the line created by first two point:")
	x_value = float(input())
	return point_1, point_2, x_value
