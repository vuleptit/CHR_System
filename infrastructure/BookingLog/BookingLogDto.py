@dataclass
class BookingLogDto:
    id: int
    houseId: int
    tenantId: int
    price: float
    checkoutTime: str
    bookingNote: str
    bookingStatus: int
    createdDate: str
    bookingId: int
