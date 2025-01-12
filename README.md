# 🌱💻 Green IT Chatbot 💻🌱

Un **chatbot intelligent** pour promouvoir une informatique durable 🌍, répondre à des questions sur la consommation énergétique ⚡, la gestion des déchets électroniques ♻️, et bien plus encore.

---

## 📋 Description 📝

Ce projet utilise **Flask** 🐍 pour le backend et **Sentence Transformers** 🧠 pour analyser les questions des utilisateurs. La base de connaissances 🗂️ est stockée dans un fichier **JSON** facile à modifier, ce qui rend le projet simple à personnaliser.

---

## 🚀 Fonctionnalités ✨

- 🤖 **Réponses intelligentes** basées sur une base de connaissances thématique.
- 🔍 **Analyse des questions** grâce à Sentence Transformers.
- 🛠️ **Facilité de personnalisation** avec une base de connaissances en JSON.
- 🌐 **Interface utilisateur web** simple et accessible.

---

## 🛠️ Installation 🖥️

### 1. Clonez le dépôt 🛒
```bash
git clone https://github.com/your-repo/green-it-chatbot.git
cd green-it-chatbot
```

### 2. Installez les dépendances 📦
Assurez-vous d'avoir **Python** 🐍 installé sur votre machine, puis exécutez :

```bash
pip install -r requirements.txt
```

### 3. Initialisez les ressources NLTK 🧩
Certaines ressources NLTK doivent être téléchargées avant de lancer l'application. Utilisez ces commandes dans un terminal Python :
```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```

### 4. Lancez l'application 🚦
Exécutez la commande suivante pour démarrer le serveur Flask :
```bash
python app.py
```

### 5. Accédez au chatbot 🌟
Ouvrez votre navigateur et visitez [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 📂 Structure du projet 📁

```
green-it-chatbot/
├── app.py               # Fichier principal Flask 🐍
├── requirements.txt     # Liste des dépendances 📦
├── knowledge_base.json  # Base de connaissances 🗂️
├── templates/
│   └── index.html       # Interface utilisateur 🌐
```

---

## 👩‍💻 Utilisation 💬

1. **Posez vos questions** sur des thèmes comme l'énergie ⚡, les déchets électroniques ♻️, ou l'équilibre numérique 🧘.
2. **Recevez des réponses personnalisées** et pertinentes pour adopter des pratiques responsables.
3. Explorez, apprenez et contribuez à un numérique plus durable ! 🌱

---

## ✨ Améliorations possibles 🚀

- 🎨 Ajout d'une interface utilisateur plus moderne.
- 📈 Extension de la base de connaissances avec de nouveaux sujets.
- ☁️ Hébergement en ligne via **Heroku**, **Render**, ou un serveur dédié.
- 🧠 Intégration d'un modèle de langage avancé pour des réponses encore plus pertinentes.

---

## 📜 Licence 📝

Ce projet est sous licence **MIT** 📖. Consultez le fichier `LICENSE` pour plus d'informations.
