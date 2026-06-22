from Backend.app1.adapter.orm import StudentInfo, Payments, Room, RoomAssignment
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError


class HostelRepository:
    def __init__(self, session):
        self.session = session

    # ---------------- STUDENT ----------------
    def create_student(self, data):
        existing = self.session.query(StudentInfo).filter(
            StudentInfo.phone == data.phone
        ).first()

        if existing:
            return {"status": "exists"}
        try:
            student = StudentInfo(name=data.name, phone=data.phone)
            self.session.add(student)
            self.session.commit()
            self.session.refresh(student)
            return student

        except SQLAlchemyError:
            self.session.rollback()
            return None

    def get_student(self, student_id):
        return self.session.get(StudentInfo, student_id)

    def get_all_student(self):
        return self.session.query(StudentInfo).all()

    def create_room(self, data):
        existing = self.session.query(Room).filter(
            Room.room_no == data.room_no
        ).first()

        if existing:
            return {"status": "exists"}

        room = Room(
            room_no=data.room_no,
            capacity=data.capacity,
            price_per_std=data.price_per_std,
            status=data.status
        )

        self.session.add(room)
        self.session.commit()
        self.session.refresh(room)

        return {"status": "success", "data": room}

    # ---------------- ROOM ----------------
    def get_all_room(self):
        return self.session.query(Room).all()

    def get_room(self, room_id):
        return self.session.get(Room, room_id)

    def get_room_occupancy(self, room_id):
        return self.session.query(RoomAssignment).filter(
            RoomAssignment.room_id == room_id,
            RoomAssignment.end_date.is_(None)
        ).count()

    # ---------------- ROOM ASSIGNMENT ----------------
    def assign_room(self, student_id, room_id, start_date):
        student = self.get_student(student_id)
        room = self.get_room(room_id)

        if not student or not room:
            return {"status": "not_found"}

        active = self.session.query(RoomAssignment).filter(
            RoomAssignment.student_id == student_id,
            RoomAssignment.end_date.is_(None)
        ).first()

        if active:
            return {"status": "already_assigned"}

        occupied = self.get_room_occupancy(room_id)
        if occupied >= room.capacity:
            return {"status": "room_full"}

        assignment = RoomAssignment(
            student_id=student_id,
            room_id=room_id,
            start_date=start_date
        )

        self.session.add(assignment)
        self.session.commit()
        self.session.refresh(assignment)

        return {"status": "success", "data": assignment}

    # ---------------- PAYMENTS ----------------
    def create_payments(self, student_id, payments):
        student = self.get_student(student_id)
        if not student:
            return None

        # get active assignment
        assignment = self.session.query(RoomAssignment).filter(
            RoomAssignment.student_id == student_id,
            RoomAssignment.end_date.is_(None)
        ).first()

        if not assignment:
            return "no_room_assigned"

        room = self.get_room(assignment.room_id)

        objs = []

        for p in payments:
            due = room.price_per_std - p.amount_paid
            balance = max(due, 0)

            status = (
                "paid" if due <= 0 else
                "partial" if p.amount_paid > 0 else
                "unpaid"
            )

            obj = Payments(
                student_id=student_id,
                room_id=room.id,
                month=p.month,
                amount_paid=p.amount_paid,
                due_amount=due,
                balance=balance,
                payment_date=p.payment_date,
                status=status
            )

            objs.append(obj)

        self.session.add_all(objs)
        self.session.commit()
        return objs

    def get_payments(self, student_id):
        return self.session.query(Payments).filter(
            Payments.student_id == student_id
        ).all()

    def get_active_room(self, student_id):
        return self.session.query(RoomAssignment).filter(
            RoomAssignment.student_id == student_id,
            RoomAssignment.end_date.is_(None)
        ).first()

    def room_capacity(self, room_id):
        current = self.session.query(Room).filter(
            Room.id == room_id).count()
        return current
