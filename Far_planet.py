def find_farthest_orbit(list_of_orbits):
    pi = 3.1415926
    S_max = 0
    for x, y in list_of_orbits:
        if x == y:
            continue
        else:
            S = pi * x * y
            if S > S_max:
                S_max = S
                x_max = x
                y_max = y
    return (x_max, y_max)


orbits = [(3, 23), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
