import httpx

class SearchPersonService:

    async def search_person(self, payload: dict):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post("v1/bills/validate", json=payload)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise Exception(e.response.json())