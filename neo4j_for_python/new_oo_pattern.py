from neo4j.v1 import GraphDatabase, basic_auth

# driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "tschebotarew"))
# session = driver.session()

def make_(keyw, var, obj, **kwargs):
    "CREATE (a:%s {name:'%(name)s', title:'%(title)s'})"
    query = "%s (%s:%s " % (keyw, var, obj)
    if kwargs is not None:
        query = query + '{ '
        query = query + ', '.join([str("%s:'%s'") % (key, val) for key, val in kwargs.iteritems()])
        query = query + "})"
    else:
        query = query + ")"
    print query
    return query

def make_match(obj_a, obj_b, relationship, **kwargs):
    query = "MATCH" + make_(keyw='', var='a', obj=obj_a, name='Bob')
    query = query + ", " + make_(keyw='', var='b', obj=obj_b, name='Alex')
    query = query + "CREATE (a)-[:%s]->(b)" % (relationship)
    print query
    return query

def make_match_attr(obj, attribute, val, **kwargs):
    "MATCH (a:%(object)s) WHERE a.title = '%(title)s' RETURN a.name AS name, a.title as title"
    query = "MATCH" + make_(keyw='', var='a', obj=obj)
    query = query + "WHERE a.%s = '%s'" % (attribute, val)
    print query
    return query

def run_(query, session):
    return session.run(query)

def main():

    # Note this line will have the auth for your individual local db
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "tschebotarew"))
    session = driver.session()

    q = make_(keyw='CREATE', var= 'a', obj='Person', name='Bob', title='GRA')
    r = run_(q, session)

    q = make_(keyw='CREATE', var='b', obj='Person', name='Alex', title='Cosmetologist')
    r = run_(q, session)

    q = make_(keyw='MERGE', var='c', obj='Person', name='Eliakah', title='Programmer')
    r = run_(q, session)

    q = make_match(obj_a='Person', obj_b='Person', relationship='KNOWS', name='Bob')
    r = run_(q, session)

    q = make_match_attr(obj='Person', attribute='name', val='Bob')
    r = run_(q, session)
    print r

    session.close()

if __name__ == '__main__':

    try:
        main()
    except Exception as e:
        print str(e)

