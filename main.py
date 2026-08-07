import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import payments_collection
from observability import configure_observability
from routes import payments

logger = logging.getLogger("payment-service")

app = FastAPI(title="Sports Store — Payment Service")
configure_observability(app, "payment-service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(payments.router, prefix="/api")


@app.on_event("startup")
async def create_indexes():
    try:
        await payments_collection.create_index("idempotency_key", unique=True)
    except Exception:  # Mongo may be unavailable (e.g. unit tests)
        logger.warning(
            "database_index_creation_skipped",
            extra={"event": "database_index_creation_skipped"},
        )


@app.get("/health")
def health():
    return {"status": "ok", "service": "payment-service"}
