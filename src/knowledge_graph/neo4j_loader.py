"""
Neo4j Knowledge Graph Loader
Loads and manages judicial knowledge graph in Neo4j
"""

import logging
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


class Neo4jLoader:
    """Load and manage judicial knowledge graph in Neo4j."""
    
    def __init__(self, uri="bolt://localhost:7687", username="neo4j", password="password"):

        self.uri = uri
        self.username = username
        self.driver = None

        try:
            from neo4j import GraphDatabase
            self.driver = GraphDatabase.driver(uri, auth=(username, password))
            logger.info(f"Connected to Neo4j at {uri}")
        except ImportError:
            logger.warning("neo4j-driver not installed")
        except Exception as e:
            logger.error(f"Error connecting to Neo4j: {str(e)}")
    
    def create_case_node(self, case_id: str, case_data: Dict) -> bool:

        if self.driver is None:
            return False

        try:
            query = """
            MERGE (c:Case {id:$case_id})
            SET c.title=$title,
                c.year=$year,
                c.court=$court,
                c.judgment=$judgment
            """

            with self.driver.session() as session:
                session.run(query, case_id=case_id, **case_data)

            logger.info(f"Created case node: {case_id}")
            return True

        except Exception as e:
            logger.error(f"Error creating case node: {str(e)}")
            return False
    
    def create_relationship(self, case_id1: str, case_id2: str, relationship_type: str) -> bool:

        if self.driver is None:
            return False

        try:
            query = """
            MATCH (c1:Case {id:$case_id1})
            MATCH (c2:Case {id:$case_id2})
            MERGE (c1)-[:SIMILAR_TO]->(c2)
            """

            with self.driver.session() as session:
                session.run(query, case_id1=case_id1, case_id2=case_id2)

            logger.info("Created SIMILAR_TO relationship")
            return True

        except Exception as e:
            logger.error(f"Error creating relationship: {str(e)}")
            return False
    
    def close(self):
        """Close Neo4j connection."""
        if self.driver:
            self.driver.close()
            logger.info("Neo4j connection closed")


if __name__ == "__main__":

    print("Testing Neo4j Knowledge Graph Loader...\n")

    loader = Neo4jLoader(
        uri="bolt://localhost:7687",
        username="neo4j",
        password="password"
    )

    case_data = {
        "title": "Fraud Case Example",
        "year": 2023,
        "court": "Supreme Court",
        "judgment": "Conviction"
    }

    loader.create_case_node("CASE_101", case_data)
    loader.create_case_node("CASE_102", case_data)

    loader.create_relationship(
        "CASE_101",
        "CASE_102",
        "SIMILAR_TO"
    )

    print("Graph nodes and relationship created.")

    loader.close()