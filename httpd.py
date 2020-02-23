import http.server
import socketserver


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = "<html><head></head><body><h1>It works</h1></body></html>"
        self.wfile.write(bytes(html, "utf8"))
        return


if __name__ == "__main__":
    try:
        port = 8585
        with socketserver.TCPServer(("", port), RequestHandler) as httpd:
            print(f"Server started at localhost:{port}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        pass