# -*- coding: utf-8 -*-

import urllib
import requests

from .sign import sign


class Request(object):

    timeout = 10
    version = 'SDK_PYTHON_1.1'

    def __init__(self, secretId, secretKey):
        self.secretId = secretId
        self.secretKey = secretKey

    def generateUrl(self, requestHost, requestUri, params, method='GET'):

        params['RequestClient'] = self.version
        params['Signature'] = sign(self.secretKey, requestHost,
                                   requestUri, params, method)
        params = urllib.urlencode(params)

        url = 'https://%s%s' % (requestHost, requestUri)
        if method.upper() == 'GET':
            url += '?' + params
        return url

    def send(self, requestHost, requestUri, params, files={}, method='GET'):

        params['RequestClient'] = self.version
        params['Signature'] = sign(self.secretKey, requestHost,
                                   requestUri, params, method)
        url = 'https://%s%s' % (requestHost, requestUri)

        if method.upper() == 'GET':
            req = requests.get(url, params=params,
                               timeout=self.timeout, verify=False)
        else:
            req = requests.post(url, data=params, files=files,
                                timeout=self.timeout, verify=False)

        if req.status_code != requests.codes.ok:
            req.raise_for_status()

        return req.text
