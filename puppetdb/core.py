#!/usr/bin/env python
# Copyright (c) 2013 Arcus, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions
# of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import utils
import v2

class ClientException(BaseException):
    pass

class AuthException(BaseException):
    pass

class PuppetDBClient(object):
    def __init__(self, host='localhost', port=8080, api_version='v2',
        use_ssl=False):
        self._host = host
        self._port = port
        self._api_version = api_version
        ssl = {
            True: 'https',
            False: 'http',
        }
        apis = {
            'v2': v2,
        }
        self._api = apis[api_version]
        self._api_url = '{0}://{1}:{2}'.format(ssl[use_ssl], self._host, self._port)

    def get_root(self):
        return utils.api_request(self._api_url, '/')

    def get_nodes(self):
        return self._api.get_nodes(self._api_url)

    def get_node(self, name=None):
        return self._api.get_node(self._api_url, name)

    def get_node_facts(self, name=None):
        return self._api.get_node_facts(self._api_url, name)

    def get_node_fact(self, name=None, fact_name=None):
        return self._api.get_node_fact(self._api_url, name, fact_name)