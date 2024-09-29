# Class: Guest
class Guest:
    def __init__(self, guest_id: int, name: str, contact_info: str, payment_info: str):
        self._guest_id = guest_id
        self._name = name
        self._contact_info = contact_info
        self._payment_info = payment_info

    # Getter and setter methods
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_contact_info(self):
        return self._contact_info

    def set_contact_info(self, contact_info):
        self._contact_info = contact_info

    def get_payment_info(self):
        return self._payment_info

    def set_payment_info(self, payment_info):
        self._payment_info = payment_info

    # Function headers with pass statements
    def check_in(self):
        pass  # This function checks the guest into the hotel.

    def check_out(self):
        pass  # This function checks the guest out of the hotel.


# Class: Room
class Room:
    def __init__(self, room_id: int, room_type: str, status: str, price: float):
        self._room_id = room_id
        self._room_type = room_type
        self._status = status
        self._price = price

    # Getter and setter methods
    def get_room_type(self):
        return self._room_type

    def set_room_type(self, room_type):
        self._room_type = room_type

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    # Function headers with pass statements
    def update_status(self):
        pass  # This function updates the status of the room.


# Class: Reservation
class Reservation:
    def __init__(self, reservation_id: int, guest: Guest, room: Room, check_in: str, check_out: str, status: str):
        self._reservation_id = reservation_id
        self._guest = guest
        self._room = room
        self._check_in = check_in
        self._check_out = check_out
        self._status = status

    # Getter and setter methods
    def get_reservation_id(self):
        return self._reservation_id

    def set_reservation_id(self, reservation_id):
        self._reservation_id = reservation_id

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    # Function headers with pass statements
    def create_reservation(self):
        pass  # This function creates a new reservation.

    def modify_reservation(self):
        pass  # This function modifies an existing reservation.

    def cancel_reservation(self):
        pass  # This function cancels the reservation.

    def view_reservation(self):
        pass  # This function displays reservation details.


# Class: Invoice
class Invoice:
    def __init__(self, invoice_id: int, reservation: Reservation, amount: float):
        self._invoice_id = invoice_id
        self._reservation = reservation
        self._amount = amount

    # Getter and setter methods
    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    # Function headers with pass statements
    def generate_invoice(self):
        pass  # This function generates the invoice for a reservation.


# Class: Payment
class Payment:
    def __init__(self, payment_id: int, guest: Guest, invoice: Invoice, amount: float):
        self._payment_id = payment_id
        self._guest = guest
        self._invoice = invoice
        self._amount = amount

    # Getter and setter methods
    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    # Function headers with pass statements
    def process_payment(self):
        pass  # This function processes the payment.


# Class: Receptionist
class Receptionist:
    def __init__(self, receptionist_id: int, name: str):
        self._receptionist_id = receptionist_id
        self._name = name

    # Function headers with pass statements
    def check_in_guest(self):
        pass  # This function handles the guest check-in process.

    def check_out_guest(self):
        pass  # This function handles the guest check-out process.


# Creating objects and populating them with data from Figure 1

# Guest information
guest = Guest(guest_id=1, name="Ted Vera", contact_info="tedvera@mac.com", payment_info="Mastercard ending in 9904")

# Room information
room = Room(room_id=101, room_type="2 Queen Beds /No Smoking/Desk/Safe/Coffee Maker In Room/Hair Dryer",
            status="available", price=89.95)

# Reservation information
reservation = Reservation(
    reservation_id=52523687,
    guest=guest,
    room=room,
    check_in="Sun, Aug 22, 2010 - 03:00 PM",
    check_out="Tue, Aug 24, 2010 - 12:00 PM",
    status="confirmed"
)

# Invoice information
invoice = Invoice(
    invoice_id=1,
    reservation=reservation,
    amount=201.48  # Total charges including taxes and fees
)

# Payment information
payment = Payment(
    payment_id=1,
    guest=guest,
    invoice=invoice,
    amount=201.48
)


# Display the reservation confirmation
def display_reservation_details():
    print(f"Reservation Confirmed for {guest.get_name()}")
    print(f"Email: {guest.get_contact_info()} | Reservation ID: {reservation.get_reservation_id()}")
    print(f"Check-in: {reservation._check_in} | Check-out: {reservation._check_out}")
    print(f"Hotel: Comfort Inn & Suites, Los Alamos, 2455 Trinty Drive, Los Alamos, NM 87544 | Phone: 505-661-1110\n")

    print(
        f"Room: {room.get_room_type()} | Price per night: ${room.get_price():.2f} | Total: ${room.get_price() * 2:.2f}")
    print(f"Payment Method: {guest.get_payment_info()} | Total Amount (including taxes): ${invoice.get_amount():.2f}")

    print(f"Taxes and Fees: $21.58 | Total Nights: 2 | Rooms Booked: 1")


# Call the function to display reservation details
display_reservation_details()