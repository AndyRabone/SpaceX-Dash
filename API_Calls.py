import urllib.request
import json
"""
Capsules

Detailed info for serialized dragon capsules

    Get all capsules : GET /capsules
    Get one capsule : GET /capsules/:id
    Query capsules : POST /capsules/query
    lock Create a capsule : POST /capsules
    lock Update a capsule : PATCH /capsules/:id
    lock Delete a capsule : DELETE /capsules/:id

Cores

Detailed info for serialized first stage cores

    Get all cores : GET /cores
    Get one core : GET /v4/cores/:id
    Query cores : POST /cores/query
    lock Create a core : POST /cores - lock
    lock Update a core : PATCH /cores/:id - lock
    lock Delete a core : DELETE /cores/:id - lock

Crew

Detailed info on dragon crew members

    Get all crew members : GET /crew
    Get one crew member : GET /crew/:id
    Query crew members : POST /crew/query


Dragons

Detailed info about dragon capsule versions

    Get all dragons : GET /dragons
    Get one dragon : GET /dragons/:id
    Query dragons : POST /dragons/query


Landpads

Detailed info about landing pads and ships

    Get all landpads : GET /landpads
    Get one landpad : GET /landpads/:id
    Query landpads : POST /landpads/query


Launches

Detailed info about launches

    Get past launches : GET /launches/past
    Get upcoming launches : GET /launches/upcoming
    Get latest launches : GET /launches/latest
    Get next launches : GET /launches/next
    Get all launches : GET /launches
    Get one launch : GET /launches/:id
    Query launches : POST /launches/query


Launchpads

Detailed info about launchpads

    Get all launchpads : GET /launchpads
    Get one launchpad : GET /launchpads/:id
    Query launchpads : POST /launchpads/query


Payloads

Detailed info about launch payloads

    Get all payloads : GET /payloads
    Get one payload : GET /payloads/:id
    Query payloads : POST /payloads/query


Rockets

Detailed info about rocket versions

    Get all rockets : GET /rockets
    Get one rocket : GET /rockets/:id
    Query rockets : POST /rockets/query


Ships

Detailed info about ships in the SpaceX fleet

    Get all ships : GET /ships
    Get one ship : GET /ships/:id
    Query ships : POST /ships/query


Company Info

Detailed info about SpaceX as a company

    Get company info : GET /company

Roadster info

Detailed info about Elon's Tesla roadster's current position

    Get roadster info : GET /roadster

"""
def make_request(url):
    req = urllib.request.Request("https://api.spacexdata.com/v4/{0}".format(url))
    response = urllib.request.urlopen(req)
    the_page = response.read()
    json_payload = json.loads(the_page)
    return json_payload

def get_type(json):
    global type_
    type_ = type(json_payload)
    return type_

def parse_payload_list(payload):
    """
    Unpacks json from list if required.
    """    
    if type_ == list:
        payload = payload[0]
    else:
        payload = payload
    return payload

def get_key(json):
    """
    Return the 'key' element of the key valued pairs.
    """
    json_keys_list = []
    if type_ == list:
        for k in json[0]:
            json_keys_list.append(k)
    else:
        for k in json:
            json_keys_list.append(k)
    return json_keys_list

def print_request(json_payload):
    if type_ == list:
        for e in json_payload:
            for k in keys: 
                if type(e["{0}".format(k)]) == list:
                    # TODO: Doesn't handle nested dicts very well.
                    print("{0} - {1}".format(k, ", ".join(e["{0}".format(k)])))
                else:
                    print("{0} - {1}".format(k, e["{0}".format(k)]))
                print("{0} - {1}".format(k, e["{0}".format(k)]))
            print("\r\r\r")
    else:
        for k in keys:  
            print("{0} - {1}".format(k, json_payload[k]))




"""
<<<<<<<<< Make request, check for nested content. >>>>>>>>>
"""
json_payload = make_request('launches')
get_type(json_payload)

"""
<<<<<<<<< Extract keys and print to terminal in readable format. >>>>>>>>>
"""
keys = get_key(json_payload)
print_request(json_payload)