import http.server
import socketserver


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == '/':
                html = "<html><head></head><body><h1>It works</h1></body></html>"
            elif self.path == '/health':
                html = "<html><head></head><body><h1>I'm alive~</h1></body></html>"
            else:
                raise Exception('Not Found')
        except Exception:
            html = "<html><head></head><body><h1>Not Found</h1></body></html>"
            self.send_response(404)
        else:
            self.send_response(200)
        finally:
            self.send_header("Content-type", "text/html")
            self.end_headers()

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
