from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import atexit

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
    httpd.serve_forever()

def run_server():
    run()

# Register the cleanup function with atexit
atexit.register(run_server)

if __name__ == '__main__':
    # Create a thread for the server
    server_thread = threading.Thread(target=run_server)

    # Start the server thread
    server_thread.start()

    # Main thread can continue with other tasks
    print("Main thread is doing something else...")

    # The main thread can now safely exit without affecting the server thread
