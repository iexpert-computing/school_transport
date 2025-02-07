from pydantic import BaseModel
from datetime import date

class PagamentoCreate(BaseModel):
    id_contrato: int
    valor_pago: float
    data_pagamento: date

class PagamentoUpdate(BaseModel):
    id_contrato: int
    valor_pago: float
    data_pagamento: date

class PagamentoResponse(BaseModel):
    id_pagamento: int
    id_contrato: int
    valor_pago: float
    data_pagamento: date

    class Config:
        from_attributes = True
