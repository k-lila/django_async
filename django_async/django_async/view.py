import asyncio
import httpx
from django.http import HttpResponse
from datetime import datetime, timedelta

# def api(request):
#     time.sleep(1)
#     payload = {"message": "Hi!"}

#     if "task_id" in request.GET:
#         payload["task_id"] = request.GET["task_id"]
#     return JsonResponse(payload)


async def speed_tracker():
    now = datetime.now()
    speed = 0.03
    size = 50
    print()
    print()
    print("  speed tracker  ".center(53, "="))
    print()
    print(f" | 0 ms")
    for num in range(0, size):
        dif = datetime.now() - now
        dif = round(dif.total_seconds() * 1000, 3)
        print(f" | {dif}ms")
        await asyncio.sleep(speed)
        print
    print("=" * 53)


async def http_call_async():
    asyncio.create_task(speed_tracker())
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org")
        print(f"{response}".rjust(45, "-"))


async def async_view(request):
    asyncio.create_task(http_call_async())
    return HttpResponse(
        f"função assíncrona executada às {(datetime.now() - timedelta(hours=3)).time()}"
    )
