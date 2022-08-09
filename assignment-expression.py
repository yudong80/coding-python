fresh_fruit = {
    '사과': 10, 
    '바나나' : 8
}
if count := fresh_fruit.get('사과',0):
    print('make 레모네이드')
else:
    print('out of stock')