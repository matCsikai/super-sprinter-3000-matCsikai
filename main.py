from flask import Flask, render_template, request
import csv
import common
app = Flask(__name__)


@app.route('/story')
@app.route('/story/<int:story_id>', methods=['GET', 'POST'])
def story(story_id=None):
    database_as_list = common.data_list_with_id()
    # opens empty add story form template
    if story_id is None:
        return render_template("form.html", story_id=story_id)
    else:
        for data_list in database_as_list:
            # open story form template to edit
            if story_id == data_list[0]:
                data_for_edit = data_list
                return render_template("form.html", story_id=story_id, data_for_edit=data_for_edit)
            # return to list template if ID not exist
            elif story_id != data_list[0] and story_id <= len(database_as_list):
                continue
            else:
                return render_template("list.html")


@app.route('/list', methods=['GET', 'POST'])
def list_manager():
    # adds story input to data.csv
    database_as_list = common.data_list_with_id()
    if request.method == 'POST':
        story_title = request.form["Story title"]
        user_story = request.form["User Story"]
        acceptance_criteria = request.form["Acceptance criteria"]
        business_value = request.form["Business Value"]
        estimation = request.form["Estimation"]
        status = request.form["Status"]
        fieldnames = ["Story title", "User Story", "Acceptance criteria", "Business Value", "Estimation", "Status"]
        with open("data.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({"Story title": story_title, "User Story": user_story, "Acceptance criteria":
                            acceptance_criteria, "Business Value": business_value, "Estimation": estimation,
                            "Status": status})
        return render_template("list.html", database_as_list=database_as_list)
    # sends data with IDs to list template
    else:
        return render_template("list.html", database_as_list=database_as_list)


if __name__ == "__main__":
    app.run(debug=True)
