def create_tuple(x: int, y: int, z: int):
	smallest = None
	greatest = None
	if x <= y <= z:
		smallest = x
		greatest = z
	elif x <= z <= y:
		smallest = x
		greatest = y
	elif y <= x <= z:
		smallest = y
		greatest = z
	elif y <= z <= x:
		smallest = y
		greatest = x
	elif z <= y <= x:
		smallest = z
		greatest = x
	elif z <= x <= y:
		smallest = z
		greatest = y
	sumof = x + y + z
	return (smallest, greatest, sumof)

if __name__ == "__main__":
	print(create_tuple(5, 3, -1))