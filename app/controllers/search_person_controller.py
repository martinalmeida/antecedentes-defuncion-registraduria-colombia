from app.services.backgrounds_service import BackgroundService
from app.services.death_service import DeathService

class SearchPersonController:

    def __init__(self):
        self.background_service = BackgroundService()
        self.death_service = DeathService()

    async def send_search(self, payload: dict):
        try:
            background = await self.background_service.search_background(payload)
            death = await self.death_service.search_death(payload)
            return {
                "status": "success",
                "data": {
                    "background": background,
                    "death": death
                }
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }