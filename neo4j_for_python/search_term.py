from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "tschebotarew"))
session = driver.session()

result = session.run("MATCH (knight:Person:Knight) WHERE knight.castle = {castle} "
                     "RETURN knight.name AS name", {"castle": "Camelot"})
retained_result = list(result)
session.close()
for record in retained_result:
    print("%s is a knight of Camelot" % record["name"])