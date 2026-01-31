from neo4j import GraphDatabase
import csv

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "password")
)

def run():
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")

        with open("data/orders.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                session.run("""
                MERGE (c:Client {id:$cid})
                MERGE (o:Order {id:$oid})
                MERGE (p:Product {id:$pid})
                MERGE (c)-[:PLACED]->(o)
                MERGE (o)-[:CONTAINS]->(p)
                """, cid=row["client_id"], oid=row["order_id"], pid=row["product_id"])

if __name__ == "__main__":
    run()

