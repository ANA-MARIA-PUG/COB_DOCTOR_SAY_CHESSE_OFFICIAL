import os
from flask import Flask, render_template

# Inițializăm aplicația Flask (Flask caută automat folderul 'templates' și 'static')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
