from example11_13 import Pixel


class ColorPixel(Pixel):
    __slots__ = ('color',)

cp = ColorPixel()
# print(cp.__dict__)
cp.x = 2
cp.color = 'blue'
cp.flavor = 'banana'
