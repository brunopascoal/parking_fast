from dj_rql.filter_cls import AutoRQLFilterClass
from parking.models import ParkingRecord, ParkingSpot

class ParkingRecordFilterClass(AutoRQLFilterClass):
  MODEL = ParkingRecord

class ParkingSpotFilterClass(AutoRQLFilterClass):
  MODEL = ParkingSpot
