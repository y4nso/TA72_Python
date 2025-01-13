# 🌱 Green IT Chatbot 🌍

Bienvenue sur **Green IT Chatbot** ! Ce projet est un chatbot interactif conçu pour discuter des sujets liés au Green IT. 🌿 Posez vos questions sur la sobriété numérique, la gestion des déchets électroniques, ou d'autres thèmes similaires. Le chatbot est là pour vous répondre intelligemment !

---

## 📖 **Fonctionnalités principales**

✨ **Interface utilisateur moderne :**
- Questions utilisateur alignées à droite (💬 bulle bleue).
- Réponses IA alignées à gauche (🤖 bulle grise).

🎯 **Thèmes aléatoires :**
- Propose 5 sujets choisis au hasard parmi le corpus.
- Les suggestions changent dynamiquement lorsque vous cliquez sur un thème.

🧠 **Modèle NLP avancé :**
- Comprend les questions similaires même si elles ne sont pas identiques à celles du corpus.
- Utilise **Sentence Transformers** pour mesurer la similarité entre phrases.

---

## 🚀 **Démarrage rapide**

### **1. Prérequis**

- Python 3.8 ou plus récent 🐍
- Pip pour gérer les dépendances 📦

### **2. Installation**

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/green-it-chatbot.git
   cd green-it-chatbot
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Lancez l'application :
   ```bash
   python app.py
   ```

4. Ouvrez un navigateur 🌐 et accédez à [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 🛠 **Structure du projet**

```
green_it_chatbot/
├── app.py               # Serveur Flask (backend)
├── chatbot_logic.py     # Logique du chatbot
├── templates/
│   └── index.html       # Interface utilisateur
├── static/
│   ├── style.css        # Styles CSS
│   └── script.js        # Logique JS pour les interactions
├── green_it_corpus.json # Corpus de questions/réponses
├── requirements.txt     # Dépendances Python
```

### **Descriptions :**
- **app.py :** Définit les routes pour l'interface et le traitement des requêtes.
- **chatbot_logic.py :** Gère le traitement des questions et l'entraînement du chatbot.
- **index.html :** Interface utilisateur moderne avec suggestions dynamiques.
- **style.css :** Définit le design des bulles de chat et des suggestions.
- **script.js :** Gère les interactions utilisateur (envoi de messages, clics sur thèmes).

---

## ✨ **Fonctionnement**

1. **Interface utilisateur :**
   - Tapez une question ou cliquez sur un thème proposé dans la colonne de gauche.
   - Les messages utilisateur apparaissent en 💬 bleu.
   - Les réponses du chatbot sont affichées en 🤖 gris.

2. **Suggestions dynamiques :**
   - 5 thèmes aléatoires sont proposés à chaque chargement.
   - Cliquez sur un thème pour poser une question liée et actualiser les suggestions.

3. **Traitement des questions :**
   - Le chatbot utilise **ChatterBot** pour répondre aux questions du corpus.
   - Si aucune réponse claire n'est trouvée, un modèle NLP calcule la similarité pour fournir une réponse pertinente.

---

## 📚 **Technologies utilisées**

- **[Flask](https://flask.palletsprojects.com/)** : Framework web pour le backend.
- **[ChatterBot](https://github.com/gunthercox/ChatterBot)** : Bibliothèque de chatbot basée sur le machine learning.
- **[Sentence Transformers](https://www.sbert.net/)** : Modèle NLP pour mesurer la similarité entre phrases.
- **HTML/CSS/JavaScript** : Interface utilisateur moderne et réactive.

---

## 🧩 **Personnalisation**

### Ajouter de nouveaux thèmes :
1. Ouvrez `green_it_corpus.json`.
2. Ajoutez des paires question/réponse au format suivant :
   ```json
   {
       "question": "Qu'est-ce que la sobriété numérique ?",
       "answer": "La sobriété numérique consiste à réduire l'empreinte écologique du numérique."
   }
   ```

3. Relancez le chatbot :
   ```bash
   python app.py
   ```

---

## 🐛 **Problèmes connus**

- **Taille du corpus limitée :** La compréhension du chatbot dépend fortement de la qualité et de la taille des données du corpus.
- **ChatterBot 1.0.4 :** Cette version est utilisée pour éviter les problèmes de compatibilité.

---

## 🤝 **Contribuer**

Vous souhaitez contribuer ? Voici comment vous pouvez aider :
1. Forkez le dépôt 🍴.
2. Créez une branche pour vos modifications :
   ```bash
   git checkout -b ma-nouvelle-fonctionnalite
   ```
3. Faites vos modifications et validez-les :
   ```bash
   git commit -m "Ajout d'une nouvelle fonctionnalité"
   ```
4. Envoyez vos modifications :
   ```bash
   git push origin ma-nouvelle-fonctionnalite
   ```
5. Ouvrez une Pull Request.

---

## 📝 **Licence**

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.
```

---

### **Requirements.txt**

```plaintext
flask
chatterbot==1.0.4
nltk
sentence-transformers
torch
```

