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
│   └── gambar_laporan/         # Report images
├── LK1_Abdulkharis_2388010004_NLP.docx  # Lembar Kerja 1
├── LK1_Abdulkharis_2388010004_NLP.pdf   # Versi PDF
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
- Data mentah (raw data)
- Data yang sudah diproses
- Dataset untuk training dan testing

---

## 🔗 Referensi

- **NLTK Documentation:** https://www.nltk.org/
- **spaCy Documentation:** https://spacy.io/
- **Hugging Face:** https://huggingface.co/
- **NLP with Python:** https://www.nltk.org/book/

---

## 👨‍💻 Author

**Abdul Kharis**  
NIM: 2388010004  
Semester 6 - Informatics Engineering

---

*Last Updated: March 2026*
