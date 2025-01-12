from flask import Flask, render_template, request, session
import nltk
import string
import random
from nltk.stem import WordNetLemmatizer
from sentence_transformers import SentenceTransformer
import torch
import json

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Clé secrète pour la session

# Charger la base de connaissances depuis le fichier JSON
with open("knowledge_base.json", "r", encoding="utf-8") as file:
    knowledge_base = json.load(file)

categories = list(knowledge_base.keys())

theme_suggestions = {
    "énergie": ("Parler de la consommation d'énergie", "Comment réduire ma consommation d'énergie ?"),
    "sécurité": ("Parler de la sécurité informatique", "Comment protéger mes données personnelles ?"),
    "environnement": ("Parler de l'impact environnemental du numérique", "Comment est-ce que le numérique impact l'environnement ?"),
    "déchets": ("Parler de la gestion des déchets électroniques", "Comment réduire mes déchets électroniques ?"),
    "équilibre": ("Parler de l'équilibre numérique", "Comment trouver un équilibre sain avec mes appareils numériques ?"),
    "éthique": ("Parler de l'éthique du numérique", "Quels sont les aspects éthiques du numérique ?"),
    "logiciels_libres": ("Parler des logiciels libres", "Quels sont les avantages des logiciels libres ?"),
    "accessibilité": ("Parler de l'accessibilité numérique", "Comment rendre l'informatique plus accessible à tous ?"),
    "sobriété": ("Parler de la sobriété numérique", "Comment adopter une sobriété numérique au quotidien ?"),
    "responsabilité": ("Parler de la responsabilité sociale du numérique", "Quelles sont les responsabilités sociales des acteurs du numérique ?")
}

lemmatizer = WordNetLemmatizer()

def preprocess_user_input(user_input):
    user_input = user_input.lower()
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(user_input)
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(tokens)

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
cat_embeddings = model.encode(categories, convert_to_tensor=True)

def generate_response(user_input):
    text = preprocess_user_input(user_input)
    query_embedding = model.encode(text, convert_to_tensor=True)
    similarities = torch.nn.functional.cosine_similarity(query_embedding, cat_embeddings)
    best_idx = torch.argmax(similarities).item()
    best_category = categories[best_idx]
    best_score = similarities[best_idx].item()

    if best_score < 0.2:
        return "Je suis désolé, je ne suis pas sûr de pouvoir répondre à cette question. Pouvez-vous préciser votre demande ?"
    else:
        return knowledge_base[best_category]

@app.route("/", methods=["GET", "POST"])
def index():
    if 'chat_history' not in session:
        # Initialisation de la session sans messages
        session['chat_history'] = []
        # Plus besoin d'échantillonner, on va simplement afficher tous les thèmes
        session['all_themes'] = categories  # On garde une clé 'all_themes'

    if request.method == "POST":
        selected_theme = request.form.get("theme", None)
        user_query = request.form.get("user_query", "").strip()

        if selected_theme and selected_theme in theme_suggestions:
            _, user_message = theme_suggestions[selected_theme]
            session['chat_history'].append(("user", user_message))
            bot_response = generate_response(user_message)
            session['chat_history'].append(("assistant", bot_response))
            session.modified = True

        elif user_query:
            session['chat_history'].append(("user", user_query))
            bot_response = generate_response(user_query)
            session['chat_history'].append(("assistant", bot_response))
            session.modified = True

    return render_template("index.html",
                           chat_history=session.get('chat_history', []),
                           all_themes=session.get('all_themes', []),
                           theme_suggestions=theme_suggestions)

if __name__ == "__main__":
    app.run(debug=True)

