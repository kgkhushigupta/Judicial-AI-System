"""
Similarity Search Module
Performs semantic similarity search on legal cases
"""

import logging
from typing import List, Dict, Optional
import numpy as np

logger = logging.getLogger(__name__)


class SimilaritySearch:
    """Perform semantic similarity search on judicial cases."""
    
    def __init__(self, embedder, faiss_index):
        """
        Initialize similarity search.
        
        Args:
            embedder: Case embedder instance
            faiss_index: FAISS index instance
        """
        self.embedder = embedder
        self.index = faiss_index
        self.case_database = {}
        logger.info("SimilaritySearch initialized")
    
    def index_case(self, case_id: str, case_text: str) -> bool:
        """
        Index a case for similarity search.
        
        Args:
            case_id: Unique case identifier
            case_text: Full or summary text of case
            
        Returns:
            True if successful
        """
        try:
            # Generate embedding
            embedding = self.embedder.embed_text(case_text)
            if embedding is None:
                return False
            
            # Add to FAISS index
            self.index.add_vectors(
                np.array([embedding]),
                ids=[case_id]
            )
            
            # Store metadata
            self.case_database[case_id] = {
                'text': case_text,
                'embedding': embedding
            }
            
            return True
        
        except Exception as e:
            logger.error(f"Error indexing case {case_id}: {str(e)}")
            return False
    
    def find_similar_cases(self, query_text: str, k: int = 5) -> List[Dict]:
        """
        Find similar cases to query text.
        
        Args:
            query_text: Query case text
            k: Number of similar cases to return
            
        Returns:
            List of similar cases with scores
        """
        try:
            # Generate query embedding
            query_embedding = self.embedder.embed_text(query_text)
            if query_embedding is None:
                return []
            
            # Search FAISS index
            distances, indices = self.index.search(query_embedding, k)
            
            results = []
            for distance, idx in zip(distances, indices):
                if idx >= 0:  # Valid result
                    results.append({
                        'distance': float(distance),
                        'similarity_score': 1.0 / (1.0 + distance),
                        'index_position': int(idx)
                    })
            
            logger.info(f"Found {len(results)} similar cases")
            return results
        
        except Exception as e:
            logger.error(f"Error searching similar cases: {str(e)}")
            return []


if __name__ == "__main__":
    # Usage example would go here
    pass
