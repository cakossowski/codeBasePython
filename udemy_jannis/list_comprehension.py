xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
Ohne List comprehension würde der Code um die Quadratzahlen in ys einzupflegen so aussehen:

ys = []
for x in xs:
ys.append(x * x)

"""

# List comprehension verkürzt das deutlich:
ys = [ x * x for x in xs]

"""
zuerst die Operation die durchgeführt werden soll, dann die loop durch die iteriert werden soll
"""

print(xs)
print(ys)


students = ['Max', 'Monika', 'Erik', 'Franziska']
lengths = [len(student) for student in students]

print(lengths)
