# Judicial AI System

An advanced AI-powered system for analyzing court judgments, predicting case outcomes, detecting biases, and generating explainable insights.

## 🎯 Features

- **PDF Document Ingestion**: Extract text from court judgment PDFs using Apache Tika
- **Text Processing**: Clean, normalize, and preprocess legal documents at scale using Spark
- **NLP Analysis**: 
  - Detect and extract document sections (facts, issues, reasoning, etc.)
  - Extract named entities (judges, parties, laws)
  - Identify and cluster keywords
- **Semantic Search**: Find similar cases using FAISS vector similarity search with BERT embeddings
- **Knowledge Graph**: Build and query relationships between cases using Neo4j
- **Case Outcome Prediction**: Machine learning models to predict case outcomes
- **Bias Detection**: Identify demographic, temporal, and procedural biases
- **Explainable AI**: Generate human-readable explanations for predictions
- **Dashboard**: Interactive Streamlit dashboard for case analysis and exploration

## 📁 Project Structure

```
Judicial-AI-System/
├── data/
│   ├── raw_pdfs/              # Original court judgment PDFs
│   ├── extracted_text/        # Text extracted from PDFs
│   ├── processed_cases/       # Cleaned case data
│   ├── embeddings/            # BERT embeddings
│   └── faiss_index/           # Vector search index
├── src/
│   ├── ingestion/             # PDF extraction
│   ├── preprocessing/         # Text cleaning and Spark processing
│   ├── nlp/                   # NLP tasks (sections, entities, keywords)
│   ├── clustering/            # Case clustering
│   ├── embeddings/            # Case embeddings
│   ├── similarity/            # Similarity search
│   ├── knowledge_graph/       # Neo4j integration
│   ├── prediction/            # Outcome prediction
│   ├── bias_detection/        # Bias analysis
│   └── explanation/           # Explainable AI
├── dashboard/                 # Streamlit web interface
├── notebooks/                 # Jupyter notebooks for experiments
├── config/                    # Configuration files
├── models/trained_models/     # Trained ML models
├── logs/pipeline_logs/        # Application logs
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Apache Tika server (for PDF extraction)
- Neo4j database (for knowledge graph)
- FAISS (for similarity search)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Judicial-AI-System
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download spaCy model:
```bash
python -m spacy download en_core_web_sm
```

### Configuration

Edit `config/config.yaml` to set up:
- PDF extraction paths
- Neo4j connection details
- FAISS index settings
- ML model parameters
- Logging configuration

### Running the Dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard will be available at `http://localhost:8501`

## 📊 Workflow

1. **Data Ingestion**: Place PDFs in `data/raw_pdfs/`
2. **Text Extraction**: Run PDF extraction pipeline
3. **Preprocessing**: Clean and normalize text
4. **NLP Analysis**: Extract sections, entities, and keywords
5. **Embedding Generation**: Create BERT embeddings
6. **Indexing**: Build FAISS index for similarity search
7. **Knowledge Graph**: Load case relationships into Neo4j
8. **Analysis**: Run prediction, bias detection, and similarity search
9. **Visualization**: Explore results in dashboard

## 🔍 Main Modules

### Ingestion (`src/ingestion/`)
- `pdf_extractor.py`: Extract text from PDF documents

### Preprocessing (`src/preprocessing/`)
- `spark_preprocessing.py`: Distributed text processing
- `text_cleaning.py`: Text normalization and cleaning

### NLP (`src/nlp/`)
- `section_detector.py`: Identify document sections
- `entity_extractor.py`: Extract entities (persons, laws, dates)
- `keyword_extractor.py`: Extract important keywords

### Similarity & Embeddings
- `embeddings/case_embeddings.py`: Generate BERT embeddings
- `similarity/faiss_index.py`: Vector index management
- `similarity/similarity_search.py`: Semantic similarity search

### Analytics
- `prediction/outcome_model.py`: Case outcome prediction
- `bias_detection/bias_detector.py`: Detect biases
- `explanation/reasoning_engine.py`: Generate explanations

### Knowledge Graph
- `knowledge_graph/neo4j_loader.py`: Load data to Neo4j
- `knowledge_graph/graph_queries.py`: Query the graph

## 🛠️ Technology Stack

- **Data Processing**: Pandas, PySpark, Apache Tika
- **NLP**: Transformers, spaCy, BERT
- **Machine Learning**: scikit-learn, PyTorch
- **Vector Search**: FAISS
- **Graph Database**: Neo4j
- **Web Framework**: FastAPI, Streamlit
- **Data Management**: Python, YAML

## 📝 Example Usage

```python
from src.ingestion.pdf_extractor import PDFExtractor
from src.preprocessing.text_cleaning import TextCleaner
from src.embeddings.case_embeddings import CaseEmbedder
from src.similarity.similarity_search import SimilaritySearch

# Extract PDF
extractor = PDFExtractor()
text = extractor.extract_text("case.pdf")

# Clean text
cleaner = TextCleaner()
cleaned_text = cleaner.clean_text(text)

# Generate embedding
embedder = CaseEmbedder()
embedding = embedder.embed_text(cleaned_text)

# Search similar cases
search = SimilaritySearch(embedder, faiss_index)
similar_cases = search.find_similar_cases(cleaned_text, k=5)
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## ⚠️ Ethical Considerations

This system is designed to support judicial analysis and should be used responsibly:

- Results should be reviewed by legal professionals
- Bias detection is not a replacement for legal oversight
- Predictions should inform, not replace, human judgment
- Transparency and explainability are paramount


## 🙏 Acknowledgments

- Built with BERT embeddings from Hugging Face
- Vector search powered by Facebook FAISS
- Graph capabilities via Neo4j
- Web interface using Streamlit
