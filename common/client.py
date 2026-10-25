"""Готовый HTTP-клиент. Бизнес-логика сервисов сюда не импортируется."""
import json
from urllib.error import HTTPError, URLError
from urllib.request import ProxyHandler, Request, build_opener

class ClientError(RuntimeError):
    pass

def request_json(method, url, data=None, timeout=3):
    payload = None if data is None else json.dumps(data, ensure_ascii=False).encode("utf-8")
    request = Request(url, data=payload, method=method,
                      headers={"Content-Type": "application/json; charset=utf-8"})
    # Учебные адреса локальные, системный HTTP-прокси не требуется.
    opener = build_opener(ProxyHandler({}))
    try:
        with opener.open(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise ClientError(f"{method} {url}: HTTP {error.code}: {detail}") from error
    except (URLError, TimeoutError, OSError) as error:
        raise ClientError(f"Сервис недоступен: {url}. Проверь запуск и порт. {error}") from error
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise ClientError(f"Сервис вернул неверный JSON: {url}") from error
