from flask import Flask,request
from controllers import v_firebase, v_model
import json
import flask

app = Flask(__name__)

# Firebase
@app.route('/')
def working():
   return "This is working"

@app.route('/model/classify', methods=['GET', 'POST'])
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
  y_pred = v_model.predict(x, song)

  return flask.jsonify({
      "data": y_pred,
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
   app.run()