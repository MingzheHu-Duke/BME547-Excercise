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

def cal_slope(point_1, point_2):
	slope = (point_2[1] - point_1[1])/(point_2[0] - point_1[0])
	print("The line formed is : \n y = {}x + {}".format(slope, point_1[1]-slope*point_1[0]))
	return slope
	
def cal_y(point_1, point_2, x_value):
	slope = cal_slope(point_1, point_2)
	y = slope*x_value + point_1[1]-slope*point_1[0]
	return y
	
if __name__ == "__main__":
	point_1, point_2, x_value = user_input()
	y = cal_y(point_1, point_2, x_value)
	print("The corresponding y value on the line is {}".format(y))
