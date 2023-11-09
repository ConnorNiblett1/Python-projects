# Python 3 server example
from  http.server import BaseHTTPRequestHandler, HTTPServer 
import time 

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler): 
    def do_GET(self): 
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Hello world! This is a webpage!</p>", "utf-8"))
        self.wfile.write(bytes("<p> And hello to you! Please enter your name below!</p>", "utf-8"))
        self.wfile.write(bytes("""<form action="/" method="post">
                                   <label for="name">Please enter your name:</label><br>
                                   <input type="text" id="name" name="name"><br>
                                   <input type = "submit" value = "Click me!">
                                </form>  
                              """, "utf-8" )) 
        self.wfile.write(bytes())
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self): 
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
       
        user_input = post_data.split('=')[1]

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes("html>head>title>https://pythonbasics.org</title>/head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes(f"<p>Hello {user_input}!</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":     
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt: 
        pass

    webServer.server_close()
    print("Server stopped.")

   
