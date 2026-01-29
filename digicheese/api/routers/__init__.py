from fastapi import APIRouter
from .client_router import router as router_client

router = APIRouter(prefix="/api/v1")
router.include_router(router_client)
