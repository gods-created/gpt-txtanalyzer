from models import TagsAndSentiment
from enums import SentimentsEnum
from openai import (
    OpenAI, 
    APIConnectionError, 
    PermissionDeniedError,
    APIStatusError,
    RateLimitError,
    ConflictError,
    OpenAIError
)
from os import getenv
from loguru import logger
from sys import getsizeof

class AIAnalyze:
    def __init__(self):
        self.openai_client = None
        self.openai_api_key = getenv('OPENAI_API_KEY')
        self.opena_ai_model = getenv('OPENAI_MODEL')
        self.sentiment_values = [each.value for each in SentimentsEnum]
        self.max_obj_size = 2056

    async def __aenter__(self):
        try:
            self.openai_client = OpenAI(
                api_key=self.openai_api_key
            )
        except OpenAIError as e:
            logger.error(str(e))

        return self
    
    async def start(self, text: str) -> dict:
        response_json = {}

        try:
            if not all((
                self.openai_client,
                self.opena_ai_model
            )):
                raise ValueError('\'OPENAI_API_KEY\' or/and \'OPENAI_MODEL\' (environment variables) is/are empty or invalid.')

            if (text_size := getsizeof(text)) > self.max_obj_size:
                raise ValueError(f'The max. text size is {self.max_obj_size}KB. Current text size is {text_size}KB.')

            response = self.openai_client.responses.parse(
                model=self.opena_ai_model,
                input=[
                    {
                        'role': 'system',
                        'content': f'You need to read the text and determine its sentiment ({", ".join(self.sentiment_values)}), ' \
                                   'as well as select appropriate tags for it at your discretion.',
                    },
                    {'role': 'user', 'content': text},
                ],
                text_format=TagsAndSentiment,
            )

            response_json = response.output_parsed
            
        except (
            APIConnectionError, 
            PermissionDeniedError,
            APIStatusError,
            RateLimitError,
            ConflictError,
            OpenAIError,
            ValueError,
        ) as e:
            class_name = e.__class__.__name__
            logger.error(f'\'AIAnalyze.start\' method execute error ({class_name}): {str(e)}')

        except Exception as e:
            logger.error(f'\'AIAnalyze.start\' method execute error: {str(e)}')

        finally:
            return response_json
    
    async def __aexit__(self, *args, **kwargs):
        if self.openai_client:
            self.openai_client.close()