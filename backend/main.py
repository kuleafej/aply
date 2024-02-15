from fastapi import Depends, FastAPI
from backend.routers import text_completion_router


app = FastAPI(
    title="For Job Applicants",
    description="Assists in Job Applicantions",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Joachim Kuleafenu",
        "email": "kuleafenujoachim@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
    },
)


app.include_router(text_completion_router.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}