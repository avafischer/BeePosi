from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def Hello_World():
    return render_template("Index.html")



@app.route("/information")
def information():
    return render_template("Information.html")
    
@app.route("/quizgrade", methods=["POST", "GET"])
def quiz():
    Q1 = request.form["q1"]
    Q2 = request.form["q2"]
    Q3 = request.form["q3"]
    Q4 = request.form["q4"]
    Q5 = request.form["q5"]
    Q6 = request.form["q6"]
    Q7 = request.form["q7"]
    Q8 = request.form["q8"]
    Q9 = request.form["q9"]
    Q10 = request.form["q10"]
    Q11= request.form["q11"]
    Q12= request.form["q12"]
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
    display = "your score is " + str(score) + "/12"
    return display

@app.route("/quiz")
def quizload():
    return render_template("quiz.html")

if __name__ == "__main__":
    app.run()