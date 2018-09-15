import json_parser as jp
import data_entry as de
import urllib.request
import json
import arrow

class ServerState:
    def __init__(self):
        self.data_dict = {}
        self.map_2d_data_dict = {}
        self.jp = jp.JSON_Parser()

    def update_involi(self):
        involi_bytes = urllib.request.urlopen("https://hackzurich.involi.live/http_recorded/").read()
        involi_dict = json.loads(involi_bytes.decode("utf8"))
        involi_list = involi_dict["data"]

        for entry in involi_list:
            data_entry = de.DataEntry(entry)
            self.data_dict[data_entry.icao] = data_entry

    def update_drone(self, drone_data_dict):
        drone_data_entry = de.DataEntry(drone_data_dict)
        self.data_dict[drone_data_entry.icao] = drone_data_entry

    def dump_data_dict_to_json(self):
        #filter the involi and drone entries s.t. only iaec and geographic position is left:
        data_list = [self.data_dict[element].data_entry_dict for element in self.data_dict]
        parsed_dict = {}
        parsed_dict["timestamp"] = str(arrow.utcnow())
        parsed_dict["data"] = data_list
        return json.dumps(parsed_dict)


if __name__ == "__main__":
    json_parser = jp.JSON_Parser()
    server_state = ServerState()

    # Updates the server state with the current data from involi
    server_state.update_involi()

    # Update the server state with the current data from involi
    server_state.update_drone(json_parser.mock_drone_data)

    print(server_state.dump_data_dict_to_json())
