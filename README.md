# AIStream Chat

Веб-чат на `FastAPI` с `WebSocket` и генерацией ответов через `GigaChat`.

## Демонстрация
![demo](demo.gif)


## Что делает проект

- Принимает сообщения от клиента через `WebSocket`.
- Отправляет запрос в `GigaChat`.
- Возвращает ответ в формате чанка `ai_response_chunk`.




## Требования

- Python `3.12+`.
- `uv` для установки зависимостей и запуска.

## Установка

```bash
uv sync
```

## Настройка окружения

1. Скопируйте шаблон:

```bash
cp .env.example .env
```

2. Заполните `.env`:

```env
GIGACHAT_API_KEY=your_api_key
GIGACHAT_SCOPE=GIGACHAT_API_PERS
GIGACHAT_TEMPERATURE=0.7
SYSTEM_PROMPT=Ваш системный промпт
```

## Запуск

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Сервис будет доступен по адресу [http://localhost:8000](http://localhost:8000).


## Логи

- В терминал выводятся только сообщения уровня `ERROR`.
- Ошибки запросов к `GigaChat` пишутся с traceback.

## Структура

- `main.py` - роуты FastAPI и `WebSocket`-обработчик.
- `llm.py` - интеграция с `GigaChat`.
- `config.py` - настройки и переменные окружения через `pydantic-settings`.
- `frontend/index.html` - собранный фронтенд.
