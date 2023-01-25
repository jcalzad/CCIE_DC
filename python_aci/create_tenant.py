import requests
import json
from apic_token import get_token

print("Enter new Tenant name:")
tenant_name = input()


def create_tenant():
  
   token = get_token()

   url = "https://<<apic>>/api/mo/uni.json"
   
   payload = {
      "fvTenant": {
         "attributes": {
            "name": tenant_name,
            "descr": "Deployed with Python"
         }
      }
   }

   headers = {
      "Cookie" : f"APIC-Cookie={token}", 
   }

   requests.packages.urllib3.disable_warnings()
   response = requests.post(url,data=json.dumps(payload), headers=headers, verify=False)

   if (response.status_code == 200):
      print("Successfully created " + tenant_name + "!")
   else:
      print("Issue with creating " + tenant_name + ".")

def get_tenant():
   return tenant_name



if __name__ == "__main__":
   create_tenant()
