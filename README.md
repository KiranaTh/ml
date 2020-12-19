# ml
## To install 
Create a project folder and a venv folder:
`$ python3 -m venv venv`
On Windows:
`> \Python27\Scripts\virtualenv.exe venv`

## Activate the environment
Activate the corresponding environment:
`$ . venv/bin/activate`
On Windows:
`> venv\Scripts\activate`

## Install Flask
Within the activated environment, use the following command to install Flask:
`$ pip install Flask`

## Install requirements.txt
install on the same relative path of requirements.txt file
`$ pip install -r requirements.txt`

## Install setup.py
install setup file
`$ cd app/
 $ python3 setup.py install`

## To test 
go to the relative path of vircade folder
`$ cd app/vircade/
 $ python3 __init__.py`

## To test firebase or model
go to the relative path of controllers folder
`$ cd app/vircade/controllers
 $ python3 v_firebase.py
 $ python3 v_model.py`

## References
Flask installation:
[link name](https://flask.palletsprojects.com/en/1.1.x/installation/)
