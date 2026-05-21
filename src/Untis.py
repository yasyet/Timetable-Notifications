import requests
import config

class Client:
    base_url = "https://gymgan.webuntis.com/"

    def __init__(self):
        self.USERNAME = config.USERNAME
        self.PASSWORD = config.PASSWORD
        self.SERVER = config.SERVER
        self.SCHOOL = config.SCHOOL
        self.USERAGENT = config.USERAGENT

        self.last_status_code = None
        self.bearer_token = self.generateBearerToken(config.CLIENT_HEADERS)

    def generateBearerToken(self, headers):
        endpoint = "WebUntis/api/token/new"
        url = f"{self.base_url}{endpoint}"

        response = requests.get(url=url, headers=headers)

        self.last_status_code = response.status_code

        if response.status_code == 200:
            return f"Bearer {response.text}"
        else:
            return None