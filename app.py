from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/basic", methods=["POST", "GET"])
def basic():
    result=None
        
    if request.method=="POST":
        try:
            
            num1=float(request.form.get("num1"))
            num2=float(request.form.get("num2"))
            operation=request.form.get("operation")

            if operation=="add":
                result=num1+num2
            elif operation=="sub":
                result=num1-num2
            elif operation=="mul":
                result=num1*num2
            elif operation=="div":
                result=num1/num2 if num2!=0 else "Cannot divide by Zero"
            elif operation=="remainder":
                result=num1%num2
            elif operation=="floor_division":
                result=num1//num2
        
        except ValueError:
            result="Invalid Input"

    return render_template("basic_calc.html", result=result)

#Finance Calculator





def simple_interest(p, r, t):
    return (p*r*t)/100

def compound_interest(p, r, t, n):
    amount = p * (1 + r / (100 * n )) ** (n * t)
    return amount - p

def emi_calculator(p, r, t):
    r = r / (12 * 100)
    t = t * 12
    emi = (p * r * (1+r)**t) / ((1 + r) ** t - 1)
    return emi

#Finance Route



@app.route("/finance", methods=["GET", "POST"])
def finance():
    result=None
    calc_type=None

    if request.method == "POST":
        calc_type =  request.form.get("calc_type")

        if calc_type == "si":
            p = float(request.form["principal"])
            r = float(request.form["rate"])
            t = float(request.form["time"])
            result = simple_interest(p, r, t)

        elif calc_type == "ci":
            p = float(request.form["principal"])
            r = float(request.form["rate"])
            t = float(request.form["time"])
            n = int(request.form["n"])
            result = compound_interest(p, r, t, n)

        elif calc_type == "emi":
            p = float(request.form["principal"])
            r = float(request.form["rate"])
            t = float(request.form["time"])
            result = round(emi_calculator(p, r, t), 2)

    return render_template("finance.html", result=result, calc_type=calc_type)

#Health Calculator



def bmi_calculator(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def bmr_calculator(weight, height, age, gender):
    if gender == "male":
        return round(10 * weight + 6.25 * height - 5 * age + 5, 2)
    else:
        return round(10 * weight + 6.25 * height - 5 * age - 161, 2)
    

@app.route("/health", methods=["GET", "POST"])
def health():
    result = None
    category = None
    calc_type = None

    if request.method == "POST":
        calc_type = request.form.get("calc_type")

        if calc_type == "bmi":
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            result = bmi_calculator(weight, height)
            category = bmi_category(result)

        elif calc_type == "bmr":
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            age = int(request.form["age"])
            gender = request.form["gender"]
            result = bmr_calculator(weight, height, age, gender)

    return render_template("health.html", result=result, category=category, calc_type=calc_type)


@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    return render_template("signup.html")

                
if __name__=="__main__":
    app.run(debug=True)