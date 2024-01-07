from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Social media strategist',
    'location': 'Remote',
    'salary': '25k',
}, {
    'id': 2,
    'title': 'frontend engineer',
    'location': 'Remote',
    'salary': '25k',
}, {
    'id': 3,
    'title': 'fullstack engineer',
    'location': 'Remote',
    'salary': '25k',
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)

#instead of returning data to render html
#this is used to create api end points
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
