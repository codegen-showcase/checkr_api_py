import pydantic
import typing


class MotorVehicleReportCustomRulesRuleKey2(pydantic.BaseModel):
    """
    MotorVehicleReportCustomRulesRuleKey2
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    satisfied: typing.Optional[bool] = pydantic.Field(alias="satisfied", default=None)
