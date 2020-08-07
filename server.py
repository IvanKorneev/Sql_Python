from flask import Flask, render_template, request, jsonify
from sqler import SQLer
app = Flask(__name__)
sqler = SQLer()

@app.route('/')
def root():
    return render_template('index.html')


@app.route("/json", methods=['POST'])
def serve_json():
    try:
        result = {}
        result = sqler.execute_sql(request.values['query'])
        
    except Exception as e:
        print(e)
        return jsonify({"employees":[{"Error": e}]})
    else:
        pass
        # print(f"SQL:\n{request.values['query']}\nexecuted well.")
    finally:
        return jsonify({"employees":result})


if __name__ == "__main__":
    app.run("localhost", port=3000, debug=True)


