import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Example data: Replace these with your actual resumes and labels
resumes = [
    "Experienced software engineer with expertise in Python, JavaScript, and web development.",
    "Data scientist with experience in machine learning, Python, and data analysis.",
    "Web developer proficient in HTML, CSS, JavaScript, and React."
]
labels = [
    "Software Engineer",
    "Data Scientist",
    "Web Developer"
]

# Step 1: Initialize and train the TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(resumes)

# Step 2: Initialize and train the classifier (Logistic Regression in this case)
classifier = LogisticRegression()
classifier.fit(X, labels)

# Step 3: Save the trained vectorizer and classifier to .pkl files
with open('model/vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

with open('model/classifier.pkl', 'wb') as classifier_file:
    pickle.dump(classifier, classifier_file)

print("Model training and saving complete.")
