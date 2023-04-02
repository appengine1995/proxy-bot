import random
import os
import re
import config
import datetime
from urllib import parse
global proxylist, tgproxylist

def init():
    global proxylist, tgproxylist
    if os.path.isfile(config.PROXY_FILE):
        with open(config.PROXY_FILE, "r") as file:
            lines = file.readlines()
            proxylist = [line.split() for line in lines]
    else:
        with open(config.PROXY_FILE, "w") as file:
            pass
    if os.path.isfile(config.TGPROXY_FILE):
        with open(config.TGPROXY_FILE, "r") as file:
            lines = file.readlines()
            tgproxylist = [line.split() for line in lines]
    else:
        with open(config.TGPROXY_FILE, "w") as file:
            pass

def subconvert(text):
    url_list = re.findall("[-A-Za-z0-9+&@#/%?=~_|!:,.;]+://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]", text)
    url_list = list(set(url_list))
    result = random.choice(config.backend) + "sub?target=clash&url=" + parse.quote_plus(url_list[0])
    for url in url_list[1:]:
        if len(url) != 0:
            result = result + "|" + parse.quote_plus(url)
    result = result + "&insert=false&config=" + parse.quote_plus(config.ini) + "&emoji=true&list=false&tfo=false&expand=true&scv=true&fdn=false&new_name=true"
    return result

def get_proxy():
    if len(proxylist) > 0:
        num_of_values = random.randint(1, 3)
        random_values = ""
        for num in random.sample(proxylist, num_of_values):
            random_values += str(num[0]) + "\n"
        return str(random_values) + config.NEWS
    else:
        return "代理池为空" + config.NEWS

def get_tgproxy():
    if len(tgproxylist) > 0:
        num_of_values = random.randint(1, 3)
        random_values = ""
        for num in random.sample(tgproxylist, num_of_values):
            random_values += str(num[0]) + "\n"
        return str(random_values) + config.NEWS
    else:
        return "代理池为空" + config.NEWS

def get_proxylist():
    init()
    proxy = str(len(proxylist))
    tgproxy = str(len(tgproxylist))
    return "v2ray/clash代理池中有：" + proxy + "个代理\nmtproxy代理池中有：" + tgproxy + "个代理"