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

## Continuous integration

Pull requests targeting `main` run the pytest suite and a non-publishing container build. Pushes to `main` repeat validation, authenticate to AWS through GitHub OIDC, and publish exactly one immutable ECR image tagged `<VERSION>-<7-character-git-hash>`. `VERSION` is the semantic-version source and changes are made deliberately through a pull request.

Configure the Actions variables `AWS_REGION` and `AWS_ECR_PUBLISH_ROLE_ARN` at repository or organization scope. The role ARN is configuration, not a secret; no static AWS credentials are stored. CI does not deploy to EKS. Deployment is handled later through Argo CD.
