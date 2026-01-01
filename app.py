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

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    return render_template("signup.html")

                
if __name__=="__main__":
    app.run(debug=True)