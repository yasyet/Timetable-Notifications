import os
from dotenv import load_dotenv

from Untis import AuthDetails, Untis

import datetime
from collections.abc import Mapping
from typing import Any, Optional

def extract_attr(s: set) -> Optional[str]:
    try:
        item = next(iter(s))
    except StopIteration:
        return None
    if isinstance(item, Mapping):
        return item.get("code")
    if hasattr(item, "code"):
        return getattr(item, "code")
    if hasattr(item, "to_dict"):
        return item.to_dict().get("code")
    if hasattr(item, "__dict__"):
        return item.__dict__.get("code")
    return None

def main():
    # Init auth_key
    load_dotenv()

    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    SERVER = os.getenv("SERVER")
    SCHOOL = os.getenv("SCHOOL")
    USERAGENT = os.getenv("USERAGENT")

    required = {
        "USERNAME": USERNAME,
        "PASSWORD": PASSWORD,
        "SERVER": SERVER,
        "SCHOOL": SCHOOL,
        "USERAGENT": USERAGENT,
    }
    missing = [k for k, v in required.items() if not v]
    if missing:
        raise RuntimeError(f"Missing environment variables: {', '.join(missing)}")

    auth_details = AuthDetails(USERNAME, PASSWORD, SERVER, SCHOOL, USERAGENT)

    """# Get timetable for today or tomorrow if it's after 4pm
    start_datetime = datetime.datetime.today() + datetime.timedelta(days=2)
    end_datetime = start_datetime

    if datetime.datetime.now().hour >= 16:
        start_datetime += datetime.timedelta(days=1)
        end_datetime += datetime.timedelta(days=1)"""
    
    # Demo start time
    start_datetime = datetime.datetime(2026, 5, 19)
    end_datetime = start_datetime

    with Untis(auth_details) as untis:
        timetable = untis.get_timetable(start_datetime, end_datetime)

        day = timetable

        print(f"Morgen hast du {len(timetable)} Stunden\n")
            

if __name__ == "__main__":
    main()
