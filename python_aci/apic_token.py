import requests
import json


def get_token():  
   url = "https://<<apic>>/api/aaaLogin.json"

   payload = {
      "aaaUser": {
         "attributes": {
            "name":"<<username>>",
            "pwd":"<<password>>"
         }
      }
   }

   headers = {
      "Content-Type" : "application/json"
   }

   requests.packages.urllib3.disable_warnings()
   response = requests.post(url,data=json.dumps(payload), headers=headers, verify=False).json()

   token = response['imdata'][0]['aaaLogin']['attributes']['token']
   return token

def main():
   token = get_token()
   print("The token is: " + token)

if __name__ == "__main__":
   main()
