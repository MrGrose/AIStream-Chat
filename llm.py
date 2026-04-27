import logging

from gigachat import Chat, GigaChat, Messages, MessagesRole

from config import settings


payload = Chat(
    messages=[
        Messages(
            role=MessagesRole.SYSTEM,
            content=settings.system_prompt,
        )
    ],
    temperature=settings.gigachat_temperature,
)


async def get_ai_response(msg: str) -> str:
    async with GigaChat(
        credentials=settings.gigachat_api_key,
        scope=settings.gigachat_scope,
        verify_ssl_certs=False,
    ) as giga:
        
        payload.messages.append(Messages(role=MessagesRole.USER, content=msg))
        response = await giga.achat(payload)
        payload.messages.append(response.choices[0].message)
        
        return response.choices[0].message.content