from py2neo import authenticate, Graph, watch

# set up authentication parameters
authenticate("camelot:7474", "neo4j", "tschebotarew")

# connect to authenticated graph database
graph = Graph("http://camelot:7474/db/data/")