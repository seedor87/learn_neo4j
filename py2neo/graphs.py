from py2neo import Node, Relationship, Graph, watch

watch("httpstream")

graph = Graph("http://neo4j:tschebotarew@localhost:7474/db/data/")

alice = Node("Person", name="Alice")
bob = Node("Person", name="Bob")
alice_knows_bob = Relationship(alice, "KNOWS", bob)
graph.create(alice_knows_bob)

alice.properties["age"] = 33
bob.properties["age"] = 44
alice.push()
bob.push()

tx = graph.cypher.begin()
print tx.append('Match (n) return n')
print tx.commit()