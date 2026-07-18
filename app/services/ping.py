import time
import httpx


async def ping_website(url: str):
    # Add https:// if the user didn't provide a scheme
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"

    start = time.perf_counter()

    async with httpx.AsyncClient(follow_redirects=True, timeout=10) as client:
        response = await client.get(url)

    elapsed = (time.perf_counter() - start) * 1000

    return {
        "url": str(response.url),
        "status": response.status_code,
        "time": round(elapsed, 2),
    }