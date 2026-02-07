from flask import Flask, render_template, request
import numpy as np
import pickle

with open('MINI_HOUSE.plk', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        features = [float(x) for x in request.form.values()]
        final_features = np.array([features])
        prediction = model.predict(final_features)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
