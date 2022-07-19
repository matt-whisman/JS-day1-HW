def to_weird_case(string):
    return "".join(c.upper() if i % 2 == 0 else c for i, c in enumerate(string.lower()))


print(to_weird_case('String'))
print(to_weird_case('Weird string case'))
