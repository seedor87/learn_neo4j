from py2neo import Node, Relationship, walk

# WORKS ONLY IN v3.0 AND UP
class WorksWith(Relationship): pass
class Likes(Relationship): pass

print
a = Node("Person", name="Alice")
b = Node("Person", name="Bob")
print a.labels()
print b.labels()
print 'Name:', a['name']

print
""" NOTES
class Relationship(start_node, type, end_node, **properties)
class Relationship(start_node, end_node, **properties)
class Relationship(node, type, **properties)
class Relationship(node, **properties)
"""
ab = Relationship(a, "KNOWS", b)
ba = Relationship(b, "KNOWS", a)
print 'ab', ab
print 'ba', ba
print hash(ab), hash(ba)

print
c = Node("Person", name="Carol")
ac = WorksWith(a, c, since=2000)
print ac.type()
print ac == ac

print
for op in ['|', '-', '^']: # += '&' is for intersection
    S = eval('ab %s ac' % (op))
    print S
    print S.keys()
    print S.relationships()
    print S.labels()
    print S.nodes()
    print S.types()

print
w = ab + Likes(b, c) + ac + ba
print 'W:', w
print 'Nodes:', w.nodes()
print 'name:', w.start_node()['name']
print 'realtions:'
for rel in w.relationships():
    print "\t", rel, rel['since']

print
wlk = walk(w)
nodes = set()
rels = set()
for x in wlk:
    if isinstance(x, Node):
        nodes.add(x)
    else: # is instance Relationship
        rels.add(x)
print rels
print nodes
