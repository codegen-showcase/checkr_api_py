import pydantic
import typing

from .motor_vehicle_report_custom_rules_rule_key1 import (
    MotorVehicleReportCustomRulesRuleKey1,
)
from .motor_vehicle_report_custom_rules_rule_key2 import (
    MotorVehicleReportCustomRulesRuleKey2,
)


class MotorVehicleReportCustomRules(pydantic.BaseModel):
    """
    Object with custom rules applied to generate this MVR.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    rule_key_1: typing.Optional[MotorVehicleReportCustomRulesRuleKey1] = pydantic.Field(
        alias="rule_key_1", default=None
    )
    rule_key_2: typing.Optional[MotorVehicleReportCustomRulesRuleKey2] = pydantic.Field(
        alias="rule_key_2", default=None
    )
