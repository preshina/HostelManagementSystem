from Backend.app1.adapter.repository import HostelRepository
from Backend.app1.service.exceptions import StudentNotFoundException, RoomFullException, StudentAlreadyAssignedException, StudentOrRoomNotFoundException, RoomNotAssignedException, StudentAlreadyExistsException
from Backend.app1.schema.hostel import StudentWithPayments, PaymentOut


class HostelService:
    def __init__(self, db):
        self.repo = HostelRepository(db)

    # ---------------- STUDENT ----------------
    def create_student(self, data):
        result = self.repo.create_student(data)

        if result["status"] == "exists":
            raise StudentAlreadyExistsException()

    def get_all_student(self):
        return self.repo.get_all_student()

    def create_room(self, data):
        result = self.repo.create_room(data)

        if result["status"] == "exists":
            raise RoomFullException()

        return result["data"]

    def get_all_room(self):
        return self.repo.get_room()
    # ---------------- ROOM ASSIGNMENT ----------------

    def assign_room(self, student_id, room_id, start_date):
        result = self.repo.assign_room(student_id, room_id, start_date)

        if result["status"] == "not_found":
            raise StudentOrRoomNotFoundException()

        if result["status"] == "already_assigned":
            raise StudentAlreadyAssignedException()

        if result["status"] == "room_full":
            raise RoomFullException()

        return result["data"]

    # ---------------- PAYMENTS ----------------
    def create_payments(self, student_id, payments):
        result = self.repo.create_payments(student_id, payments)

        if result is None:
            raise StudentNotFoundException()

        if result == "no_room_assigned":
            raise RoomNotAssignedException()

        return {
            "message": "Payments created successfully",
            "payments": [
                {
                    "id": p.id,
                    "student_id": p.student_id,
                    "month": p.month,
                    "amount_paid": p.amount_paid,
                    "due_amount": p.due_amount,
                    "balance": p.balance,
                    "payment_date": p.payment_date,
                    "status": p.status,
                }
                for p in result
            ]
        }

    # ---------------- GET STUDENT ----------------
    def get_student_with_payments(self, student_id):
        student = self.repo.get_student(student_id)

        if not student:
            raise StudentNotFoundException()

        payments = self.repo.get_payments(student_id)
        assignment = self.repo.get_active_room(student_id)

        room_no = None
        if assignment:
            room = self.repo.get_room(assignment.room_id)
            room_no = room.room_no

        return {
            "id": student.id,
            "name": student.name,
            "phone": student.phone,
            "room": room_no,
            "payments": [
                {
                    "amount_paid": p.amount_paid,
                    "month": p.month,
                    "status": p.status
                }
                for p in payments
            ]
        }

    def get_active_room(self, std_id):
        return self.repo.get_active_room(std_id)

    def get_room_capacity(self, room_id):
        return self.repo.room_capacity(room_id)
