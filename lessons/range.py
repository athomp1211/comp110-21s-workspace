"""Range example."""

start: int = 0
stop: int = 101
step: int = 10

a_range: range = range(start, stop, step)
print(a_range.start)
print(a_range.stop)
print(a_range.step)
print(a_range[0])
print(a_range[1])
print(a_range[2])
print(len(a_range))
print(f"Max value in range: {a_range[len(a_range) - 1]}")
