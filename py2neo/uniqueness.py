
from py2neo import Node, Relationship, Graph, watch, Path

watch("httpstream")

graph = Graph("http://neo4j:tschebotarew@localhost:7474/db/data/")

alice = graph.merge_one("Person", "email", "alice@example.com")
bob = graph.merge_one("Person", "email", "bob@email.net")
graph.create_unique(Relationship(alice, "KNOWS", bob))

carol = graph.merge_one("Person", "email", "carol@foo.us")
dave = graph.merge_one("Person", "email", "dave@dave.co.uk")
graph.create_unique(Path(alice, "KNOWS", bob, "KNOWS", carol, "KNOWS", dave))