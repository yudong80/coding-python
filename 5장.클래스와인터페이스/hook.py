names = ['소크라테스', '아르키메데스', '플라톤', '아리스토텔레스']
names.sort(key=len)
print(names)

# 내가 만든 func
def minus_len(obj):
    return len(obj) * -1

names.sort(key=minus_len)
print(names)