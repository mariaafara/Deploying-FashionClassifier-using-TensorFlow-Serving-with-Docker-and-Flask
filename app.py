from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap

import os
import model
# Create an instance of flask app
app = Flask(__name__, template_folder='Template')
# pass the app instance in the Bootstrap class for using the bootstrap functionalities in the html files.
Bootstrap(app)

"""
Routes
"""
# Add a default route to the index.html
# It accepts the GET and POST requests and saves the uploaded images in static folder
# Then it makes a call to the model.get_prediction function to get predictions and pass it to result.html.

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            class_name = model.get_prediction(image_path)
            result = {
                'class_name': class_name,
                'image_path': image_path,
            }
            return render_template('result.html', result = result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
