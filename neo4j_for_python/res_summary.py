from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "tschebotarew"))
session = driver.session()

result = session.run("PROFILE MATCH (p:Person {name: {name}}) "
                     "RETURN id(p)", {"name": "Arthur"})
summary = result.consume()
print(summary.statement_type)
print(summary.profile)

print "Notifs:"
for notification in summary.notifications:
    print(notification)