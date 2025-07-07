import pydantic
import typing


class ReportAddresses(pydantic.BaseModel):
    """
    ReportAddresses
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    end_date: typing.Optional[str] = pydantic.Field(alias="end_date", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Name of location.
    """
    start_date: typing.Optional[str] = pydantic.Field(alias="start_date", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
