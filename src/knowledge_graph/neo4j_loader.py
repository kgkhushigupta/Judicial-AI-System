"""
Neo4j Knowledge Graph Loader
Loads and manages judicial knowledge graph in Neo4j
"""

import logging
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


class Neo4jLoader:
    """Load and manage judicial knowledge graph in Neo4j."""
    
    def __init__(self, uri: str = "bolt://localhost:7687", 
                 username: str = "neo4j", password: str = "password"):
        """
        Initialize Neo4j connection.
        
        Args:
            uri: Neo4j server URI
            username: Database username
            password: Database password
        """
        self.uri = uri
        self.username = username
        self.driver = None
        self.session = None
        
        try:
            from neo4j import GraphDatabase
            self.driver = GraphDatabase.driver(uri, auth=(username, password))
            self.session = self.driver.session()
            logger.info(f"Connected to Neo4j at {uri}")
        except ImportError:
            logger.warning("neo4j-driver not installed")
        except Exception as e:
            logger.error(f"Error connecting to Neo4j: {str(e)}")
    
    def create_case_node(self, case_id: str, case_data: Dict) -> bool:
        """
        Create a case node in the graph.
        
        Args:
            case_id: Unique case identifier
            case_data: Dictionary of case properties
            
        Returns:
            True if successful
        """
        if self.session is None:
            return False
        
        try:
            query = """
            CREATE (c:Case {id: $case_id, title: $title, year: $year, 
                    court: $court, judgment: $judgment})
            """
            self.session.run(query, case_id=case_id, **case_data)
            logger.info(f"Created case node: {case_id}")
            return True
        
        except Exception as e:
            logger.error(f"Error creating case node: {str(e)}")
            return False
    
    def create_relationship(self, case_id1: str, case_id2: str, 
                           relationship_type: str) -> bool:
        """
        Create a relationship between two cases.
        
        Args:
            case_id1: First case ID
            case_id2: Second case ID
            relationship_type: Type of relationship
            
        Returns:
            True if successful
        """
        if self.session is None:
            return False
        
        try:
            query = f"""
            MATCH (c1:Case {{id: $case_id1}})
            MATCH (c2:Case {{id: $case_id2}})
            CREATE (c1)-[r:{relationship_type}]->(c2)
            """
            self.session.run(query, case_id1=case_id1, case_id2=case_id2)
            logger.info(f"Created {relationship_type} relationship")
            return True
        
        except Exception as e:
            logger.error(f"Error creating relationship: {str(e)}")
            return False
    
    def close(self):
        """Close Neo4j connection."""
        if self.session:
            self.session.close()
        if self.driver:
            self.driver.close()
            logger.info("Neo4j connection closed")


if __name__ == "__main__":
    loader = Neo4jLoader()
