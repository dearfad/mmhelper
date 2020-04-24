from flask import Flask, request
import joblib

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def predict():

    css = '<style>form{width:600px;margin:20px auto;background-color:seashell;font-family:SimSun;\
                       text-align:left;padding: 20px;line-height:22px}</style>'

    form = '<form method="POST" action="/"> \
                <h2>预测乳腺癌患者5年后生存状况<h2>\
                \
                <h3>请输入病例信息 <br>\
                <br>\
                病理分期: <br>\
                <select name="Stage">\
                <option value="1">I期</option> \
                <option value="2">II期</option> \
                <option value="3">III期</option> \
                <option value="4">IV期</option> \
                </select><br> \
                \
                分子分型: <br>\
                <select name="Luminal"> \
                <option value="1">Luminal A</option> \
                <option value="2">Luminal B1</option> \
                <option value="3">Luminal B2</option> \
                <option value="4">HER2过表达型</option> \
                <option value="5">三阴性</option> \
                </select><br> \
                \
                分限度分级: <br>\
                <select name="Risk"> \
                <option value="1">低危</option> \
                <option value="2">中危</option> \
                <option value="3">高危</option> \
                </select> <br>\
                \
                年龄分组: <br>\
                <select name="Age"> \
                <option value="1"><35岁</option> \
                <option value="2">35-50岁</option> \
                <option value="3">>50岁</option> \
                </select> <br>\
                \
                月经状态:<br> \
                <select name="Menopause"> \
                <option value="0">绝经前</option> \
                <option value="1">绝经后</option> \
                </select> <br>\
                \
                组织学分级: <br>\
                <select name="MBNG"> \
                <option value="1">I级 </option> \
                <option value="2">II级</option> \
                <option value="3">III级</option> \
                </select> <br>\
                \
                T分期: <br>\
                <select name="T"> \
                <option value="1">T1</option> \
                <option value="2">T2</option> \
                <option value="3">T3</option> \
                <option value="4">T4</option> \
                </select> <br>\
                \
                N分期:<br> \
                <select name="N"> \
                <option value="0">N0</option> \
                <option value="1">N1</option> \
                <option value="2">N2</option> \
                <option value="3">N3</option> \
                </select> <br>\
                \
                M分期: <br>\
                <select name="M"> \
                <option value="0">M0</option> \
                <option value="1">M1</option> \
                </select> <br>\
                \
                ER: <br>\
                <select name="ER"> \
                <option value="0">阴性</option> \
                <option value="1">阳性</option> \
                </select> <br>\
                \
                PR:<br>\
                <select name="PR"> \
                <option value="0">阴性</option> \
                <option value="1">阳性</option> \
                </select><br> \
                \
                Her2:<br>\
                <select name="Her2"> \
                <option value="1">-/+</option> \
                <option value="2">++</option> \
                <option value="3">+++</option> \
                </select> <br>\
                \
                Ki67:<br>\
                <select name="Ki67"> \
                <option value="1">＜30%</option> \
                <option value="2">≥30%</option> \
                </select> <br>\
                \
                有无周边组织浸润:<br>\
                <select name="Infiltration"> \
                <option value="0">无</option> \
                <option value="1">有</option> \
                </select><br> \
                \
                内分泌治疗:<br>\
                <select name="Endocrine"> \
                <option value="0">无</option> \
                <option value="1">有</option> \
                </select> <br>\
                \
                化疗:<br>\
                <select name="Chemotherapy"> \
                <option value="0">无</option> \
                <option value="1">有</option> \
                </select><br> \
                \
                放疗:<br>\
                <select name="Radiotherapy"> \
                <option value="0">无</option> \
                <option value="1">有</option> \
                </select> <br>\
                \
            <br><input type="submit" value="START"></form>'

    result = ''
    proba=''

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
        Endocrine = request.form.get('Endocrine')
        Chemotherapy = request.form.get('Chemotherapy')
        Radiotherapy = request.form.get('Radiotherapy')

        predict = model.predict(
            [[Stage, Luminal, Risk, Age, Menopause, MBNG, T, N, M, ER, PR, Her2, Ki67, Infiltration,Endocrine,Chemotherapy,Radiotherapy]])
        proba=model.predict_proba(
            [[Stage, Luminal, Risk, Age, Menopause, MBNG, T, N, M, ER, PR, Her2, Ki67, Infiltration,Endocrine,Chemotherapy,Radiotherapy]])
        
        if predict[0] == 1:
            death = '<font color="red">死亡</font>'
        else:
            death = '<font color="green">生存</font>'

        result = f'<H3>预测5年预后: {death}</H3>'
        
        proba=f'<H3>预测概率: {proba}</H3>'
        
    return css + form + result+ proba


if __name__ == '__main__':

    model = joblib.load("moon.pkl")

    app.run(host="0.0.0.0", port="5000")