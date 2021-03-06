# Boston Housing Price Prediction 

This is a simple Machine Learning Model that helps predict housing prices in Boston. Its written using scikit learn and pickled using Flask for use in a production system via an API endpoint. 

The Model is not accurate and thus should not be used in any production systems. The focus of this codebase is to be able to pickle the model onto a REST API. 

## Installation and Running 

This documentation assumes an understanding of Python Programming Language and the use of a *nix system. It also assumes you have installed `virtualenv`. 

Clone the repository and run the following commands to get you up and running 

` pip install -r requirements.txt` 

Run the Jupyter Notebook using the following command 

` jupter notebook` 

Run the API using the following command. You can specify another port apart from `8080`

`gunicorn --bind 0.0.0.0:8080 wsgi:application -w 1` 

## Getting Predictions 

To get predictions, make sure you are running the API using the above gunicorn command. You can use the following curl command to get predictions. Feel free to adjust the input 

`curl -X GET http://0.0.0.0:8080/predict -H "Content-Type: application/json" -d '{"input":"7"}' `