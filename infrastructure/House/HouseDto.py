@dataclass
class HouseDto:
    id: int
    ownerId: int
    country: str
    city: str
    district: str
    addressDetail: str
    note: str
    houseStatus: int
    houseTypeId: int
