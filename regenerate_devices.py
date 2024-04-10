#!/usr/bin/env python3

import json
import yaml
import requests


def getPlayDevices():
    url = "https://raw.githubusercontent.com/teqcorp/play_certified_devices/main/devices.json"

    response = requests.get(url)
    response.raise_for_status()

    return response.json()


def getMobileDBDevices():
    with open("devices.yml", "r") as f:
        data = yaml.load(f.read(), Loader=yaml.CLoader)

    devices = []

    for oem in data:
        for codename in data[oem]:
            model = data[oem][codename]

            devices.append(
                {
                    "codename": codename,
                    "retail_branding": oem,
                    "marketing_name": model,
                    "model": "nan",
                    "name": f"{oem} {model}",
                }
            )

    return devices


def main():
    play_devices = getPlayDevices()

    mobiledb_devices = getMobileDBDevices()

    # TODO: Sort this list
    devices = play_devices + mobiledb_devices

    with open("devices.json", "w") as f:
        f.write(json.dumps(devices).replace("},", "},\n"))


if __name__ == "__main__":
    main()
