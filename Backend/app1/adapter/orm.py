from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Date, UniqueConstraint
from datetime import date


class Base(DeclarativeBase):
    pass


# -------------------------
# STUDENT
# -------------------------
class StudentInfo(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=False)

    payments: Mapped[list["Payments"]] = relationship(
        back_populates="student",
        cascade="all, delete"
    )

    assignments: Mapped[list["RoomAssignment"]] = relationship(
        back_populates="student",
        cascade="all, delete"
    )


# -------------------------
# ROOM
# -------------------------
class Room(Base):
    __tablename__ = "room"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    room_no: Mapped[str] = mapped_column(
        String(10), nullable=False, unique=True)
    capacity: Mapped[int] = mapped_column(Integer, nullable=False)
    price_per_std: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(String(30), default="active")

    assignments: Mapped[list["RoomAssignment"]] = relationship(
        back_populates="room",
        cascade="all, delete"
    )

    payments: Mapped[list["Payments"]] = relationship(
        back_populates="room"
    )


# -------------------------
# ROOM ASSIGNMENT (CORE TABLE)
# -------------------------
class RoomAssignment(Base):
    __tablename__ = "room_assignment"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    student_id: Mapped[int] = mapped_column(
        ForeignKey("student.id"), nullable=False)
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"), nullable=True)

    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date | None] = mapped_column(Date, nullable=True)

    student: Mapped["StudentInfo"] = relationship(back_populates="assignments")
    room: Mapped["Room"] = relationship(back_populates="assignments")


# -------------------------
# PAYMENTS
# -------------------------
class Payments(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    student_id: Mapped[int] = mapped_column(
        ForeignKey("student.id"), nullable=False)
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"), nullable=True)

    month: Mapped[date] = mapped_column(Date, nullable=False)
    amount_paid: Mapped[int] = mapped_column(Integer, default=0)
    due_amount: Mapped[int] = mapped_column(Integer, nullable=False)
    balance: Mapped[int] = mapped_column(Integer, nullable=False)
    payment_date: Mapped[date] = mapped_column(Date, nullable=False)

    status: Mapped[str] = mapped_column(String(30), default="unpaid")

    student: Mapped["StudentInfo"] = relationship(back_populates="payments")
    room: Mapped["Room"] = relationship(back_populates="payments")
