from flask import Flask
# from flask import routes
from flask import render_template

app = Flask(__name__)

# from app import routes

@app.route('/')
def index():
  # render_template()
  return render_template('0-index.html')

if __name__ == '__main__':
  app.run()
