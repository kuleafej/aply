from pydantic import BaseModel, Field
from datetime import date


#################### TEXT COMPLETION SCHEMAS #######################
class TextCompletion(BaseModel):
    system: str
    user_message: str
