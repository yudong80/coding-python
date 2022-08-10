from collections import defaultdict

data = defaultdict(set)
data['영국'].add('바스')
data['영국'].add('런던')
korea = data['한국']
print(f'한국 방문: {korea}')