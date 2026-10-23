# Задание 2. Окружение и зависимости

1. Из корня проекта создай окружение: python -m venv .venv
2. Покажи путь его интерпретатора, версию Python и список пакетов.
3. В answers.md объясни, зачем нужно окружение и почему .venv нет в Git.
4. Назови три модуля стандартной библиотеки из этого урока.
5. Объясни, почему в корневом requirements.txt нет сторонних пакетов.
6. Напиши команду установки пакетов из requirements.txt. Устанавливать дополнительные пакеты не требуется.

Windows PowerShell, без активации:

    .venv\Scripts\python -c "import sys; print(sys.executable)"
    .venv\Scripts\python --version
    .venv\Scripts\python -m pip list

macOS / Linux:

    .venv/bin/python -c "import sys; print(sys.executable)"
    .venv/bin/python --version
    .venv/bin/python -m pip list

Если команда python отсутствует на Windows, попробуй py -m venv .venv.
Версию и пути запиши по своему компьютеру, не копируй чужой вывод.
