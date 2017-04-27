# -*- coding: utf-8 -*-

import base64
import hashlib
import hmac
from argparse import ArgumentParser

class BaseUrlSigner(object):
    def __init__(self, security_key):
        if isinstance(security_key, unicode):
            security_key = security_key.encode('utf-8')
        self.security_key = security_key

    def validate(self, actual_signature, url):
        url_signature = self.signature(url)
        return url_signature == actual_signature

    def signature(self, url):
        raise NotImplementedError()

class UrlSigner(BaseUrlSigner):
    """Validate urls and sign them using base64 hmac-sha1
    """

    def signature(self, url):
        return base64.urlsafe_b64encode(
            hmac.new(
                self.security_key, unicode(url).encode('utf-8'), hashlib.sha1
            ).digest()
        )

if __name__ == '__main__':
    options = ArgumentParser()
    options.add_argument('-s', '--sitename', action='store', dest='site', 
                         help='this program will securize url')
    args = options.parse_args()
    site = args.site
    security_key = 'BOTEZu^p_EH+(G5hf5in'
    BaseUrlSigner(security_key)
    safeurl = UrlSigner().signature(site)
    print safeurl
