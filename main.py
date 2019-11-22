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
    question = "Find the count of each street surface type (concrete,macadam,etc) for every Electoral division (Ward-DED)"
    with open('sparql/1.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/1', query=query)

@app.route("/query/2")
def query_two():
    question = "How many bins are present on each street class type (local road, national primary, etc.)?"
    with open('sparql/2.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/2', query=query)

@app.route("/query/3")
def query_three():
    question = "Where the damaged bins are located along with the surface type of the corresponding street?"
    with open('sparql/3.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/3', query=query)

@app.route("/query/4")
def query_four():
    question = "How many roads were built in each Dublin City Council (DCC) area over past 5 years?"
    with open('sparql/4.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/4', query=query)

@app.route("/query/5")
def query_five():
    question = "Find the count of each street type for every Electoral division (Ward-DED)"
    with open('sparql/5.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/5', query=query)

@app.route("/query/6")
def query_six():
    question = "Calculate the bin density on each street. Formula used = No of bins/ Line Lenght of the street"
    with open('sparql/6.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/6', query=query)

@app.route("/query/7")
def query_seven():
    question = "How many bins are available for advertisement on a particular street surface type?"
    with open('sparql/7.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/7', query=query)

@app.route("/query/8")
def query_eight():
    question = "How many bins are present in each DCC area?"
    with open('sparql/8.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/8', query=query)


@app.route("/query/9")
def query_nine():
    question = "Which city centre streets were built in and before 2000 and compute the total number of bins present on them?"
    with open('sparql/9.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/9', query=query)

@app.route("/query/10")
def query_ten():
    question = "Where the damaged bins are located along with the surface type of the corresponding street?"
    with open('sparql/10.txt','r') as queryData:
        query = str(queryData.read())
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

    return render_template("index.html", results=results, question=question, path='/query/10', query=query)


if __name__ == "__main__":  # on running python app.py
    app.run()  # run the flask app
