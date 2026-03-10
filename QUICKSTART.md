# Judicial AI System - Quick Start Guide

## Installation

```bash
# 1. Navigate to project directory
cd Judicial-AI-System

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Download NLP models
python -m spacy download en_core_web_sm
```

## Configuration

Edit `config/config.yaml` to customize:
- Data paths
- Model settings
- Database connections
- API parameters

## Running Components

### PDF Extraction
```python
from src.ingestion.pdf_extractor import PDFExtractor

extractor = PDFExtractor()
text = extractor.extract_text("path/to/case.pdf")
```

### Text Preprocessing
```python
from src.preprocessing.text_cleaning import TextCleaner

cleaner = TextCleaner()
cleaned = cleaner.clean_text(text)
```

### NLP Analysis
```python
from src.nlp.entity_extractor import EntityExtractor
from src.nlp.keyword_extractor import KeywordExtractor

extractor = EntityExtractor()
entities = extractor.extract_all_entities(text)

kw_extractor = KeywordExtractor()
keywords = kw_extractor.extract_keywords(text)
```

### Similarity Search
```python
from src.embeddings.case_embeddings import CaseEmbedder
from src.similarity.similarity_search import SimilaritySearch

embedder = CaseEmbedder()
search = SimilaritySearch(embedder, faiss_index)
similar = search.find_similar_cases(query_text, k=5)
```

### Dashboard
```bash
streamlit run dashboard/app.py
```

Open browser to: http://localhost:8501

## Project Structure

- **data/**: Input documents and generated data
- **src/**: Core Python modules
- **dashboard/**: Streamlit web interface
- **notebooks/**: Jupyter notebooks for experiments
- **config/**: Configuration files
- **models/**: Trained ML models
- **logs/**: Application logs

## Key Features

✅ PDF extraction with Apache Tika  
✅ Distributed text preprocessing with Spark  
✅ Advanced NLP (sections, entities, keywords)  
✅ BERT-based embeddings  
✅ FAISS vector similarity search  
✅ Neo4j knowledge graph integration  
✅ ML-based case outcome prediction  
✅ Bias detection and analysis  
✅ Explainable AI reasoning engine  
✅ Interactive web dashboard  

## Documentation

See [README.md](README.md) for comprehensive documentation.
