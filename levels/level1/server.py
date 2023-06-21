from http.server import HTTPServer, BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def do_GET(self):
        if self.path == '/':
            self.send_response(200, 'OK')
            pass
        else:
            self.send_response(404, 'Not found')

        # after sending the status line, we send headers
        self.send_header('Server', 'demo')
        self.end_headers()


server = HTTPServer(('', 8080), RequestHandler)

if __name__ == "__main__":
    print('Listening on port 8080')
    server.serve_forever()
