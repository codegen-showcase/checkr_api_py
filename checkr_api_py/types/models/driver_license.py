import pydantic
import typing
import typing_extensions

from .driver_license_issued_dates_item import DriverLicenseIssuedDatesItem


class DriverLicense(pydantic.BaseModel):
    """
    DriverLicense
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    candidate_id: typing.Optional[str] = pydantic.Field(
        alias="candidate_id", default=None
    )
    """
    ID of the candidate.
    """
    current: typing.Optional[bool] = pydantic.Field(alias="current", default=None)
    """
    Defines whether the driver license is the candidate's current license.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    issued_dates: typing.Optional[typing.List[DriverLicenseIssuedDatesItem]] = (
        pydantic.Field(alias="issued_dates", default=None)
    )
    """
    An array of issued date objects
    """
    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
    """
    The driver license number.
    """
    object: typing.Optional[typing_extensions.Literal["candidate_driver_license"]] = (
        pydantic.Field(alias="object", default=None)
    )
    source: typing.Optional[str] = pydantic.Field(alias="source", default=None)
    """
    Where/how Checkr learned about the license.
    """
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    The state that issued the driver license.
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """
