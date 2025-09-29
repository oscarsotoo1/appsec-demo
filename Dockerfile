# ----- build -----
FROM python:3.11-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -t /deps
COPY . .

# ----- run (distroless) -----
FROM gcr.io/distroless/python3-debian12
WORKDIR /app
COPY --from=build /deps /deps
ENV PYTHONPATH=/deps
COPY app ./app
USER 65532:65532
EXPOSE 8000
CMD ["-m","uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
