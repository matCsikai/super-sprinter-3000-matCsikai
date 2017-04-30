from flask import Flask, render_template, request
import csv
import trial
app = Flask(__name__)


@app.route('/story')
@app.route('/story/<int:story_id>')
def story(story_id=None):
    return render_template("form.html", story_id=story_id)
    

@app.route('/list', methods=['POST', 'GET'])
def add_to_data_file():
    story_title = request.form["Story title"]
    user_story = request.form["User Story"]
    acceptanc_criteria = request.form["Acceptance criteria"]
    business_value = request.form["Business Value"]
    estimation = request.form["Estimation"]
    status = request.form["Status"]
    fieldnames = ["Story title", "User Story", "Acceptance criteria", "Business Value", "Estimation", "Status"]
    with open("data.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({"Story title": story_title, "User Story": user_story, "Acceptance criteria":
                        acceptanc_criteria, "Business Value": business_value, "Estimation": estimation,
                        "Status": status})
    database_as_list = trial.data_list_with_id()
    return render_template("list.html", database_as_list=database_as_list) # needs revision




if __name__ == "__main__":
    app.run(debug=True)
