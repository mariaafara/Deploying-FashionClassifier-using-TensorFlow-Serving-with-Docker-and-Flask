# Deploying-FashionClassifier-using-TensorFlow-Serving-with-Docker-and-Flask
Deploy a pre-trained tensorflow classifier using TensorFlow Serving with Docker.
<br> Create a visual web interface using Flask web framework that will serve to get predictions from the served TensorFlow model and help end-users to consume through API calls. 

Execution Steps: 
  1.  Setup tensorflow serving server on localhost:
  
			sudo docker run -v $(pwd)/my_fashion_model:/models/fashion_model/1 -e MODEL_NAME=fashion_model -p 9501:8501 tensorflow/serving

  
  2.  Setup virtual environment and install necessary packages: 
  
          Conda create –n fashion-classification-env python=3.8
		    Conda activate fashion-classification-env
	      pip install flask
	      pip install tensorflow
	      pip install pillow
	  
  3.  Run flask app with: Python app.py 
  4.  Access the app by going to http://127.0.0.1:5000/ in your browser
	