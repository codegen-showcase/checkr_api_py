import pydantic
import typing


class DriverLicenseIssuedDatesItem(pydantic.BaseModel):
    """
    DriverLicenseIssuedDatesItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    source: typing.Optional[str] = pydantic.Field(alias="source", default=None)
    """
    Indicates where this issued date information came from. Issued dates added through the API will have a source of "client".
    """
    value: typing.Optional[str] = pydantic.Field(alias="value", default=None)
    """
    The issued date.
    """
