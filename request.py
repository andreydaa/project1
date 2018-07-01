#!/usr/bin/env python3

import re
import requests


def check_link(link):

    try:
        resp = requests.get(link)
    except requests.exceptions.HTTPError:
        return ''
    if resp.status_code != 200:
        return ''
    return resp.text


def main():
    
    a_link, b_link = input(), input()
    rg = re.compile(r'<a href="(\S+)"[^>]*>\w+</a>', re.DOTALL)

    text = check_link(a_link)
    a_links = rg.findall(text)

    for l in a_links:
        text = check_link(l)
        links = rg.findall(text)
        if any(link == b_link for link in links):
            return 'Yes'
    return 'No'


if __name__ == '__main__':
    print(main())
