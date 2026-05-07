from dataclasses import dataclass


@dataclass
class Aeroporto:

    ID: int
    IATA_CODE: str
    AIRPORT: str
    CITY: str
    STATE: str
    COUNTRY: str
    LATITUDE: int
    LONGITUDE: int
    TIMEZONE_OFFSET: int

    def __eq__(self, other):
        return self.ID == other.ID

    def __hash__(self):
        return hash(self.ID)

    def __str__(self):
        pass