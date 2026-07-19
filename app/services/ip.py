import httpx
import ipaddress


def is_private_ip(ip: str) -> bool:
    try:
        return ipaddress.ip_address(ip).is_private
    except ValueError:
        return False


async def lookup_ip(ip: str):
    if is_private_ip(ip):
        return {
            "status": "private",
            "message": "Private IP address"
        }

    url = f"http://ip-api.com/json/{ip}"

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(url)
        return response.json()