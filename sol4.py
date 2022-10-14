import time
import numpy as np 
def solution(l):
	# start = time.time()
	# print('time to import numpy: ', time.time() - start)


	if len(l) < 3:
		return 0

	l = np.array(l)
	lucky_triples = []

	for x in l[:-3]:
		l = l[1:]
		# start = time.time()
		ys = l[[num.is_integer() for num in l/float(x)]]
		# print('time to divide list: ', time.time() - start)

		for y in ys:
			ys = ys[1:]
			# start = time.time()
			zs = ys[[num.is_integer() for num in ys/float(y)]]
			# print('time to divide list: ', time.time() - start)


			for z in zs:
				triple = [x, y, z]
				lucky_triples.append(triple)
	
	
	return len(lucky_triples)

start_time = time.time()
list = [1]*1000
print(solution(list))
print('Time: ', time.time() - start_time)
# while True:
# 	l = input("list: ")
# 	l = list(l)
# 	if not l:
# 		break
# 	sol = solution(l) 
# 	print(sol)


