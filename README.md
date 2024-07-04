---
title: Ml Book Recommendation System
emoji: 📊
colorFrom: red
colorTo: yellow
sdk: streamlit
sdk_version: 1.36.0
app_file: app.py
pinned: false
license: mit
---

# Book Recommendation App

This is a simple book recommendation app built with Streamlit using the Amazon Books Reviews dataset from Kaggle.

## Dataset

The dataset has the following columns:

- `Title`: Book Title
- `descripe`: Description of the book
- `authors`: Name of book authors
- `image`: URL for book cover
- `publisher`: Name of the publisher
- `publishedDate`: The date of publish
- `categories`: Genres of books
- `ratingsCount`: Averaging rating for book

## Installation

1. **Clone the repository** (if using a version control system):
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
    python -m venv book_recommendation_env
    source book_recommendation_env/bin/activate  # On Windows, use `book_recommendation_env\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Running the App**:
   ```bash
   streamlit run app.py
   ```

### Instructions Summary

1. **Clone the repository** (or set up your project directory).
2. **Create and activate a virtual environment** (optional but recommended).
3. **Install required packages** using `pip install -r requirements.txt`.
4. **Download the dataset** and place it in the project directory.
5. **Run the app** using `streamlit run app.py`.