import pandas as pd
import re
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text
def train_and_save_model(csv_path):
    df = pd.read_csv(csv_path)
    df['combined_text'] = df['title'].fillna('') + " " + \
                          df['description'].fillna('') + " " + \
                          df['requirements'].fillna('')
    df['text_cleaned'] = df['combined_text'].apply(clean_text)
    X = df['text_cleaned']
    y = df['fraudulent']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)
    model = LogisticRegression(max_iter=1000, class_weight='balanced')
    model.fit(X_train_tfidf, y_train)
    predictions = model.predict(X_test_tfidf)
    print(f"Model Doğruluğu: {accuracy_score(y_test, predictions)}")
    print(classification_report(y_test, predictions))
    with open('job_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('job_tfidf.pkl', 'wb') as f:
        pickle.dump(tfidf, f)
    print("Model dosyaları başarıyla oluşturuldu.")
if __name__ == "__main__":
    train_and_save_model('fake_job_postings.csv')
