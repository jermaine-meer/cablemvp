# CableMVP - quick start (Windows PowerShell)

## Build & run (all services)
docker compose up -d --build

## See running containers
docker ps
docker compose ps

## View logs
docker compose logs -f web
docker compose logs -f worker
docker compose logs -f nginx

## Test endpoints
Invoke-RestMethod -Method Get -Uri "http://localhost:8000/healthz"
$res = Invoke-RestMethod -Method Post -Uri "http://localhost:8000/api/calc" -ContentType 'application/json' -Body (@{ current_a = 12; length_m = 120 } | ConvertTo-Json)

## Enqueue test Celery job
docker exec -it cablemvp-web-1 python - <<'PY'
from tasks import long_calc
r = long_calc.delay(2,3)
print("task id:", r.id)
PY

## Stop and remove containers (and volumes)
docker compose down -v
