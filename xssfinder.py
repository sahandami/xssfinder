#!/usr/bin/python3

from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import urllib3
import os
import sys
from time import time
from subprocess import check_output

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

os.system('> xss')
counter = 0

with requests.Session() as req:

        def reqsender(url,counter):
                res = req.get(url, verify=False, stream=True, timeout=1.5)
                #time.sleep(9)
                #print(res.text)
                if 'xsst<>' in res.text:
                        print("\033[1;31;40m [xss found]\033[1;36;40m : \033[1;37;40m", url, "\033[1;36;40m : \033[1;37;40m {}/{}".format(counter,line_count))

                        file1 = open('xss', 'a')
                        file1.write(url+'\n')
                        file1.close()
                else:
                        print("\033[1;32;40m [ok]\033[1;36;40m : \033[1;37;40m", url, "\033[1;36;40m : \033[1;37;40m {}/{}".format(counter,line_count))

        pwd = check_output('pwd').strip()
        filename_demo = sys.argv[1]
        pwd = pwd.decode('utf-8')

        filename = 'b{}/{}'.format(pwd, filename_demo)[1:]
        print(filename)
        file = open(filename, 'r')
        Lines = file.readlines()
        file.close()

        file = open(filename, "r")
        line_count = 0
        for line in file:
                if line != "\n":
                        line_count += 1
        file.close()
        print(line_count)
        start = time()
        processes = []
        with ThreadPoolExecutor(max_workers=20) as executor:

                for line in Lines:
                        counter += 1
                        url = line[:-1]
                        processes.append(executor.submit(reqsender, line, counter))
        print(time() - start)