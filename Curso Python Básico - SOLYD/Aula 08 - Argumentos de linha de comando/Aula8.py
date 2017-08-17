import sys

# arg1 method
# arg2 valor 1
# arg3 valor 2
arg = sys.argv


def soma(a, b):
    return a + b


def sub(a, b):
    return a - b

if arg[1] == "soma":
    resp = soma(float(arg[2]), float(arg[3]))
elif arg[1] == "sub":
    resp = sub(float(arg[2]), float(arg[3]))

print(resp)
