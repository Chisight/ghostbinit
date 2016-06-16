#!/usr/bin/python3
# paste_ghostbin.py
# Copyright (c) 2016 Chisight
# Licensed under the MIT License
# https://opensource.org/licenses/MIT

import requests

s = requests.Session()

def getFFCookies():
    """Grab cookies from firefox to allow pastes to be edited there
    """
    from firefox_jar import firefox_jar
    s.cookies=firefox_jar()



def ghostpaste(text, expire=None, lang=None, title=None, passwd=None, http=None):
    """Send a paste to ghostbin.com.
    text: body of paste
    expire: longevity, valid suffixes: ns/us/ms/s/m/h/d/w
        '-1' for forever
    lang: language text is written in, i.e. 'python 3'
    passwd: protects your pastes, can't be read without the password
    returns URL, or None on error
    """

    headers = {    'content-type': 'application/x-www-form-urlencoded', 
            'User-Agent': 'paste_ghostbin.py/0.0.1 requests/2.9.1'}

    params = {}

    if expire is not None:
        params['expire'] = expire
    else:
        params['expire'] = '1d'

    if lang is not None:
        params['lang'] = lang # full list at https://ghostbin.com/languages.json
    else:
        params['lang'] = 'text'

    if title is not None:
        params['title'] = title

    if passwd is not None:
        params['password'] = passwd

    if http is not None:
        http = 'http'
    else:
        http = 'https'


    r=s.post(http+'://ghostbin.com/paste/new', params=params, headers=headers, data="text="+text)
    r.raise_for_status()

    return r.url

if __name__ == "__main__":
#example usage:
    getFFCookies()
    print( ghostpaste('test example paste','1h','python3'))

