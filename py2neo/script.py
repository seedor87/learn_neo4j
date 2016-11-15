
from py2neo import Node, Relationship

a = Node("Person", name="Alice")
b = Node("Person", name="Bob")
ab = Relationship(a, "KNOWS", b)
print ab

c = Node("Person", name="Carol")
class WorksWith(Relationship): pass
ac = WorksWith(a, c)
print ac.type()

w = ab + Relationship(b, "LIKES", c) + ac
print w