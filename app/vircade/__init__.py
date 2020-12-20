from flask import Flask,request
# from controllers import v_firebase, v_model
from .controllers.v_firebase import datasets
from .controllers.v_model import loadModel, predict
import json
import flask

app = Flask(__name__)

@app.route('/')
def working():
   return "This is working"

@app.route('/model/classify', methods=['GET', 'PUT'])
def test():
  json = request.get_json()
  gameID = json['gameID']
  userId = json['userId']
  ml = json['ml']
  song = json['song']
  for i in range(0, len(ml)):
     for j in range(0, len(ml[i])):
            ml[i][j]= float(ml[i][j])
  x = []
  x.append(ml)
#   y_pred = v_model.predict(x, song)
  y_pred = predict(x, song)
  send_json = {"gameID": gameID, "userId": userId, "y_pred": y_pred}
#   result = v_firebase.datasets.update(send_json["gameID"],send_json["userId"],send_json["y_pred"])
  result = datasets.update(send_json["gameID"],send_json["userId"],send_json["y_pred"])


  return flask.jsonify({
      "data": y_pred,
      "put": result
  })

    
@app.route('/test-json', methods=['GET', 'POST'])
def test_json():
  json = request.get_json()      
  return flask.jsonify({
    'success': True,
    'data': {
      'json': json,
    }
  })

#
# Firebase
#
@app.route('/training/datasets', methods=['GET'])
def datasets_list():
  result = v_firebase.datasets.get_all()
  return flask.jsonify({
     'data': result
  })


if __name__=='__main__':
   app.run(debug=True)