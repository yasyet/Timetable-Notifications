import requests
import datetime
import config

class Client:
    base_url = f"https://{config.SERVER}/WebUntis/api/"

    def __init__(self):
        self.last_status_code = None
        self.bearer_token = self.generateBearerToken(config.CLIENT_HEADERS)

    def generateBearerToken(self, headers):
        endpoint = "token/new"
        url = f"{self.base_url}{endpoint}"

        response = requests.get(url=url, headers=headers)

        self.last_status_code = response.status_code

        if response.status_code == 200:
            return f"Bearer {response.text}"
        else:
            return None
        
    def getWeeklyCalendar(self):
        # compute monday (start of the current week). If today is Saturday/Sunday, take next Monday.
        today = datetime.date.today()
        today_weekday = today.weekday()  # Monday=0 .. Sunday=6

        if today_weekday >= 5:  # Saturday(5) or Sunday(6): next week's Monday
            days_until_monday = 7 - today_weekday
            monday = today + datetime.timedelta(days=days_until_monday)
        else:
            monday = today - datetime.timedelta(days=today_weekday)

        # include the monday date in the request so API returns the week starting that day
        date_str = monday.strftime("%Y-%m-%d")

        endpoint = f"rest/view/v1/timetable/entries?start=2026-05-18&end=2026-05-22&format=4&resourceType=STUDENT&resources=474&periodTypes=&timetableType=MY_TIMETABLE&layout=START_TIME"
        url = f"{self.base_url}{endpoint}"

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "de-DE,de;q=0.9",

            "Authorization": f"{self.bearer_token}",

            "Cookie": f'{config.COOKIES}',

            "Priority": "u=3, i",
            "Referer": f"https://{config.SERVER}/timetable/my-student?date={date_str}",

            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",

            "Tenant-Id": f"{config.TENANT_ID}",

            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15",
 
            "X-Webuntis-Api-School-Year-Id": "18"
        }

        response = requests.get(url=url, headers=headers)

        self.last_status_code = response.status_code

        if response.status_code == 200:
            response_json = response.json()
            return response_json
        else:
            return None
        
class canceledLesson:
    def __init__(self):
        pass