import asyncio
import logging

from envs import APP_LOGGER_NAME
from logging_setup import load_logger_config

load_logger_config()

logger = logging.getLogger(APP_LOGGER_NAME)


async def main():
    logger.info("hello")

asyncio.run(main())
