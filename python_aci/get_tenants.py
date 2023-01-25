import requests
import json
from apic_token import get_token

def get_tenants():
   token = get_token()

   url = "https://<<apic>>/api/node/class/fvTenant.json"
   
   headers = {
      "Cookie" : f"APIC-Cookie={token}", 
   }

   requests.packages.urllib3.disable_warnings()
   response = requests.get(url, headers=headers, verify=False)

   return response

if __name__ == "__main__":
   response = get_tenants().json()
   tenants = response['imdata']
   
   for tenant in tenants:
      print(f"Tenant name: {tenant['fvTenant']['attributes']['name']}")
