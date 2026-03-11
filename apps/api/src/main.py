from fastapi import FastAPI

from .routers.onet import router as onet_router
from .routers.users import router as users_router

app = FastAPI(title="CogniHire API", version="0.2.0")
app.include_router(users_router)
app.include_router(onet_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
