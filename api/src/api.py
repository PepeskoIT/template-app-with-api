import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from envs import APP_LOGGER_NAME


logger = logging.getLogger(APP_LOGGER_NAME)

router = APIRouter()

SERVICE_STATUS_PATH = "/"


@router.get(SERVICE_STATUS_PATH)
async def get_status() -> JSONResponse:
    """Return backend status message.

    Returns:
        JSONResponse: backend status message
    """
    return {"message": "Backend service is available"}
