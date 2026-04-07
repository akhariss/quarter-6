# Natural Language Processing (NLP)

**Praktikum NLP - Semester 6**

---

## 📚 Deskripsi

Mata kuliah ini membahas teknik pemrosesan bahasa alami menggunakan Python. Fokus pada analisis teks, sentiment analysis, dan implementasi NLP pipelines.

---

## 📁 Struktur Folder

```
NLP/
├── nlp mandiri/                # NLP Mandiri Practicum
│   ├── abdulkharis.ipynb       # Main notebook
│   ├── data_mentah_dan_proses/ # Raw and processed data
│   │   ├── ulasan_mentah.csv   # Raw dataset
│   │   ├── ulasan_bersih.csv   # Cleaned dataset
│   │   ├── hasil_prediksi.csv  # Prediction results
│   │   └── *.pkl               # Trained models
│   └── gambar_laporan/         # Report images (plots, charts)
├── LK1_Abdulkharis_2388010004_NLP.*  # Lembar Kerja 1
├── Laporan_NLP_Abdul_Kharis_2388010004.*  # Final Report
└── turi3cv.ipynb                        # Notebook praktikum
```

---

## 📋 Daftar Praktikum

| Pertemuan | Topik | File |
|-----------|-------|------|
| LK 1 | Pengantar NLP & Text Preprocessing | `LK1_Abdulkharis_2388010004_NLP.pdf` |
| TURI 3 | Computer Vision & NLP Integration | `turi3cv.ipynb` |
| Mandiri | NLP Pipeline Project | `nlp mandiri/abdulkharis.ipynb` |

---

## 🛠️ Instalasi

### 1. Install Dependencies

```bash
pip install nltk spacy pandas numpy matplotlib jupyter scikit-learn
python -m nltk.downloader all
python -m spacy download en_core_web_sm
```

### 2. Jalankan Notebook

```bash
# NLP Mandiri
cd NLP/nlp mandiri
jupyter notebook abdulkharis.ipynb

# TURI 3
cd NLP
jupyter notebook turi3cv.ipynb
```

---

## 📚 Topik yang Dibahas

- Text Preprocessing (Tokenization, Stemming, Lemmatization)
- Stopwords Removal
- Part-of-Speech Tagging
- Named Entity Recognition (NER)
- Sentiment Analysis
- Word Embeddings (Word2Vec, GloVe)
- Text Classification
- NLP Pipeline Implementation

---

## 📊 Dataset

Folder `nlp mandiri/data_mentah_dan_proses/` berisi:

| File | Deskripsi |
|------|-----------|
| `ulasan_mentah.csv` | Data mentah (raw reviews) |
| `ulasan_bersih.csv` | Data yang sudah diproses |
| `hasil_prediksi.csv` | Hasil prediksi model |
| `error_analysis_50_sampel.csv` | Error analysis |
| `best_params.csv` | Best hyperparameters |
| `*.pkl` | Trained models (pickle) |

---

## 🔗 Referensi

- **NLTK Documentation:** https://www.nltk.org/
- **spaCy Documentation:** https://spacy.io/
- **Hugging Face:** https://huggingface.co/
- **NLP with Python:** https://www.nltk.org/book/
- **Scikit-learn Text Processing:** https://scikit-learn.org/stable/modules/classes.html#module-sklearn.feature_extraction.text

---

## 👨‍💻 Author

**Abdul Kharis**  
NIM: 2388010004  
Semester 6 - Informatics Engineering

---

*Last Updated: April 2026*
