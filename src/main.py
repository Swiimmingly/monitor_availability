import requests
import yaml
import time
import argparse
import json
import datetime
from urllib.parse import urlparse

def read_yaml_file(file_path):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)

    return data

def parse_and_check(config_data,hist):
    for element in config_data:
        url,name,method,headers,body = element["url"],element.get("name",""),element.get("method", "GET"),element.get("headers", {}),element.get("body","{}")
        body = json.loads(body)
        domain = urlparse(url).netloc

        availability = check_availability(
            url,
            name,
            method,
            headers,
            body  
        )
        #store in dictionary

        if domain not in hist:
            hist[domain] = [0,0]
        if availability:
                hist[domain][0] +=1
        else:
                hist[domain][1] +=1

    print_output(hist)
    return hist

def check_availability(url,name, method="GET", headers=None, body=None):
    try:
        response = requests.request(method, url, headers=headers,data=body)

        # print(f"Endpoint with name {name} has HTTP response code {response.status_code} and response latency {response.elapsed.total_seconds()*1000}")
        #check if ms is less than 500 and code is in[200-299]
        return response.status_code // 100 == 2 and int(response.elapsed.total_seconds()*1000) < 500
    except requests.ConnectionError:
        return False


def print_output(hist):
    for url,av in hist.items():
        availability_percentage = 100*(av[0]/sum(av))
        print(f"{url} has {round(availability_percentage)}% availability Percentage")
        print("[" + "=" * int(availability_percentage) + "-" * (100 - int(availability_percentage)) + "]\n")

def main(yaml_file):
    #read file and define a datastructure to keep track of data
    config_data = read_yaml_file(yaml_file)
    hist = {}

    while True:
        parse_and_check(config_data,hist)
        
    
        time.sleep(15)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check URL availability")
    parser.add_argument("yaml_file", help="Path to the configuration file in YAML format")
    args = parser.parse_args()

    main(args.yaml_file)

