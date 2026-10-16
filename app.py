import os
from flask import Flask, render_template

base_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, 
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Pentru rulare locală de test
    app.run(debug=True)