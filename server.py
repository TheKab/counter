from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key="secret"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
@app.route('/counter')
def counter():
    if "visits" in session:
        session ["visits"] += 1
    else:
        session["visits"] = 1
    return render_template("index.html")


@app.route('/destory_session')
def destory_session():
    session.clear()
    return redirect("/counter")



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.