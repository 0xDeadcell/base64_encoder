import sys
from itertools import zip_longest


def grouper(raw_binary, group_size):
    return [raw_binary[n:n+group_size] for n in range(0, len(raw_binary), group_size)] 


def read_input(data: str):
	ascii_ord_to_bin([ ord(i) for i in data])  # Gets the ordinal value of the char


def ascii_ord_to_bin(ord_values):
	bin_list = []

	for i in ord_values:
		if len(bin(i)[2:]) < 8:
			bin_list.append(bin(i)[2:].zfill(8))
	base64_list = grouper("".join(bin_list), 6)
	finished_base64 = []

	for i in base64_list:
		if len(i) == 6:
			finished_base64.append(i)

		else:
			finished_base64.append(i.ljust(6, '0'))

	#print(" ".join(bin_list) + " --> " + " ".join(finished_base64))
	#print(ord_values, " --> ", [ int("0b" + i, 2) for i in finished_base64 ], end='\n\n')
	translate_ord_to_base64([ int("0b" + i, 2) for i in finished_base64 ])


def translate_ord_to_base64(ord_list):
	chr_mapping = hashmap = {0: 'A', 16: 'Q', 32: 'g', 48: 'w', 1: 'B', 17: 'R', 33: 'h', 49: 'x',2: 'C', 18: 'S', 34: 'i', 50: 'y',3: 'D', 19: 'T', 35: 'j', 51: 'z',4: 'E', 20: 'U', 36: 'k', 52: '0',5: 'F', 21: 'V', 37: 'l', 53: '1',6: 'G', 22: 'W', 38: 'm', 54: '2',7: 'H', 23: 'X', 39: 'n', 55: '3',8: 'I', 24: 'Y', 40: 'o', 56: '4',9: 'J', 25: 'Z', 41: 'p', 57: '5',10: 'K', 26: 'a', 42: 'q', 58: '6',11: 'L', 27: 'b', 43: 'r', 59: '7',12: 'M', 28: 'c', 44: 's', 60: '8',13: 'N', 29: 'd', 45: 't', 61: '9', 14: 'O', 30: 'e', 46: 'u', 62: '+',15: 'P', 31: 'f', 47: 'v', 63: '/'}

	base64_short = []
	for i in ord_list:
		base64_short.append(chr_mapping[i])

	while len(base64_short) % 4 != 0:
		base64_short.append('=')

	print("".join(sys.argv[1:]), " --> ", "".join(base64_short))


if __name__ == "__main__":
	if len(sys.argv) >= 2:
		read_input(data='{}'.format(" ".join(sys.argv[1:])))
	else:
		print("sys.argv requires at least one argument as input.")
