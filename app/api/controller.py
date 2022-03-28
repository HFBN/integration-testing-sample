import os
import pickle
import numpy as np

import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("info.log"),
        logging.StreamHandler()
    ]
)

# Import flask and accompanying functionality
from flask import Blueprint, request, jsonify

# Set paths
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pipeline_path = os.path.join(base_path, 'models/pipeline.pkl')

# Load pipeline from binary
with open(pipeline_path, 'rb') as f:
    pipeline = pickle.load(f)

# Instantiate Blueprint
prediction_app = Blueprint('prediction_app', __name__)

# Define health endpoint
@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        return "I'm okay!"

# Define prediction endpoint
@prediction_app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get the data from the incoming request.
            json_data = request.get_json()
            logging.info(f'Received POST request with payload: {json_data}.')
            features = json_data['features']
            features = np.array(features).reshape(1, -1)
            logging.info(f'Extracted features: {features}.')
            # Make prediction
            prediction = pipeline.predict(features)
            prediction = int(prediction[0])
            logging.info(f'Made prediction {prediction}.')
            # Return / send back the result formatted in json.
            response = {'result': f'{prediction}'}
            logging.info(f'Sending response with payload: {response}.')
            return jsonify(response)
        except Exception as e:
            logging.warning(e)
            return jsonify({'error': f'{e}'})

