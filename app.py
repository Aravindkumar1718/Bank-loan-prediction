from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/form')
def form():
    return render_template('form.html')
@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Retrieve the input values from the form
        gender = int(request.form["gender"])
        married = int(request.form["married"])
        dependents = int(request.form["dependents"])
        education = int(request.form["education"])
        self_employed = int(request.form["self_employed"])
        credit_history = int(request.form["credit_history"])
        property_area = int(request.form["property_area"])
        income = int(request.form["income"])

        # Make a prediction
        prediction = model.predict([[gender, married, dependents, education, self_employed, credit_history, property_area, income]])
        result = "Approved" if prediction[0] == 1 else "Not Approved"

        return render_template("form.html", prediction_result=result)

if __name__ == "__main__":
    app.run(debug=True)
