print("\n==============================")
print("⚖ JUDICIAL AI SYSTEM DEMO")
print("==============================\n")

print("Initializing modules...\n")

# Import your modules
from src.prediction.outcome_model import OutcomePredictor
from src.bias_detection.bias_detector import BiasDetector
from src.explanation.reasoning_engine import ReasoningEngine
from src.knowledge_graph.neo4j_loader import Neo4jLoader


print("Prediction Model Loaded")
print("Bias Detection Module Loaded")
print("Reasoning Engine Loaded")
print("Knowledge Graph Loader Loaded\n")


# Initialize objects
predictor = OutcomePredictor()
bias_detector = BiasDetector()
reasoning_engine = ReasoningEngine()


print("Running Sample Case Analysis...\n")

# Fake features just for demo
import numpy as np

features = np.random.rand(10)

prediction = predictor.predict(features)

print("Prediction Result:")
print(prediction)

print("\nGenerating Explanation...\n")

explanation = reasoning_engine.explain_prediction(
    prediction,
    ["CASE_101", "CASE_102", "CASE_103"]
)

print(explanation)


print("\nRunning Bias Detection...\n")

cases = [
    {"region":"A","outcome":1},
    {"region":"B","outcome":0},
    {"region":"A","outcome":1}
]

bias_report = bias_detector.generate_bias_report(cases)

print("Bias Report:")
print(bias_report)


print("\nLoading Knowledge Graph...\n")

loader = Neo4jLoader()

case_data = {
    "title":"Fraud Case Example",
    "year":2023,
    "court":"Supreme Court",
    "judgment":"Conviction"
}

loader.create_case_node("CASE_201",case_data)
loader.create_case_node("CASE_202",case_data)
loader.create_relationship("CASE_201","CASE_202","SIMILAR_TO")

loader.close()

print("Knowledge Graph Updated\n")


print("==============================")
print("System Ready")
print("==============================")