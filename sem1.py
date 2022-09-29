my_str = 'Домашка очень неабв сложная !'.split()
print(' '.join([word for word in my_str if 'абв' not in word]))