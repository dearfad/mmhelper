from flask import Flask, request
import joblib

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def predict():


    form = '<form method="POST" action="http://127.0.0.1:5000" name="testform"> \
            Age: <input type="text" name="age" value="50"> \
            Sex: <input type="text" name="sex" value="1"> \
            Height: <input type="text" name="height" value="150"> \
            Weight: <input type="text" name="weight" value="60"> \
            <input type="submit" value="START"></form>'

    result = ''

    if request.method == 'POST':
        age = request.form.get('age')
        sex = request.form.get('sex')
        height = request.form.get('height')
        weight = request.form.get('weight')
        predict = model.predict([[age, sex, height, weight]])
        result = f'<H1>result: {predict[0]}</H1>'
        form = f'<form method="POST" action="http://127.0.0.1:5000" name="testform"> \
            Age: <input type="text" name="age" value="{age}"> \
            Sex: <input type="text" name="sex" value="{sex}"> \
            Height: <input type="text" name="height" value="{height}"> \
            Weight: <input type="text" name="weight" value="{weight}"> \
            <input type="submit" value="START"></form>'

    return form + result


if __name__ == '__main__':

    model = joblib.load("demo.pkl")

    app.run(debug=True)
