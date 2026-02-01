from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        st_slope = request.form['st_slope']
        ex_angina = request.form['ex_angina']
        oldpeak = float(request.form['oldpeak'])
        chest_pain = request.form['chest_pain'] 

        slope_map = {'Up': 0, 'Flat': 1, 'Down': 2}
        angina_map = {'N': 0, 'Y': 1}
        cp_map = {'ASY': 0, 'ATA': 1, 'NAP': 2, 'TA': 3}

        features = np.array([[
            slope_map[st_slope],
            angina_map[ex_angina],
            oldpeak,
            cp_map[chest_pain]
        ]])

        prediction = model.predict(features)
        result = "Positive for Heart Disease" if prediction[0] == 1 else "Negative (Normal)"

        return render_template('index.html', prediction_text=f'Prediction: {result}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
