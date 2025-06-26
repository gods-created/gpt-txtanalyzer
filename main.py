from asyncio import (
    # get_event_loop, 
    # set_event_loop,
    run
)
# from loguru import logger
from services import AIAnalyze
from typing import Optional
from json import loads

async def launch_ai_analyze(text: str):
    async with AIAnalyze() as obj:
        response = await obj.start(text)

    return response

# async def main(text: str) -> Optional[dict]:
def main(event, context) -> Optional[dict]:
    body = loads(event.get('body'))
    text = body.get('text')

    if not text:
        return None 
    
    return run(launch_ai_analyze(text))

# if __name__ == '__main__':
#     try:
#         text = input('Text: ')
#         loop = get_event_loop()
#         set_event_loop(loop)
#         loop.run_until_complete(main(text))
#         loop.close()

#     except KeyboardInterrupt:
#         pass 

#     except Exception as e:
#         logger.error(f'\main\' function execute error: {str(e)}')