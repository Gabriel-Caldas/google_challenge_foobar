def solution(area):
    """Takes the total area of solar panels (from 1 to 1M) and returns
        a list of the areas of the largest squares you could make out of those panels,
        starting with the larges squares first
    """
    from math import sqrt
    
    squares = []
    
    remaining_area = area
    test_area = area
    
    while (test_area > 0):
        if sqrt(test_area).is_integer():
            squares.append(test_area)
            remaining_area = remaining_area - test_area
            test_area = remaining_area
        else:
            test_area = test_area - 1 
		
    return(squares)
    
print(solution(12))

