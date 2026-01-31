# Product Recommendation with Neo4j

Graph-based recommendation system for products frequently bought together.

## Stack
- Neo4j
- Python
- Docker

## Run
```bash
docker compose -f docker/docker-compose.yml up -d
python data/generate_data.py
python scripts/import_data.py
python scripts/build_associations.py
python scripts/recommend.py

