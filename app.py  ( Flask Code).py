from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from utils import generate_password_from_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        img = request.files['image']
        if img:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(img.filename))
            img.save(filepath)
            password = generate_password_from_image(filepath)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)