import os
from urllib import request
import flask
from flask import render_template, request, redirect, url_for
import encryption
from werkzeug.utils import secure_filename
import img_converter as ic

UPLOAD_FOLDER = "static//client//img"
ALLOWED_EXTENSIONS = {'png', 'jpg'}


app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Funzione presa dal sito ufficiale di flask che serve a controllare se il file ha una delle estensioni permesse
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/codifica", methods=['GET', 'POST'])
def codifica():
    if request.method == 'POST':
        string = None
        string = request.form['stringtocode']
        # Prendo l'immagine dal form e la salvo in una cartella
        file = request.files.get('imgkey', '')
        # Try catch che serve per scrivere un messaggio di errore quando viene caricato un file diverso da .png e .jpg
        try:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(f"static\client\img\{filename}")
            # Trasformo l'immagine in un immagine ascii
            ascii_image = ic.img_to_ascii(f"static\client\img\{filename}", 100)
            coded_string = encryption.crypt(string, ascii_image)
            # Cancello dal server l'immagine usata per la crittografia
            os.remove(f"static\client\img\{filename}")
            return render_template('codifica.html', coded_string = coded_string)
        except:
            pass
        return render_template('codifica.html', insuccess = True)
    else:
        string = None
        return render_template('codifica.html')

@app.route("/decodifica", methods=["GET", "POST"])
def decodifica():
    if request.method == "POST":
        string = None
        string = request.form['stringtodecode']
        # Prendo l'immagine dal form e la salvo in una cartella
        file = request.files.get('imgkey', '')
        # Try catch che serve per scrivere un messaggio di errore quando viene caricato un file diverso da .png e .jpg
        try:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(f"static\client\img\{filename}")
            # Trasformo l'immagine in un immagine ascii
            ascii_image = ic.img_to_ascii(f"static\client\img\{filename}", 100)
            decoded_string = encryption.decrypt(string, ascii_image)
            # Cancello dal server l'immagine usata per la crittografia
            os.remove(f"static\client\img\{filename}")
            return render_template('decodifica.html', decoded_string = decoded_string)
        except:
            pass
        return render_template('decodifica.html', insuccess = True)
    else:
        string = None
        return render_template('decodifica.html')
