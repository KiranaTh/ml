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
#   json = request.get_json()
#   x = json['x']
#   n = len(x)

#   # equal-width sampling
#   REQUIRED_N = 120     # TODO: don't hard code this
#   step = (n-1) / (REQUIRED_N-1)
#   decimal_i = 0

#   indexes = []
#   sampled_x = []
#   while len(indexes) < REQUIRED_N:
#     i = int(decimal_i)
#     indexes.append(i)
#     sampled_x.append(x[i])
#     decimal_i += step

#   y = v_models.predict(x)
#   sampled_y = v_models.predict(sampled_x)
#   return flask.jsonify({
#     'success': True,
#     'data': {
#       'raw': {
#         'input-size': n,
#         'result': y,
#       },
    #   'sampled': {
    #     'input-size': len(indexes),
    #     'result': sampled_y,
    #   }
#     },
#   })
  result = v_firebase.datasets.get_all()
  ml = []
  for i in range(0, len(result)):
      x = result[i].get('ml')
      print(x)
      n = len(result[i].get('ml'))
      y = v_model.predict(x)
  return flask.jsonify({
    'success': True,
    'data': {
      'raw': {
        'input-size': n,
        'result': y,
      },}})

@app.route('/model/input-shape', methods=['GET'])
def input_shape():
  input_shape = v_models.get_input_shape()
  return flask.jsonify({
    'success': True,
    'data': input_shape,
  })
    
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

# @app.route('/training/datasets', methods=['POST'])
# def datasets_new():
#   form_data = request.form
#   result = v_firebase.datasets.new(form_data['name'])
#   return flask.jsonify({
#     'success': True,
#     'data': result
#   })

if __name__=='__main__':
   app.run()