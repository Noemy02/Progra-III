from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import parse
import crud_materias
import json

crud_materias = crud_materias.crud_materias()
port = 1000

class miServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "index.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        
        if self.path=="/frmmaterias":
            self.path = "materias.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        
        if self.path=="/frmbusqueda_materias":
            self.path = "busqueda_materias.html"
            return SimpleHTTPRequestHandler.do_GET(self)
       
        if self.path=="/materias":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(crud_materias.consultar_materias()).encode('utf-8'))

    def do_POST(self):
        longitud = int(self.headers["Content-Length"])
        datos= self.rfile.read(longitud)
        datos = datos.decode()
        datos = parse.unquote(datos)
        datos = json.loads(datos)
        if self.path=="/materias":
            resp = {"msg": crud_materias.administrar(datos)}
        if self.path=="/buscar_materias":
            resp = crud_materias.consultar_materias(datos)
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(resp).encode())
        
print("Ejecuntando server en puerto ", port)
server = HTTPServer(("localhost", port), miServer)
server.serve_forever()