import string
import random
from hashlib import md5

import requests


class TempMail:
    """
    API Wrapper for service which provides temporary email address.

    :param login: (optional) login for email address.
    :param domain: (optional) domain (from current available) for email address.
    :param api_domain: (optional) domain for temp-mail api.
    """

    def __init__(
        self,
        api_key: str,
        login: str = None,
        domain: str = None,
        api_domain: str = "privatix-temp-mail-v1.p.rapidapi.com",
    ) -> None:
        self._available_domains = None
        self.login = login
        self.domain = domain
        self.api_domain = api_domain
        self.api_key = api_key
        self.headers = {"X-Mashape-Key": self.api_key, "Accept": "application/json"}

    def __repr__(self) -> str:
        return "<TempMail [{0}]>".format(self.get_email_address())

    def get_available_domains(self) -> list:
        """
        Return list of available domains for use in email address.
        """
        if not self._available_domains:
            url = "https://{0}/request/domains/".format(self.api_domain)
            response = requests.get(url, headers=self.headers)
            domains = response.json()
            self._available_domains = domains
        return self._available_domains

    @staticmethod
    def generate_login(
        min_length: int = 6, max_length: int = 10, digits: bool = True
    ) -> str:
        """
        Generate string for email address login with defined length and
        alphabet.

        :param min_length: (optional) min login length.
        Default value is ``6``.
        :param max_length: (optional) max login length.
        Default value is ``10``.
        :param digits: (optional) use digits in login generation.
        Default value is ``True``.
        """
        chars = string.ascii_lowercase
        if digits:
            chars += string.digits
        length = random.randint(min_length, max_length)
        return "".join(random.choice(chars) for x in range(length))

    def get_email_address(self) -> str:
        """
        Return full email address from login and domain from params in class
        initialization or generate new.
        """
        if self.login is None:
            self.login = self.generate_login()

        available_domains = self.available_domains
        if self.domain is None:
            self.domain = random.choice(available_domains)
        elif self.domain not in available_domains:
            raise ValueError("Domain not found in available domains!")
        return "{0}{1}".format(self.login, self.domain)

    @staticmethod
    def get_hash(email: str) -> str:
        """
        Return md5 hash for given email address.

        :param email: email address for generate md5 hash.
        """
        return md5(email.encode("utf-8")).hexdigest()

    def get_mailbox(self, email: str = None, email_hash: str = None) -> dict:
        """
        Return list of emails in given email address
        or dict with `error` key if mailbox is empty.

        :param email: (optional) email address.
        :param email_hash: (optional) md5 hash from email address.
        """
        if email is None:
            email = self.get_email_address()
        if email_hash is None:
            email_hash = self.get_hash(email)

        url = "https://{0}/request/mail/id/{1}/".format(self.api_domain, email_hash)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def delete_email(self, email: str = None, email_hash: str = None) -> dict:
        """
        Delete a given email in a given email address

        :param email: (optional) email address.
        :param email_hash: (optional) md5 hash from email address.
        """
        if email_hash is None:
            email_hash = self.get_hash(email)

        url = "https://{0}/request/delete/id/{1}/".format(self.api_domain, email_hash)

        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_attachments(self, email: str = None, email_hash: str = None) -> dict:
        """
        Get attachments of a given email in a given email address

        :param email: (optional) email address.
        :param email_hash: (optional) md5 hash from email address.
        """
        if email_hash is None:
            email_hash = self.get_hash(email)

        url = "https://{0}/request/attachments/id/{1}/".format(
            self.api_domain, email_hash
        )

        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_attachments_legacy(self, email: str = None, email_hash: str = None) -> dict:
        """
        Get attachments of a given email in a given email address

        :param email: (optional) email address.
        :param email_hash: (optional) md5 hash from email address.
        """
        if email_hash is None:
            email_hash = self.get_hash(email)

        url = "https://{0}/request/attachments/id/{1}/".format(
            self.api_domain, email_hash
        )

        response = requests.get(url, headers=self.headers)
        return response.json()

    def get__one_attachment(
        self, email: str = None, email_hash: str = None, attachment_id: str = None
    ) -> dict:
        """
        Get attachments of a given email in a given email address

        :param attachment_id:
        :param email: (optional) email address.
        :param email_hash: (optional) md5 hash from email address.
        """
        if email_hash is None:
            email_hash = self.get_hash(email)

        url = "https://{0}/request/one_attachment/id/{1}/{2}/".format(
            self.api_domain, email_hash, attachment_id
        )

        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_message(self, email: str = None, email_hash: str = None) -> dict:
        """
        Get a given email in a given email address

        :param email: (optional) email address.
        :param email_hash: (optional) md5 hash from email address.
        """
        if email_hash is None:
            email_hash = self.get_hash(email)

        url = "https://{0}/request/one_mail/id/{1}/".format(self.api_domain, email_hash)

        response = requests.get(url, headers=self.headers)
        return response.json()

    def source_message(self, email: str = None, email_hash: str = None) -> dict:
        """
        Source a given email in a given email address

        :param email: (optional) email address.
        :param email_hash: (optional) md5 hash from email address.
        """
        if email_hash is None:
            email_hash = self.get_hash(email)

        url = "https://{0}/request/source/id/{1}/".format(self.api_domain, email_hash)

        response = requests.get(url, headers=self.headers)
        return response.json()
