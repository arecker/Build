from flask import Flask, request
import json
import subprocess
import os

app = Flask(__name__)
app.debug=True
pwd = os.path.dirname(os.path.realpath(__file__))

# Open Config
config_file = open(os.path.join(pwd, "repos.json"))
config = json.load(config_file)
config_file.close()


@app.route("/test/")
def hello_world():
    return "Yep.  We are up."


@app.route("/", methods=['POST'])
def hook_endpoint():
	blob = request.get_json()
	if blob["ref"] != "refs/heads/master":
		return "No a change to master branch.  Exiting."
	repo = blob["repository"]["full_name"]
	target = config[repo]
	exit_code = subprocess.call([target])
        if exit_code is 0:
            return "OK"
        else:
            return "Oops: " + str(exit_code)

if __name__ == '__main__':
	app.run(debug=True)
