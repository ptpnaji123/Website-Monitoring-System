from http.server import BaseHTTPRequestHandler, HTTPServer

website_status = "UP"


class WebsiteHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        global website_status

        if self.path == "/set/down":

            website_status = "DOWN"
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Website switched to DOWN")

        elif self.path == "/set/up":

            website_status = "UP"
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Website switched to UP")

        elif self.path == "/health":

            if website_status == "UP":

                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Website is healthy")

            else:

                self.send_response(503)
                self.end_headers()
                self.wfile.write(b"Website is unavailable")

        else:

            self.send_response(404)
            self.end_headers()

        print(f"Request: {self.path} | Status: {website_status}")

    def log_message(self, format, *args):
        pass


server = HTTPServer(("127.0.0.1", 8000), WebsiteHandler)

print("Test website running at http://127.0.0.1:8000")

server.serve_forever()