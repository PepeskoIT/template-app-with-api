from fastapi import FastAPI
from logging_setup import load_logger_config

import api

load_logger_config()


def create_app():
    app_ = FastAPI(docs_url="/docs")
    app_.include_router(api.router)
    return app_


app = create_app()
