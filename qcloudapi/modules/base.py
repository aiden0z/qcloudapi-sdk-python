# -*- coding: utf-8 -*-

import copy
import time
import random

from ..common.request import Request


class Base(object):

    requestHost = ''
    requestUri = '/v2/index.php'
    _params = {}

    def __init__(self, config):
        self.secretId = config['secretId']
        self.secretKey = config['secretKey']
        self.defaultRegion = config['Region']
        self.method = config['method']

    def _checkParams(self, action, params):
        self._params = copy.deepcopy(params)
        self._params['Action'] = action[0].upper() + action[1:]

        if 'Region' not in self._params:
            self._params['Region'] = self.defaultRegion

        if 'SecretId' not in self._params:
            self._params['SecretId'] = self.secretId

        if 'Nonce' not in self._params:
            self._params['Nonce'] = random.randint(1, 2 ** 50)

        if 'Timestamp' not in self._params:
            self._params['Timestamp'] = int(time.time())

        return self._params

    def generateUrl(self, action, params):
        self._checkParams(action, params)
        request = Request(self.secretId, self.secretKey)
        return request.generateUrl(self.requestHost, self.requestUri,
                                   self._params, self.method)

    def call(self, action, params, files={}):
        self._checkParams(action, params)
        request = Request(self.secretId, self.secretKey)
        return request.send(self.requestHost, self.requestUri, self._params,
                            files, self.method)
