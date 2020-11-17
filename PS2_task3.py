# Group NO 6
# Raj Gorhekar 2018130013
# Afan Ansari 2019230064
# EXP 5 Task 2

import numpy as np
from PS2_task2 import syndrome_decode

arr = [
    [1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 1],
]
G = np.array(arr)
valid_codewords = []

for i in range(16):
    msg = []
    for j in list("0"*(6-len(str(bin(i))))+str(bin(i))[2:]):
        msg.append(int(j))
    valid_codewords.append(np.mod(np.dot(np.array(msg), G), 2))

print("Testing all 2**k = 16 valid codewords")
for i in valid_codewords:
    decoded = syndrome_decode(i,7,4,G)
    if not np.array_equal(i[:4],decoded[0][:4]):
        quit()
print("...passed")

print("Testing all n*2**k = 112 single-bit error codewords")
for i in valid_codewords:
	current = i.copy()
	for j in range(7):
		current[j] = [1, 0][current[j]]
		decoded = syndrome_decode(current,7,4,G)
		print(f"Error Occured at Position {j} Got {current} and Expected {decoded[0]} .Error was corrected using Syndrome Decode")
		if not np.array_equal(i[:4],decoded[0][:4]):
			print("OOPS: Error decoding",current,"...expected",i[:4],"got",decoded[0][:4])
			quit()
print(f"...passed\nAll 0 and 1 error tests passed for (7,4,3) code with generator matrix G ={G}")
