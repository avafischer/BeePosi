from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def Hello_World():
    return render_template("Index.html")



@app.route("/information")
def information():
    return render_template("Information.html")
    
@app.route("/quiz", methods=["POST", "GET"])
def quiz():
    Q1 = request.form["Q1"]
    Q2 = request.form["Q2"]
    Q3 = request.form["Q3"]
    Q4 = request.form["Q4"]
    Q5 = request.form["Q5"]
    Q6 = request.form["Q6"]
    Q7 = request.form["Q7"]
    Q8 = request.form["Q8"]
    Q9 = request.form["Q9"]
    Q10 = request.form["Q10"]
    Q11= request.form["Q11"]
    Q12= request.form["Q12"]
    score = 0
    if Q1 == "myelin":
        score = score+1
    if Q2 == "addiction":
        score = score+1
    if Q3 == "drugs and gambling":
        score = score+1
    if Q4 == "screen use":
        score = score+1
    if Q5 == "phone" or Q5 == "dopamine":
        score = score+1
    if Q6 == "teenage":
        score = score+1
    if Q7 == "neurotransmitters":
        score = score+1
    if Q8 == "prefrontal cortex":
        score = score+1
    if Q9 == "prefrontal cortex":
        score = score+1
    if Q10 == "prefrontal cortex":
        score = score+1
    if Q11 == "willpower":
        score = score+1
    if Q12 == "developing":
        score = score+1
    display = "your score is " + str(score) + "/3"
    return display

@app.route("/quizload")
def quizload():
    return render_template("quiz.html")

if __name__ == "__main__":
    app.run()