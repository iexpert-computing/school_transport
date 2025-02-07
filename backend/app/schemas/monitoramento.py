from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MonitoramentoBase(BaseModel):
    id_veiculo: int
    data_hora: datetime
    localizacao: Optional[str]
    evento: Optional[str]

class MonitoramentoCreate(MonitoramentoBase):
    pass

class MonitoramentoUpdate(MonitoramentoBase):
    pass

class MonitoramentoOut(MonitoramentoBase):
    id_monitoramento: int

    class Config:
        from_attributes = True  # substitui orm_mode no Pydantic v2
