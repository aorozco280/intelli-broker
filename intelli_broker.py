import json
import getopt
import pdb
import redis
import requests
from requests.auth import HTTPDigestAuth
import sys

__author__    = "Aldo Orozco Gomez Serrano"
__copyright__ = "Copyright (C) 2017 Aldo Orozco"
__license__   = "Public Domain"
__version__   = "0.1"

redis_up = False

def main(argv):
    """Entry point for the application"""
    print_welcome_header()
    args = read_args()
    if not args['host'] or not args['port']:
        r = setup_redis()
    else
        r = setup_redis(host = args['host'], port = args['port'])
    data = get_data_file()
    print_buy_sell(data)

def print_welcome_header():
    """Prints a (nice) welcome message """
    print("==== Welcome to the (experimental) investor bot $$$$ ====")

def read_args():
    host =
    port =
    url =

    try:
        opts, args = getopt.getotp(argv, ":u:h:p")
    except getotp.GetoptError as err:
        print(err)
        print "Usage: investor_bot.py -u <url> -h <host> -p <port>"
        sys.exit()
    for otp, arg in opts:
        if opt == '-u':
            url = arg
        elif opt == '-h':
            host = arg
        elif opt == '-p':
            port = arg

def get_data_file():
    file_obj = open("input_values", 'r')
    print file_obj

def get_json_url(url)
    resp = requests.get(url)

    if (resp.ok) :
        print "========Status code: %d" % resp.status_code
        print "========Raw content: %s" % resp.content
        data = json.loads(resp.content)
        print "========Succeded: %d" % data["success"]
    else :
        print "Error occurred during read"
        sys.exit(0)


def print_buy_sell(data):
    for val in data:
        print val

def setup_redis(host='localhost', port='1234'):
    """Setup a redis connection"""
    r = redis.StrictRedis(host = host, port = port)
    redis_up = True
    return r

if __name__ == '__main__':
    main(sys.argv[1:])
