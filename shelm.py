#!/usr/bin/env python3

import argparse
from urllib import request
import requests

my_parser = argparse.ArgumentParser(description="command line utility for shelm")

subparser = my_parser.add_subparsers(dest='command')

# defining subparsers for shelm
install = subparser.add_parser('install')
search = subparser.add_parser('search')
list = subparser.add_parser('list')

# options for install subparser
install.add_argument('name',type=str,help='name of helm chart to download')

# options for search subparser
search.add_argument('chart_name',type=str, help="helm chart to search in the repository")

args = my_parser.parse_args()

if args.command == 'install':
    # API call to download specified chart will go here
    remote_url = "http://ec2-44-199-204-102.compute-1.amazonaws.com:80/files/{0}.zip".format(args.name)
    local_file = "{}.zip".format(args.name)
    try:
        request.urlretrieve(remote_url, local_file)
    except Exception:
        print('Not found')
    else:
        print('Installed ',args.name)

elif args.command == 'search':
    # API call to search for specified charts
    response = requests.get('http://ec2-44-199-204-102.compute-1.amazonaws.com:80/files')
    if args.chart_name in response.text:
        print(args.chart_name,"is available")
    else:
        print('Not found')

elif args.command == 'list':
    # API call to list all available charts
    try:
        response = requests.get('http://ec2-44-199-204-102.compute-1.amazonaws.com:80/files')
    except Exception:
        print('Error') 
    else:
        print(response.text)
