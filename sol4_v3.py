def solution(l):
	"""takes a list of positive integers l and counts the number of 
	"lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k."""
	
	size = len(l)
	if size < 3:
		return 0
	
	triples = 0
	
	for i in range(1,size-1): ## i runs gets the index of each possible y position
		xs_for_y = len([x for x in l[:i] if l[i] % x == 0]) # all possibles x's (to the left) for the y (l[i])
		zs_for_y = len([z for z in l[i+1:] if z % l[i] == 0]) # all possibles z's (to the right) for the y
 
		triples_for_y = xs_for_y * zs_for_y 
		triples += triples_for_y
	
	return triples

print(solution([1]*2000))