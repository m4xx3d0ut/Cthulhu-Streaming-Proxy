#!/usr/bin/env python3

"""
Downloads the most recent mainline version of Nginx from nginx.org and
saves it locally.

https://twitter.com/m4xx3d0ut
https://github.com/m4xx3d0ut
"""

import requests 

nginxDowloadUrl = 'http://nginx.org/en/download.html'

def nginxMainlineLatest():

    print('[*] Dowloading latest Nginx mainline from %s' % (nginxDowloadUrl))
    r = requests.get(nginxDowloadUrl) 
    status_code = str(r.status_code)
    if str(r.status_code) == '200':
        print('[*] Pass. Server status code: %s' % (status_code))
    else:
        print('[!] Error. Server status code: %s' % (status_code))
        print('[!] Unable to download. Exiting...')
        exit(0)
    txt_split = r.text.split('"/download/nginx-')[1] 
    ver = txt_split.split('.tar.gz')[0] 
    local_file = 'nginx-%s.tar.gz' % (ver) 
    remote_url = 'http://nginx.org/download/%s' % (local_file) 
    print('[*] Downloading %s from %s' % (local_file, remote_url))
    data = requests.get(remote_url) 
    print('[+] Writing to local file: %s' % (local_file))
    with open(local_file, 'wb') as file: 
        file.write(data.content) 
    print('[!] Dowload complete.')

if __name__ == '__main__':

    nginxMainlineLatest()