import uvicorn
from fastapi import FastAPI


def get_fastapi() -> FastAPI:
    app = FastAPI(
        # Titles, summary, debug, etc...
    )
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
    