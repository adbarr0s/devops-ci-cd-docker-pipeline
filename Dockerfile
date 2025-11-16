# ------------------------
#   STAGE 1 — Builder
# ------------------------
FROM python:3.10-slim AS builder

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --user -r requirements.txt


# ------------------------
#   STAGE 2 — Runtime
# ------------------------
FROM python:3.10-slim

WORKDIR /app

# Copia as libs instaladas no builder
COPY --from=builder /root/.local /root/.local

# Copia o código da aplicação
COPY app/ ./app/

ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000

# Comando default
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
