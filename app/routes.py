from flask import render_template, request
from app import app
from app.predictor import predict_focus_score
from app.datahandler import save_user_log
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    message = ""
    if request.method == "POST":
        sleep = float(request.form["sleep"])
        study = float(request.form["study"])
        mood = float(request.form["mood"])
        screen = float(request.form["screen"])
        prediction = predict_focus_score(sleep, study, mood, screen)
        save_user_log(sleep, study, mood, screen, prediction)
        if prediction >= 8:
            message = "Goood Job. You're highly focused!"
        elif prediction >= 5:
            message = "Average focus.Try tweaking your routine."
        else:
            message = "You have low focus.Try more sleep & better mood."

    return render_template("index.html", prediction=prediction, message=message)
