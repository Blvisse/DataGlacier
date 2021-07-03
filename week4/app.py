from flask import Flask,request,render_template,jsonify
import numpy as np
import pickle


app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))





@app.route('/')

def homepage():
    return render_template('homepage.html')




@app.route('/predict', methods=['POST'])

def predict():
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]

    prediction=model.predict(final_features)

    output=round(prediction[0],2)

    return render_template('homepage.html',predictions='The loan prediction is {}'.format(output))


@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)



if __name__ == "__main__":
    app.run(debug=True)