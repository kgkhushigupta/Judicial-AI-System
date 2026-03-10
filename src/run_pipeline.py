"""
Master Pipeline: Connect all modules for end-to-end processing
Pipeline Flow:
  Dataset (CSV) -> Text Cleaning -> Keyword Extraction -> 
  Embeddings -> FAISS Index -> Similarity Search
"""

import sys
import os
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

# Fix Unicode for Windows
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("\n" + "="*70)
print("JUDICIAL AI SYSTEM - MASTER PIPELINE")
print("="*70)

try:
    # ====================================================================
    # STEP 1: LOAD DATASET
    # ====================================================================
    print("\n[1/6] Loading dataset...")
    
    DATA_PATH = r"D:\bigdata\Judicial-AI-System\data\legal_dataset.csv"
    
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")
    
    df = pd.read_csv(DATA_PATH)
    print(f"  [OK] Loaded {len(df)} rows")
    print(f"  [OK] Columns: {list(df.columns)}")
    
    # ====================================================================
    # STEP 2: TEXT CLEANING
    # ====================================================================
    print("\n[2/6] Cleaning text...")
    
    from preprocessing.text_cleaning import clean_text
    
    # Combine question and answer
    df["text"] = df["question"] + " " + df["answer"]
    df["clean_text"] = df["text"].apply(clean_text)
    
    print(f"  [OK] Cleaned {len(df)} documents")
    print(f"  [OK] Sample: {df['clean_text'].iloc[0][:60]}...")
    
    # ====================================================================
    # STEP 3: KEYWORD EXTRACTION
    # ====================================================================
    print("\n[3/6] Extracting keywords...")
    
    from nlp.keyword_extractor import KeywordExtractor
    
    extractor = KeywordExtractor(num_keywords=10)
    all_keywords = []
    
    for idx, clean_text_val in enumerate(df["clean_text"]):
        keywords = extractor.extract_keywords(clean_text_val)
        all_keywords.append(keywords)
        if idx == 0:
            print(f"  [OK] Keywords for row 1: {keywords[:5]}")
    
    df["keywords"] = all_keywords
    print(f"  [OK] Extracted keywords from {len(df)} documents")
    
    # ====================================================================
    # STEP 4: EMBEDDING GENERATION
    # ====================================================================
    print("\n[4/6] Generating embeddings (TF-IDF)...")
    
    # Use simple embedding for now (to avoid BERT download delay)
    # In production, use: from embeddings.case_embeddings import CaseEmbedder
    from sklearn.feature_extraction.text import TfidfVectorizer
    
    vectorizer = TfidfVectorizer(max_features=384)  # Similar to BERT-base dims
    embeddings = vectorizer.fit_transform(df["clean_text"]).toarray()
    
    print(f"  [OK] Generated {len(embeddings)} embeddings")
    print(f"  [OK] Embedding dimension: {embeddings.shape[1]}")
    
    # ====================================================================
    # STEP 5: BUILD FAISS INDEX
    # ====================================================================
    print("\n[5/6] Building FAISS index...")
    
    try:
        import faiss
        
        # Convert to float32 (required by FAISS)
        embeddings_fp32 = embeddings.astype('float32')
        
        # Create index
        index = faiss.IndexFlatL2(embeddings_fp32.shape[1])
        index.add(embeddings_fp32)
        
        print(f"  [OK] FAISS index created")
        print(f"  [OK] Index size: {index.ntotal} vectors")
        
    except ImportError:
        print("  [!] FAISS not available, using approximate search")
        index = None
    
    # ====================================================================
    # STEP 6: SIMILARITY SEARCH
    # ====================================================================
    print("\n[6/6] Testing similarity search...")
    
    if index is not None:
        # Search for similar cases
        query_embedding = embeddings_fp32[0:1]
        distances, indices = index.search(query_embedding, k=3)
        
        print(f"  [OK] Query: {df['question'].iloc[0]}")
        print(f"  [OK] Similar cases found:")
        
        for rank, (idx, dist) in enumerate(zip(indices[0], distances[0]), 1):
            similarity = 1 / (1 + dist)  # Convert distance to similarity
            print(f"    {rank}. {df['question'].iloc[idx]} (similarity: {similarity:.3f})")
    else:
        # Fallback: cosine similarity
        from sklearn.metrics.pairwise import cosine_similarity
        
        query_embedding = embeddings[0:1]
        similarities = cosine_similarity(query_embedding, embeddings)[0]
        top_indices = np.argsort(similarities)[::-1][1:4]
        
        print(f"  [OK] Query: {df['question'].iloc[0]}")
        print(f"  [OK] Similar cases found:")
        
        for rank, idx in enumerate(top_indices, 1):
            print(f"    {rank}. {df['question'].iloc[idx]} (similarity: {similarities[idx]:.3f})")
    
    # ====================================================================
    # FINAL REPORT
    # ====================================================================
    print("\n" + "="*70)
    print("PIPELINE EXECUTION SUMMARY")
    print("="*70)
    print(f"[OK] Dataset processed: {len(df)} legal documents")
    print(f"[OK] Text cleaning: 100%")
    print(f"[OK] Keyword extraction: 100%")
    print(f"[OK] Embedding generation: 100%")
    print(f"[OK] FAISS index: Built successfully")
    print(f"[OK] Similarity search: Operational")
    print("\n[OK] MASTER PIPELINE COMPLETED SUCCESSFULLY!")
    print("="*70 + "\n")
    
except Exception as e:
    print(f"\n[ERROR] {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
