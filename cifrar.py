#!/usr/bin/env python3

import sys
import hashlib

def enMD5(cad1):
    token = hashlib.md5()
    token.update(cad1.encode('utf-8'))
    pass1 = token.hexdigest()
    return pass1

def enSHA1(cad1):
    token = hashlib.sha1()
    token.update(cad1.encode('utf-8'))
    pass1 = token.hexdigest()
    return pass1

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("En MD5: "+enMD5(sys.argv[1]))
        print("En SHA1: "+enSHA1(sys.argv[1]))
