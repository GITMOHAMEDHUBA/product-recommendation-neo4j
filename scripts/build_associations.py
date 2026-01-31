from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "password")
)

query = """
MATCH (o:Order)-[:CONTAINS]->(p1:Product)
MATCH (o)-[:CONTAINS]->(p2:Product)
WHERE p1 <> p2
WITH p1, p2, count(*) AS freq
MERGE (p1)-[r:BOUGHT_WITH]->(p2)
SET r.count = freq
"""

with driver.session() as session:
    session.run(query)

