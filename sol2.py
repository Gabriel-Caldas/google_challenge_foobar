def solution(pegs):
	"""
	Takes pegs list, creates a matrix to perform gauss elimination solution over
	system composed by equations equivalent of space between each pair of pegs in 
	sequence and returns radius of 1st gear in format [a, b], where r1=a/b
	"""
	import numpy as np
	from fractions import Fraction

	pegs = np.array(pegs)

	def create_equations_matrix(pegs):
		"""Takes number of pegs and distances between them and returns """
		n = len(pegs)

		distances = pegs[1:] - pegs[:-1]
		equations_matrix = np.zeros([n-1, n])
		lines = equations_matrix.shape[0]
		columns = equations_matrix.shape[1]

		for l in range(lines-1):
			for c in range(l,l+2):
				equations_matrix[l, c] = 1
		equations_matrix[lines-1, 0] = 0.5
		equations_matrix[lines-1, columns-2] = 1
		equations_matrix[:, -1] = distances

		return equations_matrix
	
	def check_possibility(r1, equations_matrix):
		rs = [r1,]
		vars = equations_matrix.shape[0]
		for i in range(vars-1):
			rn = equations_matrix[i, -1] - rs[-1]
			rs.append(rn)
		rs.append(r1/2)

		for r in rs:
			if r < 1:
				return False

		return True


	def solve_equations_matrix(equations_matrix):
		gauss_equations_matrix = equations_matrix.copy()
		if gauss_equations_matrix.shape[0] == 1:
			r1 = gauss_equations_matrix[0][-1] / 1.5
			a, b = [Fraction(r1).limit_denominator().numerator, Fraction(r1).limit_denominator().denominator]
			if r1 < 2: 
				return [-1, -1]
			return [a, b]

		lines = gauss_equations_matrix.shape[0]
		for l in range(lines-1):
			gauss_equations_matrix[-1,:] = gauss_equations_matrix[-1, :] * (-1)
			gauss_equations_matrix[-2,:] = gauss_equations_matrix[-1,:] + gauss_equations_matrix[-2, :]
			gauss_equations_matrix = gauss_equations_matrix[:-1,:]
		
		
		r1 = gauss_equations_matrix[0][-1]/gauss_equations_matrix[0][0]
		a, b = [Fraction(r1).limit_denominator().numerator, Fraction(r1).limit_denominator().denominator]
		if r1 < 2 or not check_possibility(r1, equations_matrix):
			return [-1, -1]
		else:
			return [a, b]
		


	eqs_matrix = create_equations_matrix(pegs)
	result = solve_equations_matrix(eqs_matrix)

	return result


while True:
	n = int(input("n: "))
	if n == 0:
		break
	pegs = []
	for i in range(n):
		peg = float(input((str(i) + ': ')))
		pegs.append(peg)
	print(solution(pegs))

print(solution([4,30,50]))
print(solution([4,17,50]))
print(solution([0, 15, 33, 43.5, 48.5]))
print(solution([15, 47, 55, 76]))
print(solution([15, 45]))
print(solution([8,32]))
print(solution([15, 47, 47, 76]))
print(solution([6, 44, 72, 161.5, 271, 411.5, 513.5, 516.5, 532.75]))








