from flask import Flask, render_template, request 
import pickle
import numpy as np

model = pickle.load(open('modelcap.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ASD.html')

@app.route('/predict',methods=['POST'])
def predict_ASD():
    A1=int(request.form.get('A1'))
    A2=int(request.form.get('A2'))
    A3=int(request.form.get('A3'))
    A4=int(request.form.get('A4'))
    A5=int(request.form.get('A5'))
    A6=int(request.form.get('A6'))
    A7=int(request.form.get('A7'))
    A8=int(request.form.get('A8'))
    A9=int(request.form.get('A9'))
    A10=int(request.form.get('A10'))
    Age=int(request.form.get('Age Months'))
    Sex=int(request.form.get('Sex_m'))
    Latino=int(request.form.get('Ethnicity_Latino'))
    NativeIndian=int(request.form.get('Ethnicity_NativeIndian'))
    Others=int(request.form.get('Ethnicity_Others'))
    Pacifica=int(request.form.get('Ethnicity_Pacifica'))
    WhiteEuropean=int(request.form.get('Ethnicity_White European'))
    asian=int(request.form.get('Ethnicity_asian'))
    black=int(request.form.get('Ethnicity_black'))
    middleeastern=int(request.form.get('Ethnicity_middle eastern'))
    mixed=int(request.form.get('Ethnicity_mixed'))
    southasian=int(request.form.get('Ethnicity_south asian'))
    jaudice=int(request.form.get('Jaundice_yes'))
    FamilymemwithASD=int(request.form.get('Family mem with ASD_yes'))
    Healthcareprofessional=int(request.form.get('Who completed the test_Health care professional'))
    Others=int(request.form.get('Who completed the test_Others'))
    Self=int(request.form.get('Who completed the test_Self'))
    Others=int(request.form.get('Who completed the test_Others'))
    familymember=int(request.form.get('Who completed the test_family member'))
    

    #prediction
    result = model.predict(np.arrray([A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, Age Months, Sex_m,Ethnicity_Latino,Ethnicity_NativeIndian, Ethnicity_Others,Ethnicity_Pacifica,Ethnicity_White European,Ethnicity_asian,Ethnicity_black,Ethnicity_middle eastern,Ethnicity_mixed,Ethnicity_south asian,Jaundice_yes,Family mem with ASD_yes,Who completed the test_Health care professional,Who completed the test_Others,Who completed the test_Self,Who completed the test_family member]).reshape(1,28))

    if result[0] == 1:
        result = 'ASD'
    else:
        result='No ASD'
    
    return render_template('ASD.html',result=result)

if __name__=='__main__':
    app.run(host='0.0.0.0',port = 8080)