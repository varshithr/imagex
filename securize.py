#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:15:17 2017

@author: varshith
"""

import base64
import hashlib
import hmac
from argparse import ArgumentParser
from urllib2 import quote

def signature(url, security_key):
        return base64.urlsafe_b64encode(
            hmac.new(
                security_key, unicode(url).encode('utf-8'), hashlib.sha1
            ).digest()
        )
            
if __name__ == '__main__':
    options = ArgumentParser()
    options.add_argument('-s', '--sitename', action='store', dest='site', 
                         help='this program will securize url')
    args = options.parse_args()
    site = args.site
    site = quote(site)
    security_key = 'BOTEZu^p_EH+(G5hf5in'
    safeurl = signature(site, security_key)
    print safeurl, site