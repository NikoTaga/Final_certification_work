from flask import Flask, render_template, request

# from process import calc_cost


app = Flask(__name__)

@app.route('/', methods=["get", "post"])  
def index():
    message = ""
    if request.method == "POST":
        area = request.form.get("area")
        # cost = calc_cost(area)
        # message = f"Стоимость недвижимости площадью {area} кв. м. равна {cost} рублей."
        message = f"информация из ввода тт {area}."

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)

