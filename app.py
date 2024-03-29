# import dependencies
import os
from flask import Flask, render_template
from flask import request
import urllib.request
import json

import json_parser as jp
import server_state as ss
import involi_worker as wf

# bootstrap the app
app = Flask(__name__)

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))
server_state = ss.ServerState()

# Start the involi websocket to receive involi traffic updates with low latency.
involi_worker = wf.InvoliWorker()
involi_worker.start()

# our base route which just returns a string
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/post_drone_position', methods=['POST', 'GET', 'PUT'])
def post_drone_position():
    if request.method == 'POST':
        #TODO validate the format of the POST
        server_state.update_drone(json.loads(request.data))
        return 'OK'
    elif request.method == 'PUT':
        server_state.update_drone(json.loads(request.data))
        return 'OK'
    else:
        # the code below is executed if the request method
        # was GET or the credentials were invalid
        return 'Use this URL for the post request. For example you can use the following command: curl --header "Content-Type: application/json" --request POST --data \'{ "icao": "FA4548", "lat": 46.530834474, "lon": 6.2578792135, "alt": 9753, "speed": 236.129796, "heading": -51.76, "last_update": "2018-09-14T22:42:25.898475+00:00" }\' http://0.0.0.0:3000/post_drone_position'

@app.route('/post_drone_delete', methods=['POST', 'GET', 'PUT'])
def delete_drone():
    if request.method == 'POST' or request.method == 'PUTs':
        ret_status = server_state.try_drone_delete_by_icao(request.data.decode("utf8"))
        return ret_status
    else:
        return 'Use this URL for the deleting the drone by its icao. For example you can use the following command: curl --header "Content-Type: application/json" --request POST --data \'FA4548\' http://0.0.0.0:3000/post_drone_delete'


@app.route('/full_data')
def full_data():
    return server_state.dump_data_dict_to_json(wf.current_request)


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
