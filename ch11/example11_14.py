from example11_13 import Pixel


class OpenPixel(Pixel):
    pass

op = OpenPixel()
print(op.__dict__)
op.x = 8
print(op.__dict__)
print(op.x)
op.color = 'green'
print(op.__dict__)
