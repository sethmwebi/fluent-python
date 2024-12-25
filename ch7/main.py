# def factorial(n):
#     """returns n!"""
#     return 1 if n < 2 else n * factorial(n - 1)
#
#
# # print(factorial.__doc__)
# # print(help(factorial))
# print(dir(factorial))
import bobo


@bobo.query("/")
def hello(person):
    return f"Hello {person}!"
