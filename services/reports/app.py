"""Готовый HTTP-адаптер. Запуск: python -m services.reports.app"""
import os
from pathlib import Path
from common.server import serve
from config import HOST, REPORTS_PORT
from .domain import ReportStore

def make_dispatch(service):
    def dispatch(method, path, body):
        if method == "GET" and path == "/reports":
            return 200, {"reports": service.list_reports()}
        if method == "POST" and path == "/reports":
            if not isinstance(body, dict) or "result" not in body:
                raise ValueError("Нужен объект с полем result")
            return 201, {"report": service.save(body["result"])}
        return 404, {"error": "Маршрут не найден"}
    return dispatch

def main():
    default = Path(__file__).resolve().parents[2] / "work_results" / "reports.json"
    service = ReportStore(os.environ.get("REPORTS_FILE", str(default)))
    serve(HOST, REPORTS_PORT, "reports", make_dispatch(service))

if __name__ == "__main__":
    main()
