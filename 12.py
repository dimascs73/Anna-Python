base = ('Ivan', 12, 'jan'), ('Peter', 22, 'mar'), ('Petir', 25, 'mar'), ('Olla', 7, 'jan')


di_ct = {name: {month: (name, date)} for name, date, month in base}

print(di_ct)