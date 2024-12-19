import array

symbols = "$¢£¥€¤"
# print(tuple(ord(symbol) for symbol in symbols))
print(array.array("I", (ord(symbol) for symbol in symbols)))
