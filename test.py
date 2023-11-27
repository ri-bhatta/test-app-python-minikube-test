from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import signal
import sys
import time

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

    # Main thread can continue with other tasks
    print("Main thread is doing something else...")

    # Sleep for demonstration purposes
    time.sleep(10)

    # The main thread will now interrupt the server thread
    server_thread.join()
