from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('multiple_reg_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Print form data for debugging
        print(request.form)

        # Get form values safely
        tv = request.form.get('tv')
        radio = request.form.get('radio')
        newspaper = request.form.get('newspaper')

        # Debug print
        print(f"TV={tv}, Radio={radio}, Newspaper={newspaper}")

        # Convert to float
        tv = float(tv)
        radio = float(radio)
        newspaper = float(newspaper)

        # Predict
        prediction = model.predict([[tv, radio, newspaper]])[0]
        price=prediction[0]

        return render_template('index.html', prediction_text=f"Predicted Sales no of quantity:{round(price,2)}")

    except Exception as e:
        # Print the error in the console
        print("Error:", e)
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
