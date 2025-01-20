class Vowels:
    def __getitem__(self, i):
        return 'AEIOU'[i]

v = Vowels()
# print(v[0])
# print(v[-1])
# for c in v: print(c)
print('E' in v)
print('Z' in v)

