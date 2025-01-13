from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk
import string
from nltk.stem import WordNetLemmatizer
from sentence_transformers import SentenceTransformer
import torch
import json
import random

# Initialisation des outils NLP
lemmatizer = WordNetLemmatizer()
nltk.download("punkt")
nltk.download("wordnet")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Charger le corpus
with open("green_it_corpus.json", "r", encoding="utf-8") as f:
    corpus = json.load(f)

# Initialisation du chatbot
chatbot = ChatBot(
    "GreenITChatbot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Je suis désolé, je ne comprends pas votre question. Pouvez-vous reformuler ?",
            "maximum_similarity_threshold": 0.75
        }
    ],
    database_uri="sqlite:///green_it_chatbot.db"
)

# Entraîner le chatbot
trainer = ListTrainer(chatbot)
for item in corpus:
    trainer.train([item["question"], item["answer"]])

# Prétraitement de l'entrée utilisateur
def preprocess_question(question):
    question = question.lower()
    question = question.translate(str.maketrans("", "", string.punctuation))
    tokens = nltk.word_tokenize(question)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(lemmatized_tokens)

# Calculer la similarité avec le modèle NLP
def find_best_match(user_input, corpus_questions):
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    corpus_embeddings = model.encode(corpus_questions, convert_to_tensor=True)
    similarities = torch.nn.functional.cosine_similarity(user_embedding, corpus_embeddings)
    best_idx = torch.argmax(similarities).item()
    best_score = similarities[best_idx].item()
    return best_idx, best_score

# Traiter le message utilisateur
def process_user_message(user_message):
    questions = [item["question"] for item in corpus]
    answers = [item["answer"] for item in corpus]

    processed_input = preprocess_question(user_message)

    bot_response = chatbot.get_response(processed_input)
    if bot_response.confidence < 0.5:
        best_idx, best_score = find_best_match(processed_input, questions)
        if best_score > 0.5:
            return answers[best_idx]
        else:
            return "Je suis désolé, je ne comprends pas votre question. Pouvez-vous reformuler ?"
    else:
        return str(bot_response)

# Obtenir 5 thèmes aléatoires
def get_random_themes():
    questions = [item["question"] for item in corpus]
    return random.sample(questions, 5)
