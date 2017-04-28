from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route('/story', methods=['POST', 'GET'])
def save(story_id=None):
    if request.method == 'POST':
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
        return render_template("form.html", story_id=story_id)
    

@app.route('/list', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form.to_dict()
        print(result)
        result_list = []
        for key, value in result.items():
            if key == 'Story title':
                result_list.append(value)
            elif key == 'User Story':
                result_list.append(value)
        print(result_list)
        return render_template("list.html", result=result)


if __name__ == "__main__":
    app.run()

