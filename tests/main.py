import config_interview as ci

values = [
    ci.Int("A", docstr="Enter value of the coefficient of X square", default=0),
    ci.List("B", default=[]),
    ci.Int("C", default=0, validator=ci.MinMaxValidator(3, 4, float))
]

builder = ci.Builder(values)
if builder.interview():
    a = builder.to_json()
    print(a)
else:
    print("configuration interview was not finished")
