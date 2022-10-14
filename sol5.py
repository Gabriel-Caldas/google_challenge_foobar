def solution(x, y):
	"""
		Takes x and y and returns the fewest number of times that a set of numbers (1,1) 
		must interact between then (as sums) until have (x,y) or the string "impossible" if this can't be done
	"""
	xy = [int(x), int(y)]

	gens = 0

	while min(xy) > 0:
		mins_in_max = max(xy)//min(xy) #number of times the lowest number will be added until get as close as possible to the max number
		rest = max(xy)%min(xy) # the rest from the "reach atempt"
		if rest == 0 and min(xy) != 1: # if there's no rest and the minimum number its not 1, it didnt start as (1,1), so = impossible
			return 'impossible'
		gens += mins_in_max
		xy = [min(xy), rest] # new max to reach
	
	gens = gens - 1 
	sol = str(gens)	
	
	return sol


print(solution('4','1'))
print(solution('2','2'))
print(solution('1','1'))
print(solution('2','1'))
print(solution('3','5'))
print(solution('2','4'))
l = 10**50
print(solution(str(l),'1'))
print(solution('18','2'))
print(solution('50','7'))


