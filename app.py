from flask import Flask, jsonify, request
import json
import pickle

# create a flask app
app = Flask(__name__)

# function to load the model 
def load_model():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model 

@app.route('/predict', methods=['GET'])
def predict():

    # parse the input features from the JSON Request 
    request_json = request.get_json()

    x = float(request_json['input'])

    # load the model 
    model = load_model()
    prediction = model.predict([[x]])[0]

    response = json.dumps({ 'response': prediction })
    return response, 200

if __name__ == "__main__":
    application.run(debug=True)
    