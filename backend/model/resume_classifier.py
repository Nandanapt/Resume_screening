import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load the trained model and vectorizer
vectorizer = pickle.load(open('model/vectorizer.pkl', 'rb'))
classifier = pickle.load(open('model/classifier.pkl', 'rb'))

def classify_resume(resume_text):
    # Transform the resume text and classify it
    resume_vector = vectorizer.transform([resume_text])
    prediction = classifier.predict(resume_vector)
    return prediction[0]
