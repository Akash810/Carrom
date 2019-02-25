# Input format is list of list
# 1 means strike(Red or Black) 
# example: [1, "Black"] or [1, "Red"]
# 2 means multisrike([Red,Black], [Black,Red], [Black,Black]) 
# example: [2,"Black","Red"] or [2,"Black","Black"]
# 3 means redstrike(Red)
# example : [3]
# 4 means strikerstrike 
# example: [4]
# 5 means defunction coin(red or black)
# example: [5, "Red"] or [5, "Black"]
# 6 means blank chance
# example: [6]
INPUT_AA = {
	"input": [
	[1, "Red"]
	]
}
INPUT_AB = {
	"input": [
	[2,"Red","Red"]
	]
}
INPUT_R = {
	"input": [
	[2, "Red","Red"]
	]
}

INPUT_Q = {
	"input": [
		[6],
		[6],
		[6],
		[6],
		[6],
		[6]
	]
}

INPUT_T = {
	"input": [
		[5, "Black"],
		[5, "Black"],
		[5, "Black"],
		[5, "Black"],
		[5, "Black"],
		[5, "Red"]
	]
}



INPUT_Z = {
	"input": [
		[3],
		[5, "Red"],
		[3],
		[5, "Red"],
		[3],
		[5, "Red"]
	]
}

INPUT_P = {
	"input": [
		[5, "Red"]
	]
}

INPUT_L = {
	"input":  [
		[1,"Black"],
		[2,"Black","Black"],
		[3],
		[5, "Red"],
		[5, "Red"],
		[2,"Red","Black"],
		[6]
	]
}

INPUT_X = {
	"input": [
		[2,"Black","Black"],									
		[2, "Black","Black"],
		[1,"Black"],
		[2,"Black","Black"],
		[2,"Red","Black"],
		[4],
		[4]
	]
}

INPUT_Y = {
	"input": [
		[1,"Black"],
		[2, "Black","Black"],
		[1,"Black"],
		[2,"Black","Black"],
		[2,"Red","Black"],
		[6],
		[2,"Black","Black"],
		[4],
		[4],
		[5]
	]
}
	