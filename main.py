from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/story')
@app.route('/story/<story_id>')
def story(story_id=None):
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

