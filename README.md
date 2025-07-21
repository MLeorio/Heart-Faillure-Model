# 🫀 Heart Failure Predictor - Flask App

Une application web simple basée sur **Flask** pour prédire le risque de décès dû à une insuffisance cardiaque à partir de données cliniques.  
Le modèle de Machine Learning atteint une précision de plus de **80 %**.

---

## 🌐 Démo en ligne

🖥️ [Voir la démo sur Render](https://ton-url-render.com) *(à modifier après déploiement)*

---

## 📦 Fonctionnalités

- Formulaire HTML ergonomique avec Bootstrap
- Prédiction du risque de décès en temps réel
- Modèle ML entraîné avec Scikit-learn
- Interface simple et responsive
- Déploiement facile via Render

---

## 🧠 Données d’entrée (features)

Les données attendues sont :

| Feature                     | Description |
|----------------------------|-------------|
| `age`                      | Âge du patient |
| `anaemia`                  | Anémie (1: Oui, 0: Non) |
| `creatinine_phosphokinase`| Niveau de CPK dans le sang |
| `diabetes`                 | Diabète (1: Oui, 0: Non) |
| `ejection_fraction`        | Pourcentage d’éjection cardiaque |
| `high_blood_pressure`      | Hypertension (1: Oui, 0: Non) |
| `platelets`                | Nombre de plaquettes dans le sang |
| `serum_creatinine`         | Niveau de créatinine sérique |
| `serum_sodium`             | Niveau de sodium sérique |
| `sex`                      | Sexe (1: Homme, 0: Femme) |
| `smoking`                  | Fumeur (1: Oui, 0: Non) |
| `time`                     | Temps de suivi en jours |

---

## ⚙️ Installation locale

```bash
git clone https://github.com/ton-utilisateur/heart_app.git
cd heart_app
pip install -r requirements.txt
python app.py
```

Ensuite, ouvre `http://localhost:5000` dans ton navigateur.

---

## 🚀 Déploiement sur Render

1. Pousse ce projet sur GitHub
2. Crée un compte sur [Render](https://render.com)
3. Clique sur **"New + > Web Service"**
4. Choisis ton repo
5. Render détectera automatiquement `render.yaml`
6. Déploie ton app 🚀

---

## 📁 Structure du projet

```
heart_app/
├── app.py                  # Application Flask
├── heart_scaler.pkl        # Scaler pour la normalisation
├── best_heart_model.pkl    # Modèle ML entraîné
├── requirements.txt        # Dépendances Python
├── render.yaml             # Config Render
└── templates/
    └── form.html           # Formulaire HTML
```

---

## 📊 Modèle entraîné

- Modèle : `RandomForestClassifier`
- Accuracy : **~85%**
- Données : [Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)

---

## ✨ Auteurs

- **Fernand** – Idée et développement
- **Catalina (ChatGPT)** – Support technique et génération de code

---

## 📜 Licence

Projet open source sous licence MIT.