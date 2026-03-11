# Judicial AI System

**AI-Powered Legal Case Intelligence Platform**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Neo4j](https://img.shields.io/badge/Neo4j-5.0+-brightgreen.svg)](https://neo4j.com/)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Workflow](#workflow)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Goals & Roadmap](#goals--roadmap)

---

## Overview







The Judicial AI System is an intelligent platform designed to assist legal professionals by using AI, machine learning, and knowledge graphs to analyze legal cases. It demonstrates how AI can support the judicial decision process and accelerate legal research workflows.

---

## Features

- **Retrieve Similar Legal Cases** - Identify precedent cases with similar patterns using FAISS
- **Predict Case Outcomes** - Forecast judicial decisions using machine learning models
- **Generate Explainable Reasoning** - Provide transparent, interpretable AI explanations
- **Detect Bias in Decisions** - Identify potential demographic, regional, and procedural bias patterns
- **Visualize Legal Relationships** - Store and query case relationships in an interactive knowledge graph

---

## System Architecture

The system processes legal cases through a multi-stage pipeline:

```
Case Input
    ↓
NLP Embeddings (Text to Vectors)
    ↓
Similarity Search (FAISS)
    ↓
Outcome Prediction (Random Forest)
    ↓
Bias Detection Analysis
    ↓
Explainable AI Reasoning
    ↓
Knowledge Graph (Neo4j)
    ↓
Dashboard UI
```

---

## Workflow

### Stage 1: Case Input
Users submit legal case descriptions including:
- Legal arguments and evidence details
- Court jurisdiction and parties involved
- Case background and relevant precedents

### Stage 2: NLP Case Embedding
Legal text is converted into numerical vectors for semantic analysis.

**Tools:** Python, NumPy, Advanced NLP techniques
**Module:** `src/embeddings/case_embeddings.py`

### Stage 3: Similar Case Retrieval
The system locates previous cases with comparable patterns using FAISS (Facebook AI Similarity Search).

**Why FAISS?**
- Extremely fast similarity search across large datasets
- Scalable architecture for enterprise legal databases
- Efficient vector-based semantic matching

**Modules:**
- `src/similarity/faiss_index.py`
- `src/similarity/similarity_search.py`

**Example Results:**


| Case ID | Court | Year | Similarity |
|---------|-------|------|------------|
| TX-2022-991A | Superior Court, Austin | 2022 | 94% |
| FL-2019-382C | District Court, Miami | 2019 | 89% |
| NY-2024-011X | Supreme Court, Albany | 2024 | 81% |

### Stage 4: Outcome Prediction
Predicts likely verdicts based on historical case patterns using Random Forest classification.

**Algorithm:** Random Forest Classifier
**Advantages:**
- Handles complex legal patterns and non-linear relationships
- Robust to noisy and incomplete data
- Provides feature importance for interpretability

**Module:** `src/prediction/outcome_model.py`

**Example Output:**
```
Predicted Verdict: Guilty
Confidence Score: 88%
Legal Risk Level: Moderate
```

### Stage 5: Bias Detection
Analyzes judicial decisions to identify systemic bias patterns in case outcomes.

**Types of Bias Detected:**
- Demographic bias (gender, age, race)
- Regional bias (geographic disparities)
- Temporal bias (historical trends)
- Procedural bias (case handling variations)

**Module:** `src/bias_detection/bias_detector.py`

**Example Analysis:**


| Bias Type | Detection Score |
|-----------|-----------------|
| Regional Bias | 12% |
| Gender Bias | 4% |
| Court Bias | 48% |

### Stage 6: Explainable AI (Reasoning Engine)
Generates clear, interpretable explanations for all predictions rather than black-box outputs.

**Example Explanation:**
> The predicted outcome is **Guilty** because similar precedent cases TX-2022-991A and FL-2019-382C involved breach of warranty violations with comparable evidence strength.

**Module:** `src/explanation/reasoning_engine.py`

### Stage 7: Knowledge Graph (Neo4j)
Stores legal case relationships and facts in a queryable graph database for pattern discovery.

**Relationship Types:**
- `SIMILAR_TO` - Cases with comparable legal issues
- `DECIDED_IN` - Court and jurisdiction associations
- `CITES` - Precedent relationships
- `INVOLVES` - Party and legal subject matter connections

**Example Query:**
```cypher
MATCH (a:Case)-[r:SIMILAR_TO]->(b:Case)
WHERE a.caseId = 'TX-2022-991A'
RETURN a, r, b
LIMIT 10
```

**Module:** `src/knowledge_graph/neo4j_loader.py`

### Stage 8: Dashboard Interface
User-facing web interface for case analysis and visualization.

**Features:**
- Case input form and management
- Similarity results table with filtering
- Outcome prediction display with confidence scores
- Bias analysis dashboard with visualizations
- Explainable reasoning display
- Knowledge graph visualization

**Technologies:**
- HTML - Semantic markup
- TailwindCSS - Modern responsive styling
- JavaScript - Interactive components

**File:** `code.html`

---

## Technologies

| Category | Tools |
|----------|-------|
| Programming | Python 3.8+ |
| Machine Learning | Scikit-learn, Random Forest |
| Numerical Computing | NumPy, Pandas |
| Similarity Search | FAISS (Facebook AI) |
| Graph Database | Neo4j 5.0+ |
| Backend Framework | Flask |
| Frontend | HTML5, TailwindCSS, JavaScript |

---

## Project Structure

```
Judicial-AI-System/
├── src/
│   ├── embeddings/
│   │   └── case_embeddings.py
│   ├── similarity/
│   │   ├── faiss_index.py
│   │   └── similarity_search.py
│   ├── prediction/
│   │   └── outcome_model.py
│   ├── bias_detection/
│   │   └── bias_detector.py
│   ├── explanation/
│   │   └── reasoning_engine.py
│   ├── knowledge_graph/
│   │   ├── neo4j_loader.py
│   │   ├── graph_queries.py
│   │   └── load_dataset_to_neo4j.py
│   ├── nlp/
│   │   ├── entity_extractor.py
│   │   ├── keyword_extractor.py
│   │   └── section_detector.py
│   ├── clustering/
│   │   └── keyword_clustering.py
│   ├── preprocessing/
│   │   ├── text_cleaning.py
│   │   ├── spark_preprocessing.py
│   │   └── test_cleaning.py
│   ├── ingestion/
│   │   └── pdf_extractor.py
│   └── run_pipeline.py
├── dashboard/
│   └── app.py
├── data/
│   └── legal_dataset.csv
├── config/
│   └── config.yaml
├── code.html
├── run_demo.py
├── requirements.txt
├── QUICKSTART.md
└── README.md
```

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Neo4j 5.0 or higher
- pip package manager

### Setup Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Judicial-AI-System
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Neo4j connection:
   - Edit `config/config.yaml`
   - Set your Neo4j server URI, username, and password

4. Load initial dataset:
   ```bash
   python src/knowledge_graph/load_dataset_to_neo4j.py
   ```

---

## Usage

### Run the Complete Demo

Execute the full pipeline:
```bash
python run_demo.py
```

This will:
- Initialize all AI modules
- Process sample legal cases
- Generate outcome predictions
- Perform bias detection analysis
- Populate the knowledge graph
- Display results in console

### Launch the Dashboard

Open the web interface:
```bash
# Simply open in your browser
code.html
```

Or serve with a local server:
```bash
python -m http.server 8000
```

Then navigate to `http://localhost:8000/code.html`

### Run Individual Components

```bash
# Text processing
python -m src.nlp.entity_extractor

# Similarity search
python -m src.similarity.similarity_search

# Knowledge graph queries
python -m src.knowledge_graph.graph_queries
```

---

## Goals & Roadmap

### Current Objectives
- Accelerate legal research and case discovery
- Identify relevant precedent cases efficiently
- Predict judicial outcomes with interpretability
- Improve transparency through explainable AI
- Detect and highlight systemic bias in judicial decisions

### Future Enhancements
- Legal-BERT embeddings for domain-specific NLP improvements
- Deep learning models (LSTM, Transformers) for prediction
- Full backend-frontend integration with real-time updates
- Neo4j graph visualization with interactive exploration
- Support for large-scale legal datasets (millions of cases)
- Multi-language support for international legal systems
- Integration with legal document scanning and OCR

---

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please open an issue on the project repository.
