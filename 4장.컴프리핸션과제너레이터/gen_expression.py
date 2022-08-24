it = (len(x) for x in open('my_file.txt'))

# generator 합성 
roots = ((x, x**0.5) for x in it)
print(next(roots)) # 첫 라인이 100자임
