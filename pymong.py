##### PyMonG
##### (c) 2024 Giovambattista Vieri All Rigths Reserved
##### License Affero GPL. 



# free -m 
# vmstat 
# df 
# lscpu 
# mpstat
# iostat

# nstat
# ss
# netstat -1
# ip -s link
# arpwatch
##############

import sys
import gnupg
import base64
import pprint


commands=["free -m",
#          "vmstat",
#          "lscpu",
#          "mpstat",
#          "iostat",
#          "nstat",
#          "ss",
#          "netstat -l",
#          "ip -s link",
#          "arpwatch",
          "df -k"]


import os 
import subprocess
import argparse


defaultkey='testgpg@example.com'

def getOptions(args=sys.argv[1:]):
    parser=argparse.ArgumentParser(description='This simple program will help you to write an encrypted monitor about a server status. The resulting string is printed on stdout and can be sent via mqtt or smtp, etc..',epilog='Example of use:')
    parser.add_argument('-v','--verbose', help='more verbose output', action='store_true')
    parser.add_argument('-a','--archive', help='archive report in files in ~./repo_path ', action='store_true')
    parser.add_argument('-k','--key', help='choose gpg key to use', default=defaultkey, action='store')
    opt=parser.parse_args(args)
    return(opt)

opt=getOptions()
verbose=opt.verbose
archive=opt.archive
enc_key=opt.key

res=""
for c in commands:
    r=subprocess.check_output(c,shell=True)
    res=res+"---"+c+"---\n"+r.decode("ascii")

###########
### print(res)
##########




recipient_key=[enc_key]
path= os.getcwd()
gpg=gnupg.GPG(gnupghome=path+'/.gnupg')
public_keys = gpg.list_keys() 

if (verbose):
    for pk in public_keys:
        print(pk['uids'])
    print ("--------------------------")

if(archive):
    file_path="/prova1.txt"
    repo_path="./repo_path"
    if not os.path.exists(repo_path):
        os.makedirs(repo_path)

    file="."+file_path
    print("--------------",file)

    output_path=repo_path+file_path
    print("--------------",output_path)

try:
###    status = gpg.encrypt_file(
####        file_data,
###        res,
###        recipients=recipient_key,
###        output=output_path + '.pgp',
###        always_trust = True
###    )
    encrypted_ascii_data= gpg.encrypt(res,
        recipients=recipient_key,
        always_trust = True
    )
except Exception as e:
    print ("---- exception ----")
    print (e)

print (encrypted_ascii_data)
