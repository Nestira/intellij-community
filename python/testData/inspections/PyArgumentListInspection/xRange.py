print(xrange(<warning descr="Parameter(s) unfilledPossible callees:xrange(self: xrange, stop: int)xrange(self: xrange, start: int, stop: int, step: int=...)">)</warning>)
print(xrange(1))
print(xrange(1, 2))
print(xrange(1, 2, 3))
print(xrange<warning descr="Unexpected argument(s)Possible callees:xrange(self: xrange, stop: int)xrange(self: xrange, start: int, stop: int, step: int=...)">(1, 2, 3, 4)</warning>)
