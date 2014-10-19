from flask import Flask
import json
import subprocess

app = Flask(__name__)

# Open Config
config_file = open("repos.json")
config = json.load(config_file)
config_file.close()


@app.route("/test/")
def hello_world():
    return "Yep.  We are up."


@app.route("/", methods=['POST'])
def hook_endpoint(request, user, repo):
	blob = request.get_json()
	if blob["ref"] != "refs/heads/master":
		return "No a change to master branch.  Exiting."
	repo = blob["repository"]["full_name"]
	target = config[repo]
	subprocess.call([target])


if __name__ == '__main__':
	app.run(debug=True)
