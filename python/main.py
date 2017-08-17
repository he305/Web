import json
from shikimori_api import Api, Request
import getpass
import requests

def main():
    id = 181151 #пиздос я охуел, как так вообще можно, узнать ссаный id невозможно блять
    #user = input("User: ")
    #password = getpass.getpass("Password: ")
    user = "he3050"
    password = "Krabsetr305"
    api = Api(user, password)
    req = Request(api, "animes")
    #data = req.get(status="ongoing", limit=10, order="popularity")
    
    # for i in range(len(data)):
    #     print(data[i]["name"])

    #req.set_name("animes")
    #data = req.get(ids=7791)
        

    # req.set_name("v2/user_rates")
    # data = req.get(user_id=181151, status="completed")
    # ids_str = ""
    # for i in range(len(data)):
    #     ids_str += str(data[i]["target_id"]) + ','
    #     print("animes/" + str(data[i]["target_id"]))

    # print(ids_str)
    # req.set_name("animes")
    # names = req.get(ids=ids_str, limit=100)
    # print(len(names))
    # for i in range(len(names)):
    #     print(names[i]['name'])
    
    url = 'https://shikimori.org/he3050/list_export/animes.json'
    data = requests.Session().get(url)
    print(json.dumps(data.json(), indent=4))
                
if __name__ == "__main__":
    main()