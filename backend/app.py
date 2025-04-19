from flask import Flask, request, render_template
import os
import PyPDF2
import pickle
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load trained model and vectorizer
vectorizer = pickle.load(open('model/vectorizer.pkl', 'rb'))
classifier = pickle.load(open('model/classifier.pkl', 'rb'))

# Home page
@app.route('/')
def home():
    return render_template('upload.html')

# Handle file upload and prediction
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return render_template('result.html', prediction="⚠️ No file part in request.")

    file = request.files['resume']
    if not file or file.filename == '':
        return render_template('result.html', prediction="⚠️ No file selected.")

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    text = extract_text_from_pdf(filepath)
    if not text.strip():
        return render_template('result.html', prediction="⚠️ No text extracted from the PDF.")

    # Predict job role
    text_vector = vectorizer.transform([text])
    prediction = classifier.predict(text_vector)[0]

    return render_template('result.html', prediction=prediction)

# Extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content
    return text

if __name__ == '__main__':
    app.run(debug=True)
