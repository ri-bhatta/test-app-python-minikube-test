from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/healthz':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    server_address = ('', 80)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Starting server on port 80...')
    httpd.serve_forever()

if __name__ == '__main__':
    # Create a thread for the server
    server_thread = threading.Thread(target=run_server)

    # Start the server thread
    server_thread.start()

    # Main thread can continue with other tasks
    print("Main thread is doing something else...")

    # Wait for the server thread to finish (although it never will in this case)
    server_thread.join()
