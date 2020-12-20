from flask import Flask,request
from controllers import v_firebase, v_model
# from .controllers.v_firebase import datasets
# from .controllers.v_model import loadModel, predict
import json
import flask
import numpy as np
import tensorflow as tf
import keras
from os import path
from scipy import stats

from firebase import firebase

# init
firebase = firebase.FirebaseApplication('https://vircade-4c1d4.firebaseio.com/', authentication=None)
MODEL_PATH = '../../model/model.h5'

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
  result = update(send_json["gameID"],send_json["userId"],send_json["y_pred"])


  return flask.jsonify({
      "data": y_pred,
      "put": result
  })

def predict(x, s):
    song = s
    songs = ['Cha Cha Slide', 'Laxed Siren Beat Loop', 'Like That', 'Lose Control', 'Plain Jain', 'Treasure']
    indx = songs.index(song)
    model = keras.models.load_model(MODEL_PATH)
    y_pred = model.predict(np.array(x))
    result = (max(y_pred.tolist()))[indx]
    result = "{:.2f}".format(result)
    return float(result)*int(100)

def update(gameID, userId, score):
        res = firebase.put('/test/'+gameID+'/'+userId, 'score', score)
        result = '/games/'+gameID+'/'+userId
        return result

    
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

