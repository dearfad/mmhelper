from flask import Flask, request
import joblib

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def predict():

    css = '<style>form{width:300px;margin:20px auto;}</style>'
    
    form = '<form method="POST" action="/"> \
                \
                Stage: \
                <select name="Stage"> \
                <option value="1">1</option> \
                <option value="2">2</option> \
                <option value="3">3</option> \
                <option value="4">4</option> \
                </select> \
                \
                Luminal: \
                <select name="Luminal"> \
                <option value="1">1</option> \
                <option value="2">2</option> \
                <option value="3">3</option> \
                <option value="4">4</option> \
                <option value="5">5</option> \
                </select> \
                \
                Risk: \
                <select name="Risk"> \
                <option value="1">1</option> \
                <option value="2">2</option> \
                <option value="3">3</option> \
                </select> \
                \
                Age: \
                <select name="Age"> \
                <option value="1">1</option> \
                <option value="2">2</option> \
                <option value="3">3</option> \
                </select> \
                \
                Menopause \
                <select name="Menopause"> \
                <option value="0">0</option> \
                <option value="1">1</option> \
                </select> \
                \
                MBNG: \
                <select name="MBNG"> \
                <option value="1">1</option> \
                <option value="2">2</option> \
                <option value="3">3</option> \
                </select> \
                \
                T: \
                <select name="T"> \
                <option value="1">1</option> \
                <option value="2">2</option> \
                <option value="3">3</option> \
                <option value="4">4</option> \
                </select> \
                \
                N: \
                <select name="N"> \
                <option value="0">0</option> \
                <option value="1">1</option> \
                <option value="2">2</option> \
                <option value="3">3</option> \
                </select> \
                \
                M: <select name="M"> \
                <option value="0">0</option> \
                <option value="1">1</option> \
                </select> \
                \
                ER: <select name="ER"> \
                <option value="0">0</option> \
                <option value="1">1</option> \
                </select> \
                \
                PR: <select name="PR"> \
                <option value="0">0</option> \
                <option value="1">1</option> \
                </select> \
                \
                Her2: <select name="Her2"> \
                <option value="1">1</option> \
                <option value="2">2</option> \
                <option value="3">3</option> \
                </select> \
                \
                Ki67: <select name="Ki67"> \
                <option value="1">1</option> \
                <option value="2">2</option> \
                </select> \
                \
                Infiltration: <select name="Infiltration"> \
                <option value="0">0</option> \
                <option value="1">1</option> \
                </select> \
                \
            <input type="submit" value="START"></form>'

    result = ''

    if request.method == 'POST':
        Stage = request.form.get('Stage')
        Luminal = request.form.get('Luminal')
        Risk = request.form.get('Risk')
        Age = request.form.get('Age')
        Menopause = request.form.get('Menopause')
        MBNG = request.form.get('MBNG')
        T = request.form.get('T')
        N = request.form.get('N')
        M = request.form.get('M')
        ER = request.form.get('ER')
        PR = request.form.get('PR')
        Her2 = request.form.get('Her2')
        Ki67 = request.form.get('Ki67')
        Infiltration = request.form.get('Infiltration')

        predict = model.predict(
            [[Stage, Luminal, Risk, Age, Menopause, MBNG, T, N, M, ER, PR, Her2, Ki67, Infiltration]])

        if predict[0] == 1:
            death = '<font color="red">死亡</font>'
        else:
            death = '<font color="green">生存</font>'

        result = f'<H3>预测5年预后: {death}</H3>'

    return css + form + result


if __name__ == '__main__':

    model = joblib.load("moon.pkl")

    app.run(host="0.0.0.0", port="5000")
