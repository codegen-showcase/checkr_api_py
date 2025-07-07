import pydantic
import typing


class MotorVehicleReportSuspensionsItem(pydantic.BaseModel):
    """
    MotorVehicleReportSuspensionsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    end_date: typing.Optional[str] = pydantic.Field(alias="end_date", default=None)
    start_date: typing.Optional[str] = pydantic.Field(alias="start_date", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
