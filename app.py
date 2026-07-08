from xhtml2pdf import pisa
from io import BytesIO
from flask import Flask, render_template,request,make_response

app = Flask(__name__)

data={}

@app.route("/",methods=['GET','POST'])
def home():
    global data
    if request.method=="GET":
        return render_template("index.html")
    elif request.method=="POST":
        data={
        "name":request.form['name'],
        "contact":request.form['Contact'],
        "education":request.form['Education'],
        "company":request.form['Company'],
        "job":request.form['work'],
        "skills":request.form['skills']
        }
        return render_template("letter.html",**data)
    else:
        return "Wrong Request"

@app.route("/download")
def download():

    html = render_template("letter.html", **data)

    pdf = BytesIO()
    pisa.CreatePDF(html, dest=pdf)

    response = make_response(pdf.getvalue())
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=Cover_Letter.pdf"

    return response

if __name__ == "__main__":
    app.run(debug=True)