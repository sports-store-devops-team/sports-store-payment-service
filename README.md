# Sports Store Payment Service

FastAPI mock payment service used by checkout. It listens on port `8005`; health is available at `GET /health`.

## Configuration

| Variable | Required | Purpose |
| --- | --- | --- |
| `MONGO_URI` | Yes | MongoDB connection URI for the payment database. |
| `JWT_SECRET` | Yes | Shared JWT verification secret. |
| `JWT_ALGORITHM` | No | JWT algorithm (default `HS256`). |
| `PAYMENT_FAILURE_SUFFIX` | No | Development-only card suffix that simulates decline (default `0000`). |

`.env.example` contains development-only placeholders. Do not use them in production.

## Build and test

```sh
docker build -t sports-store/payment-service:0.1.0 .
python -m pytest
```

Run locally with `uvicorn main:app --host 0.0.0.0 --port 8005`.
