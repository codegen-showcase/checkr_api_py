import pydantic
import typing

from .address import Address
from .charge import Charge


class FederalCriminalSearchRecordsItem(pydantic.BaseModel):
    """
    FederalCriminalSearchRecordsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[Address] = pydantic.Field(alias="address", default=None)
    arresting_agency: typing.Optional[typing.Any] = pydantic.Field(
        alias="arresting_agency", default=None
    )
    case_number: typing.Optional[str] = pydantic.Field(
        alias="case_number", default=None
    )
    county: typing.Optional[str] = pydantic.Field(alias="county", default=None)
    court_jurisdiction: typing.Optional[str] = pydantic.Field(
        alias="court_jurisdiction", default=None
    )
    court_of_record: typing.Optional[str] = pydantic.Field(
        alias="court_of_record", default=None
    )
    dob: typing.Optional[str] = pydantic.Field(alias="dob", default=None)
    file_date: typing.Optional[str] = pydantic.Field(alias="file_date", default=None)
    full_name: typing.Optional[str] = pydantic.Field(alias="full_name", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    yob: typing.Optional[int] = pydantic.Field(alias="yob", default=None)
    charges: typing.Optional[typing.List[Charge]] = pydantic.Field(
        alias="charges", default=None
    )
