from pydantic import BaseModel


class NewRowData(BaseModel):
    last_name: str
    first_name: str
    patronymic: str
    name_of_organization: str
    work_phone: str
    personal_phone_mobile: str
