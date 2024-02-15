from fastapi import APIRouter
import requests
from backend import schemas
from backend import utilities
from backend import crud
from typing import Any

router = APIRouter(
    prefix="/text-completion",
    tags=["Text-Completion"]
)

#get text completed.
@router.post("/")
async def get_text_completion(user_message: schemas.TextCompletion) -> Any:
    
    completion = crud.get_completion(user_message)

    data_to_send = {"data": completion.choices[0].message.content}

    cleaned_data = requests.post(url="http://us-east1-cis655-aply.cloudfunctions.net/aply-data-cleaner/", json=data_to_send, headers= {"Content-Type": "application/json"} )

    return cleaned_data.text