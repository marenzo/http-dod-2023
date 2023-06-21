from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime, timezone, timedelta
from email.utils import format_datetime


class RequestHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def do_GET(self):
        body = '<html><body><p>{}</p></body></html>'.format(datetime.now().isoformat()).encode('utf-8')
        # send a 200 OK response with body with caching headers
        if self.path == '/':
            self.send_response(200, 'OK')
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Server', 'demo')
            # TODO: caching headers. Use the format_date function to easily write header dates
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404, 'Not found')
            # after sending the status line, we send headers
            self.send_header('Server', 'demo')
            self.end_headers()


server = HTTPServer(('', 8080), RequestHandler)

if __name__ == "__main__":
    print('Listening on port 8080')
    server.serve_forever()
