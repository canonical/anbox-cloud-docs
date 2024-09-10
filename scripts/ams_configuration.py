#!/usr/bin/env python3

import argparse
import json
from typing import Dict

import requests
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

SWAGGER_URL = (
    "https://canonical.github.io/anbox-cloud.github.com/latest/ams/swagger.json"
)


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="AMS swagger parser",
        description="Extracts AMS configuration data",
    )
    parser.add_argument(
        "-i",
        "--input-file",
        dest="swagger_path",
        required=False,
        help="Path to the swagger json file (Should conform to swagger spec 2.0)",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output_file",
        help="Destination of the rendered configuration file",
        default="reference/ams-configuration.md",
    )
    args = parser.parse_args()
    if args.swagger_path:
        with open(args.swagger_path, mode="r") as f:
            swagger = json.load(f)
    else:
        swagger = get_swagger_from_url()
    parse_swagger(swagger, args.output_file)


def get_swagger_from_url() -> Dict:
    response = requests.get(SWAGGER_URL)
    return response.json()


def parse_swagger(swagger, output_file):
    configs = _parse_config_schema(swagger)
    nodes = _parse_node_schema(swagger)
    env = Environment(loader=FileSystemLoader("."))
    templ = env.get_template("scripts/ams-configuration.md.j2")
    text = templ.render(configs=configs, nodes=nodes)
    with open(output_file, mode="w+") as op:
        op.write(text)


def _parse_config_schema(swagger) -> dict:
    ams_config_path = "/1.0/config"
    config_props = swagger["paths"][ams_config_path]["get"]["responses"]["200"][
        "schema"
    ]["properties"]["metadata"]["properties"]["config"]["properties"]
    for prop in config_props.values():
        if "description" in prop:
            prop["description"] = prop["description"].replace("\n", " ")
    return config_props


def _parse_node_schema(swagger) -> dict:
    node_props = swagger["definitions"]["NodePatch"]["properties"]
    for base, prop in dict(node_props).items():
        key = ""
        if prop["type"] == "object":
            key = "additionalProperties"
        if prop["type"] == "array":
            key = "items"
        if key:
            if schema_name := prop[key].get("$ref"):
                name = schema_name.split("/")[-1]
                if schema := swagger["definitions"][name]:
                    for subprop_name, subprop_attrs in schema["properties"].items():
                        if subprop_name == "id":
                            continue
                        new_base = base
                        if base == "gpus":
                            new_base = f"{base}.<id>"
                        node_props[f"{new_base}.{subprop_name.replace('_', '-')}"] = (
                            subprop_attrs
                        )
            node_props.pop(base)
        else:
            val = node_props.pop(base)
            node_props[base.replace("_", "-")] = val
        if "description" in prop:
            prop["description"] = prop["description"].replace("\n", " ")
    return node_props


if __name__ == "__main__":
    SystemExit(main())
