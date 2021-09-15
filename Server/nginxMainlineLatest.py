#!/usr/bin/env python3

"""
Downloads the most recent mainline version of Nginx from nginx.org and RTMP
module from https://github.com/sergey-dryabzhinsky/nginx-rtmp-module, saves it
locally, and builds it.

https://twitter.com/m4xx3d0ut
https://github.com/m4xx3d0ut
"""

import requests
import shlex
import subprocess
from time import sleep
from os import path, mkdir, getcwd, chdir
from shutil import rmtree
from buildDeps import cmd_out

# Download page URL for Nginx latest, function will parse latest version
nginx_dl_latest = 'http://nginx.org/en/download.html'
# Direct URL of Nginx RTMP module
nginx_rtmp = \
'https://github.com/sergey-dryabzhinsky/nginx-rtmp-module/archive/dev.zip'
# Initialize file name variables
cwd = ''
nginx_latest_local = ''
rtmp_local = ''
tmp_path = ''
# Build Nginx with RTMP module
configure = \
'./configure --with-http_ssl_module --add-module=../nginx-rtmp-module-dev'
make = 'make'
make_install = 'sudo make install'
# Instal path of Nginx source build
nginx_path = '/usr/local/nginx'
nginx_sbin = '/usr/local/sbin/nginx'
nginx_ln = 'sudo ln -s /usr/local/nginx/sbin/nginx /usr/local/sbin/'
# Uninstall Nginx
nginx_uninst = 'sudo rm -f -R %s && rm -f %s' % (nginx_path, nginx_sbin)


# Check if another source install of Nginx exists
def check_nginx_install():

    if path.isdir(nginx_path) == True:
        print('[!] WARNING, existing Nginx build found.')
        rm = input('[!] Would you like to delete the existing build? (y/n):')
        if rm == 'y':
            if path.isfile(nginx_sbin) == True:
                f = subprocess.Popen(shlex.split(nginx_uninst), \
                    stderr=subprocess.PIPE, stdout=subprocess.PIPE, \
                    stdin=subprocess.PIPE)
                cmd_out(f)
            elif path.isfile(nginx_sbin) == False:
                rm_nginx_dir = nginx_uninst.split('&&')[0]
                f = subprocess.Popen(shlex.split(rm_nginx_dir), \
                    stderr=subprocess.PIPE, stdout=subprocess.PIPE, \
                    stdin=subprocess.PIPE)
                cmd_out(f)
            else:
                print('[!] Response invalid, exiting...')
                exit(0)
    else:
        print('[!] Check for existing Nginx build, none found.')


# Dowloads the latest Nginx mainline
def nginx_mainline_latest():
    global nginx_latest_local, cwd

    cwd = getcwd()
    print('[*] CWD: %s' % (cwd))
    print('[*] Dowloading latest Nginx mainline from %s' % (nginx_dl_latest))
    r = requests.get(nginx_dl_latest) 
    status_code = str(r.status_code)
    if str(r.status_code) == '200':
        print('[*] Pass. Server status code: %s' % (status_code))
    else:
        print('[!] Error. Server status code: %s' % (status_code))
        print('[!] Unable to download. Exiting...')
        exit(0)
    txt_split = r.text.split('"/download/nginx-')[1]
    ver = txt_split.split('.tar.gz')[0]
    nginx_latest_local = 'nginx-%s.tar.gz' % (ver)
    remote_url = 'http://nginx.org/download/%s' % (nginx_latest_local)
    print('[*] Downloading %s from %s' % (nginx_latest_local, remote_url))
    data = requests.get(remote_url)
    print('[+] Writing to local file: %s' % (nginx_latest_local))
    with open(nginx_latest_local, 'wb') as file: 
        file.write(data.content)
    print('[!] Dowload complete.')

# Downloads the Nginx RTMP module
def nginx_rtmp_mod():
    global rtmp_local

    rtmp_local = nginx_rtmp.split('/')[-1]

    print('[*] Downloading Nginx RTMP module from: %s' % (nginx_rtmp))
    data = requests.get(nginx_rtmp)
    print('[+] Writing to local file: %s' % (rtmp_local))
    with open(rtmp_local, 'wb') as file:
        file.write(data.content)
    print('[!] Download complete.')

# Build Nginx with RTMP support
def nginx_rtmp_build(nginx, rtmp):
    global tmp_path

    build_path = \
    input('[*] Press enter to build in ./tmp or specify full path: ')

    if build_path == '':
        print('[*] Extract archives to ./tmp...')
        if path.isdir('./tmp') == True:
            yn = input('[!] WARNING: ./tmp exists, delete it? (y/n): ')
            if yn == 'y':
                print('[-] Deleting old ./tmp directory...')
                rmtree('./tmp')
                print('[+] Creating new ./tmp directory.')
                mkdir('./tmp')
                tmp_path = '%s/tmp' % (getcwd())
            elif yn == 'n':
                print('[!] Please rename or move ./tmp and rerun installer. \
Exiting...')
                exit(0)
            else:
                print('[!] Response invalid, exiting...')
                exit(0)
        else:
            print('[+] Creating new ./tmp directory.')
            mkdir('./tmp')
            tmp_path = '%s/tmp' % (getcwd())

    else:
        if path.isdir(build_path) == True:
            print('[*] Specified path is valid.')
            if build_path[-1] == '/':
                tmp_path = '%stmp' % (build_path)
            else:
                tmp_path = '%s/tmp' % (build_path)
            if path.isdir(tmp_path) == False:
                print('[+] Creating tmp build dir: %s' % (tmp_path))
                mkdir(tmp_path)

    sleep(2)
    print('[+] Extracting archives to: %s' % (tmp_path))
    untar = 'tar -xvf %s -C %s' % (nginx_latest_local, tmp_path)
    unzip = 'unzip %s -d %s' % (rtmp_local, tmp_path)

    print('[*] Inflating tar: %s' % (nginx))
    sleep(1)

    untar_nginx = subprocess.Popen(shlex.split(untar), stderr=subprocess.PIPE, \
        stdout=subprocess.PIPE,  stdin=subprocess.PIPE)
    cmd_out(untar_nginx)

    print('[*] Unzip RTMP module: %s' % (rtmp))
    sleep(1)

    unzip_rtmp = subprocess.Popen(shlex.split(unzip), stderr=subprocess.PIPE, \
        stdout=subprocess.PIPE,  stdin=subprocess.PIPE)
    cmd_out(unzip_rtmp)

    print('[*] Building Nginx with RTMP module...')
    sleep(1)

    chdir('%s/%s' % (tmp_path, nginx_latest_local[0:-7]))

    # Now we build nginx with rtmp module
    # ./configure --with-http_ssl_module --add-module=../nginx-rtmp-module-dev
    configure_nginx = subprocess.Popen(shlex.split(configure), stderr=subprocess.PIPE, \
        stdout=subprocess.PIPE,  stdin=subprocess.PIPE)
    cmd_out(configure_nginx)
    # make
    make_nginx = subprocess.Popen(shlex.split(make), stderr=subprocess.PIPE, \
        stdout=subprocess.PIPE,  stdin=subprocess.PIPE)
    cmd_out(make_nginx)
    # sudo make install, installs to /usr/local/nginx/sbin/
    install_nginx = subprocess.Popen(shlex.split(make_install), stderr=subprocess.PIPE, \
        stdout=subprocess.PIPE,  stdin=subprocess.PIPE)
    cmd_out(install_nginx)
    # Link to /user/local/sbin
    link_nginx = subprocess.Popen(shlex.split(nginx_ln), stderr=subprocess.PIPE, \
        stdout=subprocess.PIPE,  stdin=subprocess.PIPE)
    cmd_out(link_nginx)

    # Clean up build files
    print('[*] Source build complete and Nginx has been installed!')
    clean = input('[!] Delete %s, %s, %s? (y/n): ' % (nginx_latest_local, \
    rtmp_local, tmp_path))
    chdir(cwd)
    if clean == 'y':
        # Delete downloaded archives
        build_files = [nginx_latest_local, rtmp_local]
        for f in build_files:
            rm_archives = 'sudo rm -f %s' % (f)
            rem = subprocess.Popen(shlex.split(rm_archives), stderr=subprocess.PIPE, \
                stdout=subprocess.PIPE,  stdin=subprocess.PIPE)
            cmd_out(rem)
        # Delete tmp dir
        rm_tmp = 'sudo rm -f -R %s' % (tmp_path)
        rem = subprocess.Popen(shlex.split(rm_tmp), stderr=subprocess.PIPE, \
            stdout=subprocess.PIPE,  stdin=subprocess.PIPE)
        cmd_out(rem)
        print('[*] Working files have been removed.')
    elif clean == 'n':
        print('[*] Working files preserved.')
    else:
        print('[!] Response invalid, exiting...')
        exit(0)


if __name__ == '__main__':

    check_nginx_install()
    nginx_mainline_latest()
    nginx_rtmp_mod()
    nginx_rtmp_build(nginx_latest_local, rtmp_local)