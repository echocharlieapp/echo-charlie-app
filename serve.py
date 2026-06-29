import os, http.server, socketserver

port = int(os.environ.get('PORT', 3456))
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('', port), Handler) as httpd:
    print(f'Serving on port {port}')
    httpd.serve_forever()
