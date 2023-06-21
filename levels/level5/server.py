#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler

allowed_domains = {
    "domain1.com": "Hello Domain1",
    "domain2.com": "Hello Domain2"
}


class RequestHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def do_GET(self):
        self.route()

    def route(self):
        if self.is_domain_allowed():
            content = self.get_domain_content()
            body = '<html><body><p>{}</p></body></html>'.format(content).encode('utf-8')

            self.send_response(200, 'OK')
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Server', 'demo')
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(400, 'Bad Request')
            self.end_headers()

    def is_domain_allowed(self):
        hostname = self.headers['Host'].split(':')[0]
        return hostname in allowed_domains.keys()

    def get_domain_content(self):
        hostname = self.headers['Host'].split(':')[0]
        return allowed_domains[hostname]


server = HTTPServer(('', 8080), RequestHandler)

if __name__ == "__main__":
    print('Listening on port 8080')
    server.serve_forever()
