from example14_4 import A

class U():
    def ping(self):
        print(f'{self}.ping() in LeafUA')
        super().ping()

class LeafUA(U, A):
    def ping(self):
        print(f'{self}.ping() in LeafUA')
        super().ping()
