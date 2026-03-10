"""
Outcome Prediction Model
Predicts legal case outcomes using machine learning
"""

import logging
import numpy as np
from typing import Dict, Optional, List

logger = logging.getLogger(__name__)


class OutcomePredictor:
    """Predict case outcomes using trained machine learning models."""
    
    def __init__(self, model_path: Optional[str] = None):
        """
        Initialize outcome predictor.
        
        Args:
            model_path: Path to trained model file
        """
        self.model = None
        self.model_path = model_path
        self.feature_names = []
        
        if model_path:
            self.load_model(model_path)
        
        logger.info("OutcomePredictor initialized")
    
    def train_model(self, X_train: np.ndarray, y_train: np.ndarray) -> bool:
        """
        Train outcome prediction model.
        
        Args:
            X_train: Training features
            y_train: Training labels
            
        Returns:
            True if training successful
        """
        try:
            from sklearn.ensemble import RandomForestClassifier
            
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
            self.model.fit(X_train, y_train)
            
            logger.info("Model trained successfully")
            return True
        
        except Exception as e:
            logger.error(f"Error training model: {str(e)}")
            return False
    
    def predict(self, features: np.ndarray) -> Dict:
        """
        Predict case outcome.
        
        Args:
            features: Case features
            
        Returns:
            Prediction results with confidence
        """
        if self.model is None:
            logger.error("Model not trained or loaded")
            return {}
        
        try:
            prediction = self.model.predict([features])[0]
            probabilities = self.model.predict_proba([features])[0]
            
            return {
                'outcome': prediction,
                'probabilities': probabilities,
                'confidence': float(np.max(probabilities))
            }
        
        except Exception as e:
            logger.error(f"Error predicting outcome: {str(e)}")
            return {}
    
    def batch_predict(self, features_list: List[np.ndarray]) -> List[Dict]:
        """
        Predict outcomes for multiple cases.
        
        Args:
            features_list: List of case features
            
        Returns:
            List of prediction results
        """
        predictions = [self.predict(features) for features in features_list]
        logger.info(f"Made {len(predictions)} predictions")
        return predictions
    
    def save_model(self, filepath: str) -> bool:
        """Save trained model."""
        try:
            import pickle
            with open(filepath, 'wb') as f:
                pickle.dump(self.model, f)
            logger.info(f"Model saved to {filepath}")
            return True
        except Exception as e:
            logger.error(f"Error saving model: {str(e)}")
            return False
    
    def load_model(self, filepath: str) -> bool:
        """Load trained model."""
        try:
            import pickle
            with open(filepath, 'rb') as f:
                self.model = pickle.load(f)
            logger.info(f"Model loaded from {filepath}")
            return True
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            return False


if __name__ == "__main__":
    predictor = OutcomePredictor()
