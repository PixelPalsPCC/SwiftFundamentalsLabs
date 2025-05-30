# example web server written in python3

from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handles GET requests."""
        self.send_response(200)  # Send a 200 OK status code
        self.send_header('Content-type', 'text/html')  # Set content type header
        self.end_headers()  # End of headers

        # Write the response body
        self.wfile.write(b"<html><body><h1>Hello Pixel Pals PCC Mac Nerds!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """Starts the HTTP server."""
    server_address = ('', port)  # Listen on all available interfaces
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}...")
    httpd.serve_forever()  # Start serving requests indefinitely

if __name__ == '__main__':
    run()