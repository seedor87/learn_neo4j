from neo4j.v1 import GraphDatabase, basic_auth
from pprint import pprint

"""
Each Neo4j driver has a database object for creating a driver. To use a driver, follow this pattern:

  1) Ask the database object for a new driver.
  2) Ask the driver object for a new session.
  3) Use the session object to run statements. It returns an object representing the result.
  4) Process the result.
  5) Close the session.
"""

def make_create(**kwargs):
    return "CREATE (a:%(object)s {name:'%(name)s', title:'%(title)s'})" % kwargs

def make_match_on_attrbiute(**kwargs):
    return "MATCH (a:%(object)s) WHERE a.title = '%(title)s' RETURN a.name AS name, a.title as title" % kwargs

def make_relationship():
    return "MATCH (a:Person {name:'Bob'}), (r:Role {name:'GRA'}) CREATE (u)-[:HAS_ROLE]->(r)"

def make_match_on_relationship():
    return "MATCH (a {name: 'John'})-[:friend]->()-[:friend]->(fof) RETURN a.name, fof.name"

def run_query(query, session):
    return session.run(query)

def run_clear_db(session):
    return session.run("MATCH(n) OPTIONAL MATCH (n)-[r]-() DELETE n,r)")

def main():

    # Note this line will have the auth for your individual local db
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "tschebotarew"))
    session = driver.session()

    q = make_create(object='Person', name='Bob', title='King')
    r = run_query(q, session)

    q = make_create(object='Person', name='Eliakah', title='King')
    r = run_query(q, session)

    q = make_relationship()
    r = run_query(q, session)

    # q = make_match_on_attrbiute(object='Person', title='King')
    # r = run_query(q, session)
    # for record in r:
    #   print("{0} {1}".format(record["title"], record["name"]))

    session.close()

if __name__ == '__main__':

    try:
        main()
    except Exception as e:
        print str(e)