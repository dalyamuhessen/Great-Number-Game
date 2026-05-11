from flask import Flask , render_template ,request,session,redirect
import random
app=Flask(__name__)
app.secret_key="great_number"
MAX_ATTEMPTS=5
@app.route("/")
def index():
    session["secret_number"]=random.randint(1,100)
    session["attempts"]=0
    session["game_over"]=False
    session["won"]=False
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    if session["game_over"]:
        return redirect("/")
    user_input=request.form["guess"]
    if not user_input.isdigit():
        return render_template("index.html",error="Enter a valid number.",attempts=session["attempts"])
    user_guess=int(user_input)
    secret=session["secret_number"]
    session["attempts"]=session["attempts"]+1
    attempts=session["attempts"]
    remaining=MAX_ATTEMPTS-attempts
    if user_guess < secret:
        result="low"
        message="Too Low!"
    elif user_guess>secret:
        result="high"
        message="Too high!"
    else:
        result="correct"
        message=f"{secret} was the number!"
        session["game_over"]=True
        return render_template("index.html", result=result, message=message,
                               attempts=attempts, secret=secret, game_over=True, won=True)
    
    if attempts>=MAX_ATTEMPTS:
        session["game_over"]=True
        session["won"]=False
        return render_template("index.html", result="lose", message=f"You lose! The number was {secret}.",
                               attempts=attempts, secret=secret, game_over=True, won=False)
    

    return render_template("index.html", result=result, message=message,
                           attempts=attempts, remaining=remaining, guess=user_guess)
 
if __name__ == "__main__":
    app.run(debug=True,port=5001)