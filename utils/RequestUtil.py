#!/usr/bin/env python
# coding=utf-8
import time
import urllib3
import requests


class Requests():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def __init__(self):
        requests.adapters.DEFAULT_RETRIES = 10
        self.session = requests.session()
        # self.ipaddress = ipaddress
        self.r = None
        self.session.keep_alive = False
        self.session.headers = {'Authorization': 'Basic a2FyYWY6a2FyYWY=', 'connection': 'close'}

    def do_get(self, url):
        return self.session.get(url=url, headers=self.session.headers, verify=False)

    def do_post(self, url, parameter):
        return self.session.post(url=url, json=parameter, headers=self.session.headers, verify=False)

    def get_response(self, url, method, parameter=None):
        res={}
        if str(method).upper() == 'GET':
            self.r = self.do_get(url)
        elif str(method).upper() == 'POST':
            self.r = self.do_post(url, parameter)
        return self.r
