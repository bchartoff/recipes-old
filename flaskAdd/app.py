# from flask import render_template, Flask, url_for

# app = Flask(__name__)

# @app.route('/hello')
# def hello(name=None):
# 	url_for('static', filename='testTags.js')
# 	return render_template('search.html')


import csv
from flask import Flask, jsonify, render_template, request
from os import remove, rename
app = Flask(__name__)

@app.route('/add')
def build_ingredient():
    amount = request.args.get('amount', '', type=str)
    unit = request.args.get('unit', '', type=str)
    subingredient = request.args.get('subingredient', '', type=str)
    def parseAmount(amount):
		if(amount.find("/") == -1):
			return float(amount)
		else:
			nom = float(amount.split("/")[0])
			denom = float(amount.split("/")[1])
			return nom/denom

    return jsonify(amount=parseAmount(amount), unit=unit, subingredient=subingredient, result=amount + " " + unit + " " + subingredient)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_ingredient')
def new_ingredient():
    return render_template('new_ingredient.html')

@app.route('/add_new_ingredient')
def add_new_ingredient():
    category = request.args.get('category', '', type=str)
    ingredient = request.args.get('ingredient', '', type=str)
    subingredient = request.args.get('subingredient', '', type=str)
    # cr = csv.reader(open("static/ingredients.csv", 'rU'))
    # cw = csv.writer(open("static/ingredients.csv.tmp",'wb'))
    # rowNum = 0
    # for row in cr:
    #     if(rowNum == 0):
    #         categories = row
    #         if category not in categories:
    #             categories.append(category)
    #         cw.writerow(categories)
    #     if(rowNum == 1):
    #         ingredients = row
    #         if ingredient not in ingredients:
    #             ingredients.append(ingredient)
    #         cw.writerow(ingredients)
    #     if(rowNum == 2):
    #         subingredients = row
    #         if subingredient not in subingredients:
    #             subingredients.append(subingredient)
    #         cw.writerow(subingredients)
    #     rowNum+=1
    # remove("static/ingredients.csv")
    # rename("static/ingredients.csv.tmp", "static/ingredients.csv")
    print [category, ingredient, subingredient]
    cr = open('static/ingredients.csv','a')
    cr.write('\n' + category + "," + ingredient + "," + subingredient)
    cr.close()
    return jsonify(response="done")

    # return jsonify(amount=parseAmount(amount), unit=unit, ingredient=ingredient, result=amount + " " + unit + " " + ingredient)


if __name__ == '__main__':
    app.debug = True
    app.run()