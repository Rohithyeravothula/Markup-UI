from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return render_template("index.html")


@app.route('/document', methods=['GET'])
def get_document():
	docId = request.args.get("id")
	return "document with id " + docId


@app.route('/documents', methods=['GET'])
def list_documents():
	return "documents list is shown here"


@app.route('/document/', methods=['POST'])
def add_markup():
	content = request.get_json()
	markup = content["markup"]
	return "ack"

@app.route('/documents/annotations', methods=['POST', 'GET'])
def dummy():
	if request.method == 'POST':
		content = request.get_json()
		print(content)
		return ""
	elif request.method == 'GET':
		return ""

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8000, debug=True)