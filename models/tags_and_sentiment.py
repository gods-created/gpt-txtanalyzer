from pydantic import BaseModel
from typing import List

class Tag(BaseModel):
    value: str

class TagsAndSentiment(BaseModel):
    tags: List[Tag]
    sentiment: str