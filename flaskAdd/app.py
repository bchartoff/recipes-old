# from flask import render_template, Flask, url_for

# app = Flask(__name__)

# @app.route('/hello')
# def hello(name=None):
# 	url_for('static', filename='testTags.js')
# 	return render_template('search.html')


import csv
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/add')
def build_ingredient():
    amount = request.args.get('amount', '', type=str)
    unit = request.args.get('unit', '', type=str)
    ingredient = request.args.get('ingredient', '', type=str)
    # cw = csv.writer(open("new.csv","wb"))
    # cw.writerow([amount,unit])
    def parseAmount(amount):
		if(amount.find("/") == -1):
			return float(amount)
		else:
			nom = float(amount.split("/")[0])
			denom = float(amount.split("/")[1])
			return nom/denom

    return jsonify(amount=parseAmount(amount), unit=unit, ingredient=ingredient, result=amount + " " + unit + " " + ingredient)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_ingredient')
def new_ingredient():
    return render_template('new_ingredient.html')

if __name__ == '__main__':
	app.run()
