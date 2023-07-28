"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    ret = {}
    with open(neo_csv_path, 'r') as file:
        neo_data = csv.reader(file)
        keys_list = next(neo_data)
        for row in neo_data:
            neo = dict(zip(keys_list, row))
            ret[neo['id']] = NearEarthObject(designation = neo['id'], name = neo['name'], hazardous = '')
            ret[neo['id']].approaches = ''
            #ret[neo['id']].designation = neo['id']
            if neo['diameter'] == '':
                ret[neo['id']].diameter = float('nan')
            else:
                ret[neo['id']].diameter = float(neo['diameter'])
            ret[neo['id']].fullname = neo['full_name']
            #ret[neo['id']].hazardous = ''
            #ret[neo['id']].name = neo['name']
    return ret


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path) as file:
        ret = {}
        devo = json.load(file)
        for approach in devo["data"]:
            if approach[0] in ret.keys():
                ret[approach[0]].append(CloseApproach(designation = approach[0], time = approach[3], distance = approach[4], velocity = approach[7]))
            else:
                ret[approach[0]] = [CloseApproach(designation = approach[0], time = approach[3], distance = approach[4], velocity = approach[7])]
    
    # TODO: Load close approach data from the given JSON file.
    return (ret)
