# -*- coding: utf-8 -*-

import hmac
import binascii
import hashlib


def sign(secretKey, requestHost, requestUri, params, method='GET'):
    d = {}
    for key in params:
        if method == 'post' and str(params[key])[0:1] == '@':
            continue
        d[key] = params[key]

    srcStr = method.upper() + requestHost + requestUri + '?'
    srcStr += '&'.join('%s=%s' %
                       (k.replace('_', '.'), d[k]) for k in sorted(d.keys()))

    hashed = hmac.new(secretKey.encode('utf-8'),
                      srcStr.encode('utf-8'), hashlib.sha1)

    return binascii.b2a_base64(hashed.digest())[:-1].decode('utf-8')
