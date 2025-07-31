from datetime import *

def is_it_valid(pic: str):
	if len(pic) != 11:
		return False
	else:
		dd = pic[0:2]
		mm = pic[2:4]
		yy = pic[4:6]
		X = pic[6]
		try:
			full_year = ""
			if X == "+":
				full_year += "18"
			elif X == "-":
				full_year += "19"
			elif X == "A":
				full_year += "20"
			else:
				return False
			full_year += yy
			new_date = datetime(int(full_year), int(mm), int(dd))
		except:
			return False
		yyy = pic[7:10]
		z = pic[10]
		try:
			numbered_string = dd + mm + yy + yyy
			number = int(numbered_string)
			remainder = number % 31
			default_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
			if default_string[remainder] != z:
				return False
		except:
			return False
		return True

if __name__ == "__main__":
	print(is_it_valid("230827-906F"))
	print(is_it_valid("120488+246L"))
	print(is_it_valid("310823A9877"))
	print(is_it_valid("100400A644E"))