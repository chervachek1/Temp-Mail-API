# Temp-Mail-API
API Wrapper for service which provides temporary email address.

Python API Wrapper for [Temp-Mail](https://temp-mail.org/) service. Temp-mail is a service which lets you use anonymous emails for free. You can view full API specification in [Visit Temp Mail API on RapidAPI](https://rapidapi.com/Privatix/api/temp-mail).

Requirements
------------

[Requests Docs](https://requests.readthedocs.io/en/latest/) - required.

Installation
------------

Installing with pip:

    $ pip install temp-mail-api

Usage
-----

Get all emails:

    from tempmail import TempMail

    tm = TempMail(login='test', domain='@test.pw', api_key='api_key')
    print(tm.get_mailbox())  # list of emails in test@test.pw

Generate email address and get emails from it:

    from tempmail import TempMail

    tm = TempMail()
    email = tm.get_email_address()  # test@test.pw
    print(tm.get_mailbox(email))  # list of emails

-----
Thanks to [Temp-Mail-API/Python](https://github.com/Temp-Mail-API/Python) for the inspiration.