import httpx

class DeathService:

    async def search_death(self, payload: dict):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post("https://defunciones.registraduria.gov.co:8443/VigenciaCedula/consulta", json={
                    "nuip": payload["id_card"],
                    "ip": payload["ip_address"]
                })
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise Exception(e.response.json())