#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time
from urllib.parse import urljoin
import sys
import sqlite3
from sqlite3 import Error

token = 'AbSVsVz7xfk.PTq'
serverlist = ['85.111.30.81', '85.111.39.81']
pushserver = 'https://gotify.vm64.info/'
reqpath = '/photos/07/19/38/thmb_8590719388op.jpg'


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def updatecount(provider):
    database = 'cdndb.db'
    try:
        cursor = create_connection(database).cursor()
        update = """Update cdn set failcount = failcount + 1 where id = 1"""
        print(update)
        cursor.execute(update)
        create_connection(database).commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if create_connection(database):
            create_connection(database).close()
            print("The SQLite connection is closed")


def push(provider, message):
    requestURL = urljoin(pushserver, '/message?token=' + token)
    try:
        resp = requests.post(requestURL, json={
            "message": message,
            "priority": 5,
            "title": provider
        })
    except requests.exceptions.RequestException as e:
        # Print exception if reqeuest fails
        sys.exit('Could not connect to Gotify server:\n' + str(e))

    # Print request result if server returns http error code
    if resp.status_code is not requests.codes.ok:
        sys.exit(bytes.decode(resp.content))


def fetchContent(provider):
    path = ('http://%s%s' % (provider, reqpath))
    r = requests.get(path)
    return r.status_code


def cdnHealth():
    message = 'Healthcheck failed for provider'
    for provider in serverlist:
        r = fetchContent(provider)
        if r == 200:
            updatecount(provider)
            # push(provider, message)


cdnHealth()