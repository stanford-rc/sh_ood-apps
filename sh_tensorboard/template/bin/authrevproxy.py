#!/usr/bin/python

# provides a reverse proxy that only allows requests coming from the same
# user it's running as
#
# grant access based on the presence of a _ood_token_<session_id>=<password>
# cookie, where:
#  <session_id> is the OnDemand Session id
#  <password> is the password defined in the template/before.sh script

from twisted.internet import reactor, endpoints
from twisted.web import proxy, server
from twisted.web.resource import Resource
from twisted.web.error import ForbiddenResource

import argparse
import getpass
import sys, os


#
# ReverseProxy Resource that checks cookie before forwarding requests
#
class TokenResource(Resource):

    def __init__(self, host, port, path):
            Resource.__init__(self)
            self.host = host
            self.port = port
            self.path = path

    def getChild(self, path, request):

        # get username from headers
        # - this should be set on authenticated web sessions
        try:
            user = request.getHeader("x-forwarded-user")
        except:
            user = None

        # check if the request comes from the right user (note: can be forged)
        if user == getpass.getuser():

            # get ood token cookie
            # - cookie name depends on the ood interactive session id ($PWD)
            ood_session_id = os.path.basename(os.getcwd())
            try:
                cookie = request.getCookie('_ood_token_' + ood_session_id)

            except:
                cookie = None

            # get token from environment
            # - $_ood_token_<session_id> is set in template/before.sh script
            try:
                ood_token = os.environ.get("_ood_token_" +
                                           ood_session_id.replace("-", "_"))
            except:
                ood_token = None

            # check that cookie matches the local token
            if cookie == ood_token and cookie != None:
                return proxy.ReverseProxyResource(self.host,
                                                  self.port,
                                                  '/' + path)

        # no cheese for you
        request.setResponseCode(403)
        return ForbiddenResource()


#
# parse arguments
#
def parse_args(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Token Revproxy')
    parser.add_argument('--app-port', dest='app_port', type = int,
                        required = True, help='application port, to forward requests to')
    parser.add_argument('--proxy-port', dest='proxy_port', type = int,
                        required = True, help='proxy port, to listen for requests on')
    args = parser.parse_args(argv)
    return args

#
# entry point
#
def main(argv=sys.argv[1:]):
    args = parse_args(argv)
    print('authrevproxy is starting on port {} -> {}'.format(args.proxy_port,
                                                             args.app_port) )
    dest = TokenResource('127.0.0.1', args.app_port, '')
    site = server.Site(dest)

    endpoint = endpoints.TCP4ServerEndpoint(reactor, args.proxy_port)
    endpoint.listen(site)
    reactor.run()


if __name__ == '__main__':
    main()

