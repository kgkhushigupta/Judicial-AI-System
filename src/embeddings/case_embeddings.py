"""
Case Embeddings Module
Generates BERT and other neural embeddings for legal cases
"""

import logging
import numpy as np
from typing import Optional, List

logger = logging.getLogger(__name__)


class CaseEmbedder:
    """Generate embeddings for legal cases using BERT and other models."""
    
    def __init__(self, model_name: str = 'bert-base-uncased'):
        """
        Initialize case embedder.
        
        Args:
            model_name: Pre-trained model name from HuggingFace
        """
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        
        try:
            from transformers import AutoTokenizer, AutoModel
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModel.from_pretrained(model_name)
            logger.info(f"Loaded model: {model_name}")
        except ImportError:
            logger.warning("transformers library not installed")
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
    
    def embed_text(self, text: str) -> Optional[np.ndarray]:
        """
        Generate embedding for a single text.
        
        Args:
            text: Input text (case summary or full text)
            
        Returns:
            Embedding vector or None if error
        """
        if self.model is None or self.tokenizer is None:
            logger.error("Model not initialized")
            return None
        
        try:
            import torch
            
            # Tokenize and generate embeddings
            inputs = self.tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
            
            with torch.no_grad():
                outputs = self.model(**inputs)
            
            # Use mean pooling over token embeddings
            embeddings = outputs.last_hidden_state.mean(dim=1).numpy()
            return embeddings[0]
        
        except Exception as e:
            logger.error(f"Error generating embedding: {str(e)}")
            return None
    
    def embed_batch(self, texts: List[str]) -> List[Optional[np.ndarray]]:
        """
        Generate embeddings for multiple texts.
        
        Args:
            texts: List of input texts
            
        Returns:
            List of embedding vectors
        """
        embeddings = [self.embed_text(text) for text in texts]
        logger.info(f"Generated {len(embeddings)} embeddings")
        return embeddings


if __name__ == "__main__":
    embedder = CaseEmbedder()
