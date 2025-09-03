# Cama-bg-remover

A web app for removing background images from images. Built with flask and bootstrap.

# [Cama-bg-remover](https://cama-bg-remover.vercel.app/)

> Download the code 

```bash
$ git clone https://github.com/zayinhd/cama-bg-remover.git
$ cd cama-bg-remover
```

<br />

### 👉 Set Up

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .venv\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```
$ # CMD 
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
$
$ # Powershell
$ $env:FLASK_APP = ".\app.py"
$ $env:FLASK_ENV = "development"
```

<br />

> Start the app

```bash
$ flask run
// OR
$ flask run --cert=adhoc # For HTTPS server
//OR
$ py app.py
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

Make sure to give this repo a Star ⭐
