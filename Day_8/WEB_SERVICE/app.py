from flask import Flask, request, jsonify, render_template
import numpy as np
from tensorflow.python.keras.models import load_model
from tensorflow.python.layers.normalization import BatchNormalization
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

stress_model = load_model('Day_8/WEB_SERVICE/stress_model.h5', custom_objects={'BatchNormalization': BatchNormalization}, compile=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    humidity = float(request.form['humidity'])
    temperature = float(request.form['temperature'])
    step_count = float(request.form['stepCount'])

    converted_temperature = (temperature * 9/5) + 32
    print(temperature)

    user_data = np.array([[humidity, converted_temperature, step_count]])
    scaler = StandardScaler()
    user_data_scaled = scaler.fit_transform(user_data)

    y_pred = stress_model.predict(user_data_scaled)
    predicted_class = np.argmax(y_pred, axis=1)[0]
    
    stress_levels = ["Low", "Medium", "High"]
    predicted_stress_level = stress_levels[predicted_class]
    print(predicted_stress_level)

    return jsonify({'stress_level': predicted_stress_level})

if __name__ == '__main__':
    app.run(debug=True)
