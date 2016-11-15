
from py2neo import Node, Relationship, Graph, watch

watch("httpstream")

graph = Graph("http://neo4j:tschebotarew@localhost:7474/db/data/")

# for record in graph.cypher.execute("CREATE (d:Person {name:'Dave'}) RETURN d"):
#     print(record)

# tx = graph.cypher.begin()
# statement = "MATCH (a {name:{A}}), (b {name:{B}}) CREATE (a)-[:KNOWS]->(b)"
# for person_a, person_b in [("Alice", "Bob"), ("Bob", "Dave"), ("Alice", "Carol")]:
#      tx.append(statement, {"A": person_a, "B": person_b})
# print statement
# tx.commit()

statement = "MERGE (n:Person {name:{N}}) RETURN n"

tx = graph.cypher.begin()

def add_names(*names):
    for name in names:
        tx.append(statement, {"N": name})
    tx.process()

add_names("Homer", "Marge", "Bart", "Lisa", "Maggie")
add_names("Peter", "Lois", "Chris", "Meg", "Stewie")

print tx.commit()

for record in graph.cypher.stream("MATCH (n) RETURN n LIMIT 10"):
    print record[0]
