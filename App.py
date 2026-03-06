from flask import *


App = Flask(__name__)


#below we create the home route
#routing is the process of mapping a URL to a function that will handle the request for that URL.
@App.route('/api/home')
def home():
    return jsonify ({"Message" : "Home route Accessed"})



@App.route('/api/products')
def products():
    return jsonify ({"Message" : "welcome to the products route"})

#below is a route for addition
@App.route("/api/calc", methods=["POST"])
def calculator():
    if request.method == "POST":
      number1 = (request.form["number1"]) 
      number2 = (request.form["number2"])

      sum = int(number1) + int(number2)
      
     
  
    return jsonify({"the answer is ": sum})




App.run(debug=True) 





     



App.run(debug=True)  