import uvicorn
from fastapi import FastAPI

from . import example


def setup_routers(app: FastAPI) -> None:
    app.include_router(example.router, prefix='/example')


def get_fastapi() -> FastAPI:
    app = FastAPI(
        # Titles, summary, debug, etc...
    )

    setup_routers(app)

    return app


async def run_api(
    host: str = '127.0.0.1',
    port: int = 8000,
) -> None:
    app = get_fastapi()
    
    uv_cfg = uvicorn.Config(
        app=app,
        host=host,
        port=port
    )
    await uvicorn.Server(uv_cfg).serve()
    