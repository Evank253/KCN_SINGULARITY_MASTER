# Deploy KCN Singularity Master

## Legal reminder

**Tools only.** You are responsible for what you build and deploy. See `USER_AGREEMENT.md`.

## Local API (scaffold)

```bash
cd KCN_SINGULARITY_MASTER
pip install -r 05_CODEBASES/backend/requirements.txt
export PYTHONPATH=.
uvicorn 05_CODEBASES.backend.app.main:app --host 0.0.0.0 --port 8000
# Docs: http://localhost:8000/docs
```

## Tests

```bash
cd KCN_SINGULARITY_MASTER
python -m pytest tests/ -v
```

## Demo

```bash
python demo_core.py
```

## Public cloud deploy

This repository is a **scaffold**. For a public URL:

1. Connect this GitHub repo to Railway, Render, or Fly.io
2. Set start command: `uvicorn 05_CODEBASES.backend.app.main:app --host 0.0.0.0 --port $PORT`
3. Set `PYTHONPATH` to the repo root

No production secrets or cloud credentials are included. You own any deployment.

## GitHub

https://github.com/Evank253/KCN_SINGULARITY_MASTER
