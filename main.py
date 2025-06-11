from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return """
  <html>
  <body>
    <form action="/submit" method="post">
      Enter your name: <input type="text" name="name">
      <input type="submit" value="Submit">
    </form>
  </body>
  </html>
  """
  
@app.route("/submit", methods=["POST"])
def submit():
    user_input = request.form["name"]
    return f"Hello, {user_input}! Welcome to our FastAPI application."
  
  
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)