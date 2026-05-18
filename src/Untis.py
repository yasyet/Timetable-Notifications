import webuntis
import logging
from contextlib import AbstractContextManager
from typing import Optional

logger = logging.getLogger(__name__)


class AuthDetails:
    def __init__(self, username: str, password: str, server: str, school: str, useragent: str):
        self.username = username
        self.password = password
        self.server = server
        self.school = school
        self.useragent = useragent


class Untis(AbstractContextManager):
    def __init__(self, auth_details: AuthDetails):
        self.auth_details = auth_details
        self.session: Optional[webuntis.session.Session] = None

    def init_session(self):
        self.session = webuntis.session.Session(
            server=self.auth_details.server,
            username=self.auth_details.username,
            password=self.auth_details.password,
            school=self.auth_details.school,
            useragent=self.auth_details.useragent,
        )
        return self.session

    def login(self):
        if self.session is None:
            self.init_session()
        logger.info("Logging in to Untis server")
        self.session.login()

    def logout(self):
        if self.session is None:
            return
        try:
            logger.info("Logging out from Untis server")
            self.session.logout()
        except Exception:
            logger.exception("Failed to logout cleanly")

    def __enter__(self):
        self.login()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.logout()

    def get_timetable(self, start_day: str, end_day: str):
        """
        Get timetable of logged in user for given data range.
        """
        if self.session is None:
            raise RuntimeError("Session not initialized. Call login() or use context manager.")
        return self.session.my_timetable(start=start_day, end=end_day).to_table()