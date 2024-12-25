from flask import Flask, render_template, request, send_file
from rembg import remove
import base64
import io

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['image']
    if uploaded_file.filename != '':
        input_image = uploaded_file.read()
        output_image = remove(input_image)

    global encoded_modified
    encoded_original = base64.b64encode(input_image).decode('utf-8')
    encoded_modified = base64.b64encode(output_image).decode('utf-8')
    return render_template("index.html", original_image=f'data:image/png;base64,{encoded_original}', modified_image=f'data:image/png;base64,{encoded_modified}')


@app.route('/upload/download')
def download():
    decoded_image = base64.b64decode(encoded_modified)

    image_io = io.BytesIO(decoded_image)

    return send_file(
        image_io, mimetype='image/png', as_attachment=True, download_name='cama-bg-remover.png')


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=False)
