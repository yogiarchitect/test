from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from src.models.domain.enums.internal_status_type import InternalStatusType
from src.models.enums.odometerscale_type import OdometerScaleType
from src.models.enums.programcode_type import ProgramCode


class VehicleData(BaseModel):
    msisdn: Optional[str] = Field(
        description="msisdn is associated with call that is received by call center. It stands for Mobile Station International Subscriber Directory Number and is required for callback incase call gets disconnected"
    )
    programcode: Optional[ProgramCode] = Field(description="Accepted Program Codes")
    event_datetime: Optional[int] = Field(description="Save timestamp in int*1000")
    timestamp: Optional[datetime] = Field(description="calldate and time")

    calldate: Optional[str] = Field(description="Date on which call is placed")
    calltime: Optional[str] = Field(description="Time at which call is placed")
    odometer: Optional[int] = Field(description="Km or miles per odometer scale")
    odometerscale: Optional[OdometerScaleType] = Field(
        description="0 = OdometerScaleMiles, 1=OdometerScaleKilometers"
    )

    latitude: Optional[float] = Field(
        description="Two digits followed by decimal value. Ex: 12.1234"
    )
    longitude: Optional[float] = Field(
        description="Two digits followed by decimal value. Ex: 12.1234"
    )
    headingdirection: Optional[str] = Field(
        description="one of these values EAST, WEST, NORTH, SOUTH, NORTH EAST, SOUTH EAST, SOUTH WEST, NORTH WEST"
    )

    vin: Optional[str] = Field(description="Vehicle Identification Number")

    brand: Optional[str] = Field(description="Brand of the vehicle")
    modelname: Optional[str] = Field(
        description="Vehicle model name. Ex: Jetta, Passat..etc"
    )
    modelyear: Optional[str] = Field(
        description="Vehicle model year: 2018, 2019,2020..etc"
    )
    modelcode: Optional[str] = Field(description="VW model code. Ex:BX52N6")
    modeldesc: Optional[str] = Field(
        description="Description of the car model. Ex: Golf_Volkswagen_2008"
    )

    countrycode: Optional[str] = Field(description="US/CA")
    activationtype: Optional[str] = Field(description="Type of activation")
    market: Optional[str] = Field(description="Param inside ocuSim Ex:nar-us")
    mileage: Optional[int] = Field(description="Mileage in number Ex:3197")
    mileageunit: Optional[OdometerScaleType] = Field(
        description="Mileageunit mi=MILES, km=KILOMETERS"
    )

    customerfirstname: Optional[str] = Field(description="Customer First Name")
    customerlastname: Optional[str] = Field(description="Customer Last Name")
    modelcolor: Optional[str] = Field(description="ExteriorColor of the Vehicle")
    srnumber: Optional[str] = Field(description="SRNumber Ex: 1-13220115000")
    ismoving: Optional[bool] = Field(description="Is_moving")
    cruisingrange: Optional[str] = Field(description="Cruising_range Ex: 385.25 Miles")
    locationtrueness: Optional[str] = Field(description="Location_trueness Ex: weak")
    locationconfidence: Optional[str] = Field(description="Location_confidence Ex: 2")
    locationaddress: Optional[str] = Field(description="FromLocationAddress")
    locationcity: Optional[str] = Field(description="FromLocationCity Ex: Redmond")
    locationstate: Optional[str] = Field(description="FromLocationState Ex: WA")
    locationpostalcode: Optional[str] = Field(
        description="FromLocationZip Ex: 98052-0000"
    )
    phonenumber: Optional[str] = Field(description="FromLocationPhoneNo Ex: 4258811000")
    altitude: Optional[str] = Field(description="Altitude")
    language: Optional[str] = Field(description="Hmi_language Ex: English")

    status: InternalStatusType = Field(
        InternalStatusType.UNKNOWN,
        description="Current status as returned from external service",
    )
    responsemessage: Optional[str] = Field(description="Response message")
