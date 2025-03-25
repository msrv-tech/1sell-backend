# integrations/ozon.py
from httpx import AsyncClient


class OzonAPI:
    def __init__(self, api_key):
        self.client = AsyncClient(base_url="https://api.ozon.ru")
        self.headers = {"Authorization": f"Ozon {api_key}"}

    async def get_orders(self):
        return await self.client.get("/v1/orders", headers=self.headers)