"""Готовая учебная HTTP-обвязка. Каждый процесс обслуживает свой порт."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlsplit

class BadRequest(ValueError):
    pass

def create_server(host, port, service_name, dispatch):
    class Handler(BaseHTTPRequestHandler):
        def send_json(self, status, data):
            payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def read_json(self):
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 1_000_000:
                    raise BadRequest("Нужен JSON-запрос размером до 1 МБ")
                return json.loads(self.rfile.read(length).decode("utf-8"))
            except (ValueError, UnicodeDecodeError) as error:
                raise BadRequest("Неверный JSON в теле запроса") from error

        def handle_request(self):
            path = urlsplit(self.path).path
            if self.command == "GET" and path == "/health":
                self.send_json(200, {"service": service_name, "status": "ok"})
                return
            try:
                body = self.read_json() if self.command == "POST" else None
                status, result = dispatch(self.command, path, body)
            except NotImplementedError as error:
                status, result = 501, {"error": str(error)}
            except json.JSONDecodeError:
                status, result = 500, {"error": "Повреждён JSON-файл сервиса"}
            except ValueError as error:
                status, result = 400, {"error": str(error)}
            except (OSError, KeyError, TypeError) as error:
                status, result = 500, {"error": f"Ошибка данных сервиса: {type(error).__name__}"}
            self.send_json(status, result)

        do_GET = handle_request
        do_POST = handle_request

        def do_PUT(self):
            self.send_json(405, {"error": "Метод не поддерживается"})
        do_DELETE = do_PUT
        do_PATCH = do_PUT

        def log_message(self, format, *args):
            pass
    return HTTPServer((host, port), Handler)

def serve(host, port, name, dispatch):
    with create_server(host, port, name, dispatch) as server:
        print(f"{name}: http://{host}:{port}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
