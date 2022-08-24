a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)

even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
threes_cube_set = {x**3 for x in a if x % 3 == 0}
print(even_squares_dict)
print(threes_cube_set)

c = [x for x in a if x > 4 and x % 2 ==0 ]
print(c)