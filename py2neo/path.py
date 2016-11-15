from py2neo import Node, Path, Relationship, Rel, Rev

path = Path(Node(name="A"), Rel("TO"), Node(name="B"), Rev("TO"), Node(name="C"))
for relationship in path.relationships:
    print(relationship)

alice, bob, carol = Node(name="Alice"), Node(name="Bob"), Node(name="Carol")
abc = Path(alice, "KNOWS", bob, Rev("KNOWS"), carol)
print abc
print abc.nodes
print abc.rels

dave, eve = Node(name="Dave"), Node(name="Eve")
de = Path(dave, "KNOWS", eve)
print de

abcde = Path(abc, "KNOWS", de)
print abcde

for relationship in abcde.relationships:
    print(relationship)