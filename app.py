from flask import Flask, render_template, jsonify, request

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
def home_page():
  return render_template('home.html', jobs=JOBS)


@app.route('/job/<id>')
def show_jobs(id):
  # job = load_job_from_db(id)
  job = JOBS[id]

  if not job:
    return 'Not found', 404
  return render_template('jobpage.html', job=job)


#instead of returning data to render html
#this is used to create api end points
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

# @app.route('/job/<id>/apply', method="post")
# def apply_to_job(id):
#   # data = request.args what is the difference between request.form and request.args
#   data = request.form
#   return jsonify(data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
