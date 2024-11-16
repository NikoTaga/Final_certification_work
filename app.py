from flask import Flask, render_template, request
from data_processing import process


app = Flask(__name__)

@app.route('/', methods=["get", "post"])  
def index():
    message = ""
    par1 = 2
    if request.method == "POST":
        area = request.form.get("area")
        res = process(area, par1)
        message = f"входной параметр {area}, параметр после обработки {res}  ."

    return render_template("index.html", message=message)


app.run()

# if __name__ == "__main__":
#     app.run(debug=True)

