import os
from flask import Flask, render_template

# Determinăm calea absolută către folderul curent
base_dir = os.path.dirname(os.path.abspath(__file__))

# Căutăm folderul indiferent dacă e scris cu litere mari sau mici
template_dir = os.path.join(base_dir, 'templates')
if not os.path.exists(template_dir):
    template_dir = os.path.join(base_dir, 'TEMPLATES')

static_dir = os.path.join(base_dir, 'static')
if not os.path.exists(static_dir):
    static_dir = os.path.join(base_dir, 'STATIC')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
