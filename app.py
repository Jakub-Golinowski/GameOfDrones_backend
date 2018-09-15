# import dependencies
import os
from flask import Flask
import urllib.request
import json
import json_parser as jp

# bootstrap the app
app = Flask(__name__)

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))

# our base route which just returns a string
@app.route('/')
def hello_world():
    hello_world_bytes = b'Game Of Drones backend homepage.'
    return hello_world_bytes

@app.route('/mirror_recorded')
def mirror_recorded():
    contents = urllib.request.urlopen("https://hackzurich.involi.live/http_recorded/").read()
    return contents

@app.route('/map_2d')
def map_2d():
    involi_bytes = urllib.request.urlopen("https://hackzurich.involi.live/http_recorded/").read()
    involi_dict = json.loads(involi_bytes.decode("utf8"))
    print("type(contents_json) = " + str(type(involi_dict)))
    json_parser = jp.JSON_Parser()
    parsed_dict = json_parser.parse_for_map_2d(involi_dict, json_parser.mock_drone_dict)
    return json.dumps(parsed_dict)

# start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
