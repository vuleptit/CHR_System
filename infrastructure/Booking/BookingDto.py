@dataclass
class BookingDto:
    id: int
    houseId: int
    price: float
    checkinTime: str
    checkoutTime: str
    bookingNote: str
    bookingStatus: int
    createdDate: str
