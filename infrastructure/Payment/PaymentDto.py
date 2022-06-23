@dataclass
class PaymentDto:
    id: int
    paymentStatus: int
    note: str
    bookingId: int
