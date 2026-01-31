
import random
import csv

products = [
    ("P1", "Laptop", "Tech"),
    ("P2", "Mouse", "Tech"),
    ("P3", "Keyboard", "Tech"),
    ("P4", "Headphones", "Tech"),
    ("P5", "Bag", "Accessories"),
    ("P6", "Charger", "Accessories"),
]

with open("orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["order_id", "client_id", "product_id"])
    for order_id in range(1, 501):
        client_id = random.randint(1, 100)
        bought = random.sample(products, random.randint(1, 4))
        for p in bought:
            writer.writerow([order_id, client_id, p[0]])
