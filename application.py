from flask import Flask, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import json

application = Flask(__name__)

vectorizer = CountVectorizer()

def load_vectorizer():
    with open("count_vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return vectorizer

def load_model():
    with open("basic_classifier.pkl", "rb") as f:
        model = pickle.load(f)
    return model

vectorizer = load_vectorizer()
model = load_model()

@application.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        text = data.get("text", "")
        vectorized_text = vectorizer.transform([text])
        prediction = model.predict(vectorized_text)
        return json.dumps({"prediction": prediction[0]}) 
    except Exception as e:
        return json.dumps({"error": str(e)}), 500

@application.route("/")
def index():
    return "Your Flask App Works! V1.0"


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080, debug=True)