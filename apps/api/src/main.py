from fastapi import FastAPI

from .routers.users import router as users_router

app = FastAPI(title="CogniHire API", version="0.1.0")
app.include_router(users_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
