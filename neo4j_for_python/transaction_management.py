from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "tschebotarew"))
session = driver.session()

with session.begin_transaction() as tx:
    tx.run("CREATE (:Person {name: 'Merlin'})")
    tx.success = True