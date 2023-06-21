from http.server import HTTPServer, BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def do_GET(self):
        if self.path == '/redirect':
            self.send_response(302, 'Found')
            self.send_header('Location', 'https://devopsdays.org/events/2023-amsterdam/welcome/')
        else:
            self.send_response(404, 'Not found')

        # after sending the status line, we send headers
        self.send_header('Server', 'demo')
        self.end_headers()


server = HTTPServer(('', 8080), RequestHandler)

if __name__ == "__main__":
    print('Listening on port 8080')
    server.serve_forever()
