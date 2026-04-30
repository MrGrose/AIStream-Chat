from collections.abc import AsyncGenerator

from gigachat import Chat, GigaChat, Messages, MessagesRole

from config import settings


async def get_ai_response(msg: str) -> AsyncGenerator[str, None]:
    payload = Chat(
        messages=[
            Messages(
                role=MessagesRole.SYSTEM,
                content=settings.system_prompt,
            ),
            Messages(
                role=MessagesRole.USER,
                content=msg,
            ),
        ],
        temperature=settings.gigachat_temperature,
    )

    async with GigaChat(
        credentials=settings.gigachat_api_key,
        scope=settings.gigachat_scope,
        verify_ssl_certs=False,
    ) as giga:
        async for chunk in giga.astream(payload):
            if chunk.choices and chunk.choices[0].delta:
                text = chunk.choices[0].delta.content or ""
                if text:
                    yield text
