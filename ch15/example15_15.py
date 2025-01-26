from ch13.example13_10 import LottoBlower

machine = LottoBlower[int](range(1,11))

first = machine.pick()
remain = machine.inspect()
