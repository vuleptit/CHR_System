@dataclass
class NotificationDto:
    id: int
    userId: int
    houseId: str
    bookingId: int
    paymentId: int
    type: int
    content: str
