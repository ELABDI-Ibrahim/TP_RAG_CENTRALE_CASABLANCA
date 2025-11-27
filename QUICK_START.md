# ⚡ Quick Start Guide

## Démarrage Rapide en 5 Minutes

### 1. Installer les Dépendances

```bash
# Python
pip install -r requirements.txt

# Node.js (pour l'interface React)
cd frontend
npm install
cd ..
```

### 2. Lancer le Système

**Terminal 1 - Backend:**
```bash
python src/backend/api.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### 3. Ouvrir le Navigateur

Allez à: **http://localhost:3000**

### 4. Utiliser

1. Glissez-déposez des PDFs
2. Cliquez "Build Index"
3. Commencez à chatter!

---

## Alternative: Interface Ligne de Commande

```bash
# Construire l'index
python cli.py build

# Rechercher
python cli.py search "votre requête"

# Poser une question
python cli.py ask "votre question"

# Chatbot
python cli.py chat
```

---

**Pour plus de détails, voir `DEPLOYMENT_GUIDE.md`**
