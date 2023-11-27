from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import signal
import sys

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/healthz':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')

    # Use a flag to control the while loop
    running = True

    while running:
        try:
            # Handle one request at a time
            httpd.handle_request()
        except KeyboardInterrupt:
            print('Stopping server...')
            running = False

def signal_handler(sig, frame):
    # This function will be called on Ctrl+C
    sys.exit(0)

if __name__ == '__main__':
    # Register the signal handler to gracefully stop the server on Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Create a thread for the server
    server_thread = threading.Thread(target=run)

    # Start the server thread
    server_thread.start()

    # Wait for user input to stop the server
    input('Press Enter to stop the server...')

    # Set the running flag to False to stop the server
    server_thread.join()
