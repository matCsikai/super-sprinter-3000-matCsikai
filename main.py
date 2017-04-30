from flask import Flask, render_template, request
import csv
import common
app = Flask(__name__)


@app.route('/story')
@app.route('/story/<int:story_id>', methods=['GET', 'POST'])
def story(story_id=None):
    database_as_list = common.data_list_with_id()
    if story_id is None:
        return render_template("form.html", story_id=story_id)
    else:
        for data_row in database_as_list:
            if story_id == data_row[0]:
                data_for_edit = data_row
                return render_template("form.html", story_id=story_id, data_for_edit=data_for_edit)
            else:
                return render_template("list.html", database_as_list=database_as_list)
            
        


@app.route('/list', methods=['GET', 'POST'])
def add_to_data_file():
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
        database_as_list = common.data_list_with_id()
        return render_template("list.html", database_as_list=database_as_list)




if __name__ == "__main__":
    app.run(debug=True)
