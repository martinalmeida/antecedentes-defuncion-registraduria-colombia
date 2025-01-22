from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr

class BillingPeriodSchema(BaseModel):
    start_date: str = Field(..., example="2024-01-10")
    start_time: str = Field(..., example="00:00:00")
    end_date: str = Field(..., example="2024-02-09")
    end_time: str = Field(..., example="23:59:59")

class WithholdingTaxSchema(BaseModel):
    code: str = Field(..., example="06")
    withholding_tax_rate: str = Field(..., example="7.00")

class ItemSchema(BaseModel):
    code_reference: str = Field(..., example="12345", min_length=1, max_length=50)
    name: str = Field(..., example="producto de prueba", min_length=1, max_length=100)
    quantity: int = Field(..., example=1, ge=1)
    discount_rate: float = Field(..., example=20.0, ge=0.0, le=100.0)
    price: float = Field(..., example=50000.0, ge=0.0)
    tax_rate: str = Field(..., example="19.00")
    unit_measure_id: int = Field(..., example=70)
    standard_code_id: int = Field(..., example=1)
    is_excluded: int = Field(..., example=0)  # 0 = No, 1 = Yes
    tribute_id: int = Field(..., example=1)
    withholding_taxes: List[WithholdingTaxSchema] = Field(..., example=[
        {"code": "06", "withholding_tax_rate": "7.00"},
        {"code": "05", "withholding_tax_rate": "15.00"}
    ])

class CustomerSchema(BaseModel):
    identification: str = Field(..., example="123456789", min_length=1, max_length=50)
    dv: str = Field(..., example="3", min_length=1, max_length=1)
    company: Optional[str] = Field(None, example="")
    trade_name: Optional[str] = Field(None, example="")
    names: str = Field(..., example="Alan Turing", min_length=1, max_length=100)
    address: str = Field(..., example="calle 1 # 2-68", min_length=1, max_length=100)
    email: EmailStr = Field(..., example="alanturing@enigmasas.com")
    phone: str = Field(..., example="1234567890", min_length=7, max_length=15)
    legal_organization_id: str = Field(..., example="2")
    tribute_id: str = Field(..., example="21")
    identification_document_id: str = Field(..., example="3")
    municipality_id: str = Field(..., example="980")

class InvoiceSchema(BaseModel):
    numbering_range_id: int = Field(..., example=4)
    reference_code: str = Field(..., example="I3", min_length=1, max_length=20)
    observation: Optional[str] = Field(None, example="")
    payment_form: str = Field(..., example="1")
    payment_due_date: str = Field(..., example="2024-12-30")
    payment_method_code: str = Field(..., example="10")
    billing_period: BillingPeriodSchema = Field(...)
    customer: CustomerSchema = Field(...)
    items: List[ItemSchema] = Field(...)