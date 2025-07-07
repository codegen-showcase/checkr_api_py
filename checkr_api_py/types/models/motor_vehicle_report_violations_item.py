import pydantic
import typing


class MotorVehicleReportViolationsItem(pydantic.BaseModel):
    """
    MotorVehicleReportViolationsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acd_code: typing.Optional[str] = pydantic.Field(alias="acd_code", default=None)
    category: typing.Optional[str] = pydantic.Field(alias="category", default=None)
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    conviction_date: typing.Optional[str] = pydantic.Field(
        alias="conviction_date", default=None
    )
    county: typing.Optional[str] = pydantic.Field(alias="county", default=None)
    court_name: typing.Optional[str] = pydantic.Field(alias="court_name", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    disposition: typing.Optional[str] = pydantic.Field(
        alias="disposition", default=None
    )
    docket: typing.Optional[str] = pydantic.Field(alias="docket", default=None)
    issued_date: typing.Optional[str] = pydantic.Field(
        alias="issued_date", default=None
    )
    points: typing.Optional[int] = pydantic.Field(alias="points", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    state_code: typing.Optional[str] = pydantic.Field(alias="state_code", default=None)
    ticket_number: typing.Optional[str] = pydantic.Field(
        alias="ticket_number", default=None
    )
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
