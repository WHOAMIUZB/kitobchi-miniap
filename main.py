import asyncio
import logging

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from config import PORT
from database import init_db
from miniapp.api import router as miniapp_router

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Kitoblar — Mini App")
app.include_router(miniapp_router, prefix="/api")
app.mount("/", StaticFiles(directory="miniapp/static", html=True), name="miniapp-static")


@app.on_event("startup")
async def on_startup():
    await init_db()
    logging.info("Baza tayyorlandi, Mini App ishga tushdi.")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
