from fastapi import APIRouter, Header
from app.controllers.search_person_controller import SearchPersonController
from app.schemas.invoice_schema import InvoiceSchema

class Router:

    def __init__(self):
        self.router = APIRouter()
        self.search_person = SearchPersonController()
        self._register_routes()
    
    def _register_routes(self):
        
        @self.router.post("/test-search-person")
        async def create_invoice(invoice: InvoiceSchema):
            return await self.search_person.send_search(invoice.model_dump())

router = Router().router