# ml
### To install 
---
Create a project folder and a venv folder:<br />
`$ python3 -m venv venv`<br />
On Windows:<br />
`> \Python27\Scripts\virtualenv.exe venv`<br />

### Activate the environment
---
Activate the corresponding environment: <br />
`$ . venv/bin/activate`<br />
On Windows:<br />
`> venv\Scripts\activate`

### Install Flask
---
Within the activated environment, use the following command to install Flask: <br />
`$ pip install Flask`

### Install requirements.txt
---
install on the same relative path of requirements.txt file <br />
`$ pip install -r requirements.txt`

### Install setup.py
---
install setup file <br />
```$ cd app/ <br />
 $ python3 setup.py install
```

### To test 
---
go to the relative path of vircade folder <br />
```$ cd app/vircade/
 $ python3 __init__.py
```

### To test firebase or model
---
go to the relative path of controllers folder<br />
```$ cd app/vircade/controllers
 $ python3 v_firebase.py
 $ python3 v_model.py
```

### References
---
Flask installation: <br />
[link name](https://flask.palletsprojects.com/en/1.1.x/installation/)
