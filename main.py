from flask import Flask, render_template
from SPARQLWrapper import SPARQLWrapper, JSON

app = Flask(__name__)

sparql = SPARQLWrapper("http://localhost:8890/sparql")


@app.route("/")
def editor():
    results = []
    return render_template("editor.html", results=results, path='/')


@app.route("/query/1")
def query_one():
    question = "Surface of road types Electoral division (DED)wise"
    with open('sparql/1.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/1', query=query)

@app.route("/query/2")
def query_two():
    question = "How many dustbins corresponds to which street class code"
    with open('sparql/2.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/2', query=query)

@app.route("/query/3")
def query_three():
    question = "Bins damaged with street name and street type"
    with open('sparql/3.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/3', query=query)

@app.route("/query/4")
def query_four():
    question = "No of roads built in a particular electoral division (DED) in last 5 years"
    with open('sparql/4.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/4', query=query)

@app.route("/query/5")
def query_five():
    question = "Street types Electoral division (DED)wise"
    with open('sparql/5.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/5', query=query)

@app.route("/query/6")
def query_six():
    question = "Bin Density on roads per 100m "
    with open('sparql/6.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/6', query=query)

@app.route("/query/7")
def query_seven():
    question = "Bins available for advertisement on a particular street surface type"
    with open('sparql/7.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/7', query=query)


if __name__ == "__main__":  # on running python app.py
    app.run()  # run the flask app
