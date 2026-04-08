from flask import Flask, render_template, request
import pickle
import re
app = Flask(__name__)
model = pickle.load(open('job_model.pkl', 'rb'))
tfidf = pickle.load(open('job_tfidf.pkl', 'rb'))
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        job_description = request.form['job_text']
        cleaned_text = preprocess(job_description)
        vect = tfidf.transform([cleaned_text])
        prediction = model.predict(vect)
        result = "SAHTE İLAN (FRAUDULENT)" if prediction[0] == 1 else "GERÇEK İLAN (REAL)"
        return render_template('index.html',
                               prediction=result,
                               original_text=job_description[:300] + "...")
if __name__ == '__main__':
    app.run(debug=True)