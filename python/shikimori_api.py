import requests

class Api():
    def __init__(self, nick, passwd, debug=False):
        self.root_url = "https://shikimori.org/api/"
        self.nick = nick
        self.password = passwd
        self.debug = debug
        token_url = self.root_url + 'access_token?nickname={}&password={}'.format(self.nick, self.password)

        self.token = requests.get(token_url).json()['api_access_token']

        self.headers = {"X-User_Nickname" : self.nick,
                        "X-User_Api_Access_Token" : self.token,
                        "User-Agent" : "Pyhe3050"}

        self.session = requests.Session()
        self.session.headers.update()

    def _make_req(self, request, method):
        if self.debug:
            print(request.args)
        args_list = request.args
        req_url = self.root_url + request.name

        if self.debug:
            print(req_url)
    
        if method == 'get':
            r = self.session.get(req_url, params=args_list)
        elif method == 'post':
            r = self.session.post(req_url, json=args_list)

        if (self.debug):
            print(r)
        return r.json()

class Request():
    def __init__(self, api, name):
        self.api = api
        self.name = name

    def set_name(self, name):
        self.name = name

    def get(self, **args):
        self.args = args
        return self.api._make_req(self, 'get')

    def post(self, **args):
        self.args = args
        return self.api._make_req(self, 'post')

