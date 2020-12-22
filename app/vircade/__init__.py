from flask import Flask,request
import json
import flask
import numpy as np
import tensorflow as tf
import keras
from os import path
from scipy import stats
from waitress import serve
from firebase import firebase
import time

# init
firebase = firebase.FirebaseApplication('https://vircade-4c1d4.firebaseio.com/', authentication=None)
MODEL_PATH = './model/model.h5'

app = Flask(__name__)

@app.route('/')
def working():
   return "This is working"

@app.route('/model/classify', methods=['POST', 'PUT'])
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

  y_pred = predict(x, song)
  print("y_pred: "+str(y_pred))
  send_json = {"gameID": gameID, "userId": userId, "y_pred": y_pred}
  result = update(send_json["gameID"],send_json["userId"],send_json["y_pred"])
  print("result: "+result)
  time.sleep(5)
  return flask.jsonify({
      "data": y_pred,
      "put": result
  })

def predict(x, s):
    song = s
    songs = ['We Are One','All The Same','Alive','Treasure']
    indx = songs.index(song)
    model = keras.models.load_model(MODEL_PATH)
    y_pred = model.predict(np.array(x))
    result = (max(y_pred.tolist()))[indx]
    result = "{:.2f}".format(result)
    return float(result)*int(100)

def update(gameID, userId, score):
        print(gameID)
        print(userId)
        print(score)
        res = firebase.put('/games/'+gameID+'/'+userId, 'score', score)
        result = '/games/'+gameID+'/'+userId+'/score/'+str(score)
        return result

#test    
@app.route('/test-params', methods=['GET', 'POST'])
def test_params():
  json = request.get_json()
  form_data = request.form    # body (form data)
  params = request.args       # args (in url)
  return flask.jsonify({
    'success': True,
    'data': {
      'json': json,
      'form_data': form_data,
      'params': params,
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
   serve(app.vercade, host='0.0.0.0', port=8000 ,debug=True)

