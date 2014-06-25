#!/usr/bin/python
import sys, getopt, settings, json, os
from subprocess import call
from pyimgur.imgur.factory import factory

def main(argv):
    settings.init()

    # Assess command line args
    num = settings.num
    if num is None:
        num = ''
    path = ''
    msg = ''
    usage = 'Usage:\n' \
              'python main.py -p <img_path> -n <number> -m <message>\n' \
              'or\n' \
              'alias -p <img_path> -n <number> -m <message>'
    try:
        opts, args = getopt.getopt(argv,"hp:n:m:",["path=", "num=","msg="])
    except getopt.GetoptError:
        print usage
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print usage
            sys.exit()
        elif opt in ("-n", "--num"):
            num = arg
        elif opt in ("-m", "--msg"):
            msg = arg
        elif opt in ("-p", "--path"):
            path = arg

    # Load imgur config file
    config = None
    try:
        config_path = os.path.join(os.path.split(os.path.abspath(__file__))[0],
                                   "config.json")
        fd = open(config_path, 'r')
    except:
        print("config file [config.json] not found.")
        sys.exit(1)

    try:
        config = json.loads(fd.read())
    except:
        print("invalid json in config file.")
        sys.exit(1)

    # Upload image from given path anonymously to imgur and obtain link
    mfactory = factory(config)
    imgur = mfactory.build_api()
    imgur_req = mfactory.build_request_upload_from_path(path)
    try:
        res = imgur.retrieve(imgur_req)
        img_link = res['link']
    except expired:
        print("Expired access token")

    # Draft and send text message
    number = str('number=%s' % (num))
    message = str('message=%s %s' % (img_link, msg))
    cmd = ['curl', 'http://textbelt.com/text', '-d', number, '-d', message]
    print("Sending Message: [" + img_link + " " + msg + "]")
    call(cmd)

if __name__ == "__main__":
   main(sys.argv[1:])