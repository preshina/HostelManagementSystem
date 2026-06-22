# service/exceptions.py

class StudentNotFoundException(Exception):
    pass


class StudentOrRoomNotFoundException(Exception):
    pass


class PaymentAlreadyExistsException(Exception):
    pass


class StudentAlreadyExistsException(Exception):
    pass


class RoomFullException(Exception):
    pass


class RoomNotAssignedException(Exception):
    pass


class InvalidPaymentAmountException(Exception):
    pass


class StudentAlreadyAssignedException(Exception):
    pass
