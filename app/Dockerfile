# -------- Build Stage --------
FROM python:3.13-slim AS builder

WORKDIR /build

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

COPY . .


# -------- Runtime Stage --------
FROM python:3.13-slim

WORKDIR /app

# Create a non-root user
RUN groupadd --system appuser && \
    useradd --system --gid appuser appuser

# Copy installed Python packages
COPY --from=builder /install /usr/local

# Copy application
COPY --from=builder /build/app.py ./app.py

# Give application user ownership of application directory
RUN chown -R appuser:appuser /app

# Switch from root to non-root user
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
