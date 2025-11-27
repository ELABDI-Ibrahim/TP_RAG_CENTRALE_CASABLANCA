# 🚀 Guide de Déploiement - RAG System

## Guide Simple pour Déployer le Projet

Ce guide explique comment installer et lancer le système RAG de manière très simple.

---

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir installé:

1. **Python 3.9 ou supérieur**
   ```bash
   python --version
   ```

2. **Node.js 18 ou supérieur** (pour l'interface React)
   ```bash
   node --version
   ```

3. **npm** (généralement inclus avec Node.js)
   ```bash
   npm --version
   ```

---

## 🔧 Installation (Une Seule Fois)

### Étape 1: Installer les Dépendances Python

Ouvrez un terminal dans le dossier du projet et exécutez:

```bash
pip install -r requirements.txt
```

**Temps estimé:** 5-10 minutes (téléchargement des modèles)

### Étape 2: Installer les Dépendances Node.js

```bash
cd frontend
npm install
cd ..
```

**Temps estimé:** 2-3 minutes

---

## 🎯 Lancement du Système

Le système nécessite **2 terminaux** (un pour le backend, un pour le frontend).

### Terminal 1: Backend (API Python)

```bash
python src/backend/api.py
```

**Attendez de voir:**
```
✅ API Server ready!
📡 Server at: http://127.0.0.1:8000
```

**Ne fermez pas ce terminal!**

---

### Terminal 2: Frontend (Interface React)

Ouvrez un **nouveau terminal** et exécutez:

```bash
cd frontend
npm run dev
```

**Attendez de voir:**
```
➜  Local:   http://localhost:3000/
```

---

## 🌐 Accéder à l'Interface

Ouvrez votre navigateur et allez à:

**http://localhost:3000**

Vous verrez l'interface avec 3 sections:
- **Gauche:** Gestion des documents
- **Milieu:** Visualisation des documents
- **Droite:** Chat avec l'IA

---

## 📝 Utilisation

### 1. Ajouter des Documents

1. Glissez-déposez des fichiers PDF, DOCX ou MD dans la zone d'upload (section gauche)
2. Ou cliquez sur la zone pour sélectionner des fichiers

### 2. Construire l'Index

1. Cliquez sur le bouton **"Build Index"** en haut à droite
2. Attendez le message de succès (peut prendre quelques minutes)

### 3. Utiliser le Chat

1. Tapez votre question dans la zone de chat (section droite)
2. Appuyez sur **Enter** ou cliquez sur **Send**
3. L'IA répondra en utilisant vos documents!

### 4. Visualiser les Documents

1. Cliquez sur un fichier dans la liste (section gauche)
2. Le document s'affiche dans la section centrale
3. Pour les PDFs, utilisez les boutons Previous/Next pour naviguer

---

## 💻 Alternative: Interface Ligne de Commande

Si vous préférez utiliser le terminal au lieu de l'interface web:

```bash
# Construire l'index
python cli.py build

# Rechercher dans les documents
python cli.py search "votre requête"

# Poser une question
python cli.py ask "votre question"

# Démarrer le chatbot
python cli.py chat
```

---

## ⚙️ Configuration

Tous les paramètres sont dans `Config.yaml`:

- **Chemins:** Où sont les documents et la base vectorielle
- **Modèle d'embeddings:** Modèle HuggingFace utilisé
- **Taille des chunks:** Comment découper les documents
- **Paramètres LLM:** Configuration du modèle de langage

**Aucune modification nécessaire pour un usage basique!**

---

## 🐛 Problèmes Courants

### Le backend ne démarre pas

**Erreur:** `Port 8000 already in use`

**Solution:**
1. Fermez l'application qui utilise le port 8000
2. Ou modifiez le port dans `src/backend/api.py` (ligne finale)

### Le frontend ne démarre pas

**Erreur:** `Cannot find module 'react'`

**Solution:**
```bash
cd frontend
rm -rf node_modules
npm install
```


## 🔑 Variables d'Environnement (Optionnel)

Pour utiliser un modèle LLM HuggingFace, créez un fichier `.env`:

```bash
HUGGINGFACEHUB_API_TOKEN=votre_token_ici
```

**Note:** Non nécessaire pour les fonctionnalités de base.

---

## 📊 Fonctionnalités

### ✅ Implémenté (Q1-Q5):

- **Q1:** Indexation des documents (ChromaDB + HuggingFace)
- **Q2:** Recherche sémantique dans les documents
- **Q3:** Question-Réponse avec LLM
- **Q4:** Évaluation du système
- **Q5:** Chatbot conversationnel (bonus)

### 🎨 Interface Web:

- Upload de documents (drag & drop)
- Gestion de dossiers
- Visualisation PDF/Markdown
- Chat avec l'IA
- Sessions multiples
- Références aux sources

---

## 🛑 Arrêter le Système

Pour arrêter le système:

1. Dans le terminal frontend: Appuyez sur **Ctrl+C**
2. Dans le terminal backend: Appuyez sur **Ctrl+C**

---

## 📞 Support

### Documentation:

- `README.md` - Documentation principale
- `TP_COMPLIANCE.md` - Conformité aux exigences du TP
- `QUICK_START.md` - Guide rapide

### API Documentation:

Une fois le backend lancé, visitez:
- **http://127.0.0.1:8000/docs** - Documentation interactive de l'API

---

## ✅ Checklist de Déploiement

Avant de présenter:

- [ ] Python 3.9+ installé
- [ ] Node.js 18+ installé
- [ ] Dépendances Python installées (`pip install -r requirements.txt`)
- [ ] Dépendances Node.js installées (`cd frontend && npm install`)
- [ ] Documents PDF dans le dossier `data/`
- [ ] Backend démarre sans erreur
- [ ] Frontend démarre sans erreur
- [ ] Interface accessible sur http://localhost:3000
- [ ] Index construit avec succès
- [ ] Chat fonctionne

---

## 🎓 Pour le Professeur

### Déploiement Rapide (5 minutes):

```bash
# 1. Installer dépendances
pip install -r requirements.txt
cd frontend && npm install && cd ..

# 2. Lancer backend (Terminal 1)
python src/backend/api.py

# 3. Lancer frontend (Terminal 2)
cd frontend && npm run dev

# 4. Ouvrir http://localhost:3000
```

### Tester le Système:

1. Uploader des PDFs dans l'interface
2. Cliquer "Build Index"
3. Poser une question dans le chat
4. Vérifier que l'IA répond avec des sources

---

## 🎉 C'est Tout!

Le système est maintenant prêt à être utilisé!

**Questions?** Consultez `README.md` pour plus de détails.

---

**École Centrale Casablanca | TP NLP 2024**

