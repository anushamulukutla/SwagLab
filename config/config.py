"""
config/config.py

Load and normalize application configuration from a YAML file located
next to this module.

Behavior:
- Reads `config.yaml` in the same directory.
- Parses YAML into a Python dictionary.
- Uses the top-level `env` key to select an environment section (e.g. `qa`, `stage`).
- Adds a top-level `base_url` key taken from the selected environment section.

Expected `config.yaml` structure:
env: qa
browser: chrome
timeout: 10
qa:
  base_url: https://vosyn.ai
stage:
  base_url: https://stage.vosyn.ai

Return value:
- A dictionary containing the parsed configuration with `base_url` resolved.

Errors:
- Raises `FileNotFoundError` if `config.yaml` is missing.
- Propagates `yaml.YAMLError` for invalid YAML content.
"""

import yaml
import os


def get_config():

    """  The get_config() function reads configuration from a YAML file,
     determines the active environment, extracts the corresponding base URL,
      and returns a normalized
     configuration dictionary for easy use throughout the framework.”   """
    #Locate the config.yaml file relative to this script
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")

    #open and parse the YAML configuration file
    with open(config_path, "r") as file:
        #convert YAML content to a Python dictionary
        data = yaml.safe_load(file)
    #extract the environment key and set the base_url accordingly
    env = data.get("env")
    #look up the base_url for the specified environment
    data["base_url"] = data[env]["base_url"]
    #returns the normalized configuration dictionary
    return data
