#!/usr/bin/python3

# imports
import requests
import os
import sys
import datetime
import re
import json
import time
from multiprocessing import Process


j = '{"status":"UP","build":{"build":"19","date":1541617980000,"job":"CCAL-CIB","revision":"1b2b12bdf784c476ad359fcd5d444be0bd51a59d","version":"6.19"}}'


y = json.loads(j)
# y = json.dumps(j)
# print(y["status"])

# canary_username = sys.argv[1]
# canary_password = sys.argv[2]
# canary_host = sys.argv[3]
canary_request = "requests.get(url = canary_host , auth=(canary_username, canary_password))"



def do_actions():

    i = 0
    while True:
        i += 1

        print(i, "making the canary request" )
        if i >= 3:       # question on condition here  ***Need to change for successful request***
            #requests.get(url = canary_host , auth=(canary_username, canary_password))
            print("\n**successful request!**")
            break
        else:
            # time.sleep(30)  # waitretry interval of 30 sec
            time.sleep(2)  # waitretry interval **DEBUG**


if __name__ == '__main__':
    print("Listening for the Canary...\n")
    # Process
    action_process = Process(target=do_actions)

    # timeout the process for an interval.
    action_process.start()
    action_process.join(timeout=450)  # Timeout after 15 attempts to connect

    # End process.
    action_process.terminate()
    print("\nIF successful connection DO JSON validation ELSE time out!\n")
    print("JSON request!\n", j)


    bamboo_status =(y["status"])
    bamboo_build = (y["build"])
    bamboo_ver = (y["build"]["version"])
    bamboo_validation = bamboo_status, bamboo_build, bamboo_ver
    print("**Validation String=", bamboo_validation)

    # bamboo_build = bamboo_build.find('19',11)
    # print("\n", bamboo_build, "\n")

#   Validate the build is up and populated
    if bamboo_status == "UP" and \
       bamboo_build != None and \
       bamboo_ver != None:
        print("Application", bamboo_build, "deployed successfully!\n")
    else:
        print("***Application Failed to Deploy Expected***",bamboo_validation)
        sys.exit()



# # make requests to bamboo
# headers = {'Accept': 'application/json'}
# bamboo_build_results = requests.get(url = bamboo_host + get_bamboo_build_results, headers = headers, auth=(bamboo_username, bamboo_password))
# bamboo_deployment_environment_results = requests.get(bamboo_host + get_bamboo_deployment_environment_results, headers = headers, auth=(bamboo_username, bamboo_password))
#
# # extracting data in json format
# bamboo_build_results_json = bamboo_build_results.json()
# bamboo_deployment_environment_results_json = bamboo_deployment_environment_results.json()
#
#     # make requests to SNOW
# headers = {'Accept': 'application/json','content-type': 'application/json'}
# snow_post_change_results = requests.post(url = snow_host + post_snow_change_request, headers = headers, auth=(snow_username, snow_password), json = change_data)
# snow_post_change_results_json = snow_post_change_results.json()

