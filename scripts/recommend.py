from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "password")
)

def recommend(product_id):
    query = """
    MATCH (p:Product {id:$pid})-[r:BOUGHT_WITH]->(rec:Product)
    RETURN rec.id, r.count
    ORDER BY r.count DESC
    LIMIT 5
    """
    with driver.session() as session:
        return session.run(query, pid=product_id).data()

print(recommend("P1"))

