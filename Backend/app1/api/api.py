from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from Backend.app1.service.service import HostelService, StudentNotFoundException, RoomFullException, StudentAlreadyAssignedException, StudentOrRoomNotFoundException, RoomNotAssignedException, StudentAlreadyExistsException
from Backend.app1.database import get_db
from datetime import date
from Backend.app1.schema.hostel import StudentCreate, PaymentCreate, PaymentList, RoomCreate, RoomAssignmentCreate
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(StudentNotFoundException)
async def student_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": "Student not found"}
    )


@app.exception_handler(StudentOrRoomNotFoundException)
async def student_or_room_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": "Student or room  not found"}
    )


@app.exception_handler(RoomNotAssignedException)
async def room_not_assigned_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": "room not assigned"})


@app.exception_handler(RoomFullException)
async def room_full_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": "Room is already full!"}
    )


@app.exception_handler(StudentAlreadyAssignedException)
async def student_already_assigned_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": "Student is already assigned with room!"}
    )


@app.exception_handler(StudentAlreadyExistsException)
async def student_already_exists_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": "Student already Exists!"}
    )


def get_service(db: Session = Depends(get_db)):
    return HostelService(db)


# ---------------- STUDENT ----------------
@app.post("/students", response_model=StudentCreate)
def create_student(student: StudentCreate, service: HostelService = Depends(get_service)):
    return service.create_student(student)


@app.post("/rooms", response_model=RoomCreate)
def create_room(data: RoomCreate, service: HostelService = Depends(get_service)):
    return service.create_room(data)

# ---------------- ROOM ASSIGNMENT ----------------


@app.post("/students/{student_id}/{room_id}/{start_date}/assign-room", response_model=RoomAssignmentCreate)
def assign_room(
    student_id: int,
    room_id: int,
    start_date: date,
    service: HostelService = Depends(get_service)
):
    return service.assign_room(student_id, room_id, start_date)


# ---------------- PAYMENTS ----------------
@app.post("/students/{student_id}/payments")
def create_payments(student_id: int, data: PaymentList, service: HostelService = Depends(get_service)):
    return service.create_payments(student_id, data.payments)


# ---------------- GET STUDENT ----------------
@app.get("/students/{student_id}")
def get_student(student_id: int, service: HostelService = Depends(get_service)):
    return service.get_student_with_payments(student_id)


@app.get("/students")
def get_students(service: HostelService = Depends(get_service)):
    return service.get_all_student()


@app.get("/student/{student_id}")
def get_active_room(student_id: int, service: HostelService = Depends(get_service)):
    return service.get_active_room(student_id)


@app.get("/students/rooms")
def get_room(service: HostelService = Depends(get_service)):
    return service.get_all_room()


@app.get("/rooms/{room_id}")
def room_capacity(room_id, service: HostelService = Depends(get_service)):
    return service.get_room_capacity(room_id)
