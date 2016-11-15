from py2neo import Node, Graph, watch

watch("httpstream")

graph = Graph("http://neo4j:tschebotarew@localhost:7474/db/data/")

alice = Node("Person", name="Alice")
banana = Node("Fruit", "Food", colour="yellow", tasty=True)
print alice.labels

bob = Node.cast({"name": "Bob Robertson", "age": 44})

print graph.cypher.execute("CREATE (a:Person {name:{N}})", {"N": "Alice"})

person = graph.merge_one("Person", "email", "bob@example.com")
print person.properties
print person.properties['email']

print Node.cast("Person")
print Node.cast("Person", name="Alice")

alice.properties["name"] = "Ace"
print alice.properties['name']
