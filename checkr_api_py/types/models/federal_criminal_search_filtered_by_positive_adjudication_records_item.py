import pydantic
import typing

from .address import Address
from .charge import Charge


class FederalCriminalSearchFilteredByPositiveAdjudicationRecordsItem(
    pydantic.BaseModel
):
    """
    FederalCriminalSearchFilteredByPositiveAdjudicationRecordsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[Address] = pydantic.Field(alias="address", default=None)
    arresting_agency: typing.Optional[str] = pydantic.Field(
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
    filtered_by_positive_adjudication_charges: typing.Optional[typing.List[Charge]] = (
        pydantic.Field(alias="filtered_by_positive_adjudication_charges", default=None)
    )
    """
    Array of CriminalCharge objects filtered out by your account’s Positive Adjudication Matrix.
    """
