import logging
from contextlib import suppress

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse

from config import FRONTEND_INDEX_PATH
from llm import get_ai_response

LOG_FORMAT = "%(levelname)s | %(name)s | %(message)s"
logging.basicConfig(level=logging.ERROR, format=LOG_FORMAT, datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/", response_class=FileResponse)
async def main_page() -> str:
    return FRONTEND_INDEX_PATH


@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await websocket.accept()
    with suppress(WebSocketDisconnect):
        while True:
            request_data = await websocket.receive_json()
            user_message = request_data.get("content")

            try:
                ai_answer = await get_ai_response(user_message)
            except Exception:
                logger.exception("Ошибка при получении ответа от ИИ")
                continue

            await websocket.send_json(
                {
                    "type": "ai_response_chunk",
                    "content": ai_answer,
                }
            )
