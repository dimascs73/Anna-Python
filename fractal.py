def defractalize(func):
    for i in func:
        if i == func:
            func.remove(func)
    return func


fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
fractal.append(9)
defractalize(fractal)
print(fractal)
