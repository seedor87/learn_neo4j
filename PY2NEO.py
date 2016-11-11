from py2neo import Graph, Path, ServiceRoot
graph = Graph("http://neo4j:tschebotarew@localhost:7474/db/data/")
# graph = ServiceRoot("http://neo4j:tschebotarew@localhost:7474")

tx = graph.cypher.begin()
for name in ["Alice", "Bob", "Carol"]:
    tx.append("CREATE (person:Person {name:{name}}) RETURN person", name=name)
alice, bob, carol = [result.one for result in tx.commit()]

friends = Path(alice, "KNOWS", bob, "KNOWS", carol)
graph.create(friends)