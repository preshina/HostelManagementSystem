from pydantic import BaseModel, Field
from enum import Enum
from datetime import date


class PaymentStatus(str, Enum):
    paid = "paid"
    unpaid = "unpaid"
    partial = "partial"


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)

    phone: str


class StudentResponse(BaseModel):
    id: int
    name: str

    phone: str

    class Config:
        from_attributes = True


class PaymentCreate(BaseModel):
    month: date
    amount_paid: int
    payment_date: date


class PaymentList(BaseModel):
    payments: list[PaymentCreate]


class PaymentResponse(BaseModel):
    id: int
    student_id: int
    month: date
    amount_paid: int
    due_amount: int
    balance: int
    payment_date: date
    status: PaymentStatus

    class Config:
        from_attributes = True


class PaymentOut(BaseModel):
    amount_paid: int
    month: date
    status: str


class StudentWithPayments(BaseModel):
    id: int
    name: str

    payments: list[PaymentOut]

    class Config:
        from_attributes = True


class RoomAssignmentCreate(BaseModel):
    student_id: int
    room_id: int
    start_date: date


class StatusResponse(str, Enum):
    active = "active"
    maintenance = "maintenance"


class RoomCreate(BaseModel):

    room_no: str
    capacity: int
    price_per_std: int
    status: StatusResponse
