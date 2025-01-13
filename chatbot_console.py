from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
import nltk
import string
from nltk.stem import WordNetLemmatizer
from sentence_transformers import SentenceTransformer
import torch

# Initialisation du lemmatizer et du modèle NLP
lemmatizer = WordNetLemmatizer()
nltk.download("punkt")
nltk.download("wordnet")

# Charger un modèle d'embeddings
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

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

# Charger le corpus JSON
def load_corpus(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# Entraîner le chatbot
def train_chatbot(chatbot, corpus):
    trainer = ListTrainer(chatbot)
    for item in corpus:
        trainer.train([item["question"], item["answer"]])
    print("Entraînement terminé avec succès.")

# Prétraitement de la question utilisateur
def preprocess_question(question):
    question = question.lower()
    question = question.translate(str.maketrans("", "", string.punctuation))
    tokens = nltk.word_tokenize(question)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(lemmatized_tokens)

# Calculer la similarité entre la question utilisateur et celles du corpus
def find_best_match(user_input, corpus_questions):
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    corpus_embeddings = model.encode(corpus_questions, convert_to_tensor=True)
    similarities = torch.nn.functional.cosine_similarity(user_embedding, corpus_embeddings)
    best_idx = torch.argmax(similarities).item()
    best_score = similarities[best_idx].item()
    return best_idx, best_score

# Interagir avec le chatbot
def chat_with_bot(chatbot, corpus):
    questions = [item["question"] for item in corpus]
    answers = [item["answer"] for item in corpus]

    print("Chatbot Green IT est prêt à discuter. Tapez 'exit' pour quitter.")
    while True:
        user_input = input("Vous: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: À bientôt ! 👋")
            break

        # Prétraitement de l'entrée utilisateur
        processed_input = preprocess_question(user_input)

        # Essayez de trouver une réponse exacte via ChatterBot
        bot_response = chatbot.get_response(processed_input)

        # Si la réponse de ChatterBot est la réponse par défaut, utilisez la similarité
        if bot_response.confidence < 0.5:
            best_idx, best_score = find_best_match(processed_input, questions)
            if best_score > 0.5:
                print(f"Chatbot: {answers[best_idx]} (Score de similarité : {best_score:.2f})")
            else:
                print("Chatbot: Je suis désolé, je ne comprends pas votre question. Pouvez-vous reformuler ?")
        else:
            print(f"Chatbot: {bot_response}")

if __name__ == "__main__":
    # Charger et entraîner le chatbot
    corpus = load_corpus("green_it_corpus.json")  # Remplacez par le chemin de votre fichier JSON
    train_chatbot(chatbot, corpus)
    
    # Lancer la session de chat
    chat_with_bot(chatbot, corpus)
