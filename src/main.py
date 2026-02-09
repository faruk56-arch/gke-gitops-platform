from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = FastAPI(title="myapp")

# Metrics (Prometheus)
REQUESTS = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["app", "method", "path", "status"],
)

LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency in seconds",
    ["app", "path"],
)

APP_NAME = "myapp"

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/")
def root():
    start = time.time()
    status = 200

    # Simulate variable latency (for demo)
    time.sleep(random.uniform(0.01, 0.12))

    duration = time.time() - start
    LATENCY.labels(app=APP_NAME, path="/").observe(duration)
    REQUESTS.labels(app=APP_NAME, method="GET", path="/", status=str(status)).inc()

    return {"message": "hello from myapp", "latency_s": duration}

@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)
