from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Charger le modèle pré-entraîné et le scaler
model = joblib.load('heart_disease_model.pkl')
scaler = joblib.load('scaler.pkl')

# Liste des features attendues par le modèle
features = [
    "age", "anaemia", "creatinine_phosphokinase", "diabetes",
    "ejection_fraction", "high_blood_pressure", "platelets",
    "serum_creatinine", "serum_sodium", "sex", "smoking", "time"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            # Recuperer les donnees du formulaire
            values = [float(request.form.get(feat)) for feat in features]
            input_array = np.array(values).reshape(1, -1)
            input_scaled = scaler.transform(input_array)
            result = model.predict(input_scaled)[0]
            prediction = "Le patient a un risque de maladie cardiaque." if result == 1 else "Le patient n'a pas de risque de maladie cardiaque."
        except Exception as e:
            prediction = f"Erreur lors de la prédiction : {str(e)}"
    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True, port=2706)