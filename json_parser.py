import json
import arrow


class JSON_Parser:
    """Class responsible for all kinds of JSON transformations"""
    def __init__(self):
        self.mock_involi_dict = json.loads('{"timestamp": "2018-09-14T22:42:27.001569+00:00", "data": [{"icao": "AA4548", "lat": 46.530834474, "lon": 6.2578792135, "alt": 9753, "speed": 236.129796, "heading": -51.76, "last_update": "2018-09-14T22:42:25.898475+00:00"}, {"icao": "3CC158", "lat": 46.7653620825, "lon": 4.62778517592, "alt": 13106, "speed": 208.864264, "heading": -24.04, "last_update": "2018-09-14T22:42:25.899388+00:00"}, {"icao": "4B18E8", "lat": 46.4833024908, "lon": 6.50526510089, "alt": 4876, "speed": 205.7776, "heading": 60.92, "last_update": "2018-09-14T22:42:25.899995+00:00"}, {"icao": "500058", "lat": 46.236418091, "lon": 6.10996544861, "alt": 221, "speed": 6.173328, "heading": 47.58, "last_update": "2018-09-14T22:42:25.900288+00:00"}, {"icao": "4CA2AA", "lat": 47.4180719689, "lon": 7.74213169253, "alt": 10971, "speed": 212.465372, "heading": -79.49, "last_update": "2018-09-14T22:42:25.928268+00:00"}, {"icao": "A7A08A", "lat": 47.7638842137, "lon": 6.05517028969, "alt": 9139, "speed": 222.239808, "heading": -61.04, "last_update": "2018-09-14T22:42:25.929270+00:00"}, {"icao": "4CA63A", "lat": 47.3538156145, "lon": 10.2413150015, "alt": 9440, "speed": 240.245348, "heading": 146.3, "last_update": "2018-09-14T22:42:25.930079+00:00"}, {"icao": "4CA8AA", "lat": 46.01344851, "lon": 6.34316039178, "alt": 11277, "speed": 214.523148, "heading": -153.1, "last_update": "2018-09-14T22:42:25.930892+00:00"}, {"icao": "484C5A", "lat": 47.2058285154, "lon": 6.60977983604, "alt": 11582, "speed": 236.64424, "heading": -6.946, "last_update": "2018-09-14T22:42:25.931150+00:00"}, {"icao": "3451DA", "lat": 46.2372327556, "lon": 6.11106773007, "alt": 334, "speed": 3.601108, "heading": -135.4, "last_update": "2018-09-14T22:42:25.931428+00:00"}, {"icao": "4067C4", "lat": 48.0424877266, "lon": 9.64930746643, "alt": 9448, "speed": 214.008704, "heading": 151.2, "last_update": "2018-09-14T22:42:25.966992+00:00"}, {"icao": "3950C4", "lat": 47.3334782737, "lon": 6.4999149268, "alt": 10313, "speed": 204.748712, "heading": -92.81, "last_update": "2018-09-14T22:42:25.967500+00:00"}, {"icao": "300394", "lat": 47.6321067319, "lon": 10.2560126934, "alt": 8839, "speed": 243.332012, "heading": 82.9, "last_update": "2018-09-14T22:42:25.967775+00:00"}, {"icao": "3C6664", "lat": 47.7756249473, "lon": 9.10699019901, "alt": 10050, "speed": 234.07202, "heading": 153.3, "last_update": "2018-09-14T22:42:25.968079+00:00"}, {"icao": "4401D4", "lat": 47.1014329325, "lon": 9.40989781849, "alt": 11574, "speed": 232.52868800000002, "heading": 11.81, "last_update": "2018-09-14T22:42:25.968630+00:00"}, {"icao": "4B1A24", "lat": 46.3099710655, "lon": 6.21487005542, "alt": 900, "speed": 74.079936, "heading": -134.5, "last_update": "2018-09-14T22:42:25.969429+00:00"}, {"icao": "345614", "lat": 45.3181951473, "lon": 5.99881096414, "alt": 8022, "speed": 225.326472, "heading": 178.0, "last_update": "2018-09-14T22:42:25.969717+00:00"}, {"icao": "459544", "lat": 46.9265153647, "lon": 7.48207632452, "alt": 565, "speed": 68.421052, "heading": 139.4, "last_update": "2018-09-14T22:42:25.969945+00:00"}, {"icao": "3C5EE4", "lat": 46.0281658208, "lon": 6.1784737231, "alt": 10678, "speed": 228.413136, "heading": -166.5, "last_update": "2018-09-14T22:42:25.970413+00:00"}]}')
        # All the drone icao addresses should start with F because these addresses are reserved for future use and no plane will have such an address.
        self.mock_drone_dict = json.loads('{"timestamp": "2018-09-14T22:42:27.001569+00:00", "data": [{"icao": "F950C2", "lat": 46.5076169637, "lon": 5.65638755673, "alt": 4658, "speed": 205.263156, "heading": 85.84, "last_update": "2018-09-14T22:42:26.295514+00:00"}, {"icao": "FCA7F2", "lat": 45.5875617061, "lon": 6.30055438463, "alt": 11277, "speed": 226.86980400000002, "heading": -158.0, "last_update": "2018-09-14T22:42:26.295816+00:00"}, {"icao": "FC5EE2", "lat": 47.7078555556, "lon": 8.03804596927, "alt": 9532, "speed": 214.008704, "heading": -137.3, "last_update": "2018-09-14T22:42:26.296124+00:00"}, {"icao": "F400C2", "lat": 45.9115287469, "lon": 6.71605117115, "alt": 11597, "speed": 234.586464, "heading": -2.642, "last_update": "2018-09-14T22:42:26.296407+00:00"}, {"icao": "F944E7", "lat": 46.7244285541, "lon": 5.53439214841, "alt": 7529, "speed": 210.407596, "heading": -33.32, "last_update": "2018-09-14T22:42:26.330333+00:00"}]}')
        self.mock_drone_data = json.loads('{"icao": "FA7548", "lat": 46.530834474, "lon": 6.2578792135, "alt": 9753, "speed": 236.129796, "heading": -51.76, "last_update": "2018-09-14T22:42:25.898475+00:00"}')

    def prune_to_id_and_geo_coordinates(self, involi_data_dict):
        """Prunes single involi entry to only plane id and geographic coordinates"""
        pruned_dict = {key: involi_data_dict[key] for key in ['icao', 'lat', 'lon', 'alt']}
        return pruned_dict

    def parse_for_map_2d(self, involi_dict, drones_dict):
        self.check_timestamps(involi_dict["timestamp"], drones_dict["timestamp"])

        #filter the involi and drone entries s.t. only iaec and geographic position is left:
        parsed_list_involi = [self.prune_to_id_and_geo_coordinates(element) for element in involi_dict["data"]]
        parsed_list_drones = [self.prune_to_id_and_geo_coordinates(element) for element in drones_dict["data"]]
        merged_list = parsed_list_involi + parsed_list_drones

        parsed_dict = {}
        parsed_dict["timestamp"] = str(arrow.utcnow())
        parsed_dict["data"] = merged_list

        return parsed_dict

    def check_timestamps(self, involi_timestamp, drone_timestamp):
        involi_ts = arrow.get(involi_timestamp)
        drone_ts = arrow.get(drone_timestamp)

        difference = involi_ts - drone_ts


if __name__ == "__main__":
    json_parser = JSON_Parser()

    pruned_entry = json_parser.prune_to_id_and_geo_coordinates(json_parser.mock_involi_dict["data"][0])
    print("Single pruned entry: " + str(pruned_entry))

    parsed_for_map_2d = json_parser.parse_for_map_2d(json_parser.mock_involi_dict, json_parser.mock_drone_dict)
    print("Parsed for map_2d entry: " + str(parsed_for_map_2d))