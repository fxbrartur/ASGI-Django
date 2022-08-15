import asyncio
from time import sleep
import httpx
from django.http import HttpResponse


async def http_async_call():
    for num in range(1,5):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


def http_sync_call():
    for num in range(1,5):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_async_call())
    return HttpResponse("Essa é minha view async")


def sync_view(request):
    http_sync_call()
    return HttpResponse("Essa é minha view sync")