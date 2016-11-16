from py2neo import Node, Relationship, Graph, watch
from functools import wraps
watch("httpstream")

graph = Graph("http://neo4j:tschebotarew@localhost:7474/db/data/")

def print_deco(func, *args, **kwargs):
    result = func(*args, **kwargs)
    print result
    return result

def main():
    alice = Node("Person", name="Alice")
    print alice
    bob = Node("Person", name="Bob")
    print bob
    alice_knows_bob = Relationship(alice, "KNOWS", bob)
    print alice_knows_bob
    graph.create(alice_knows_bob)

    alice.properties["age"] = 33
    bob.properties["age"] = 44
    alice.push()
    bob.push()

    tx = graph.cypher.begin()
    print tx.append('Match (n) return n')
    print tx.commit()

def clear(a=0, b=0):
    return True, a, b

if __name__ == '__main__':
    label = 'label'
    age = 22
    print_deco(Node, 'label', age=22)

    n = Node('label', age=22)
    print n

