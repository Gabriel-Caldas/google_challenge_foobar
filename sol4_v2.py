import time
import numpy as np
def solution(l):
	if len(l) < 3:
		return 0

	l = np.array(l)
	count = 0
	for x in l[:-2]:
		x = l[0]
		l = l[1:]
		ys = l[l%x == 0]
		for iy, y in enumerate(ys):
			zs = ys[iy+1:]
			zs = zs[zs%y == 0]
			count += zs.shape[0]
	
	return count




start_time = time.time()
list = [1]*2000
print(solution(list))

print('Time: ', time.time() - start_time)


