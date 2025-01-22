from app.services.search_person_service import SearchPersonService

class SearchPersonController:

    def __init__(self):
        self.search_person_service = SearchPersonService()

    async def send_search(self, payload: dict):
        try:
            response = await self.search_person_service.search_person(payload)
            return {
                "status": "success",
                "data": response
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }