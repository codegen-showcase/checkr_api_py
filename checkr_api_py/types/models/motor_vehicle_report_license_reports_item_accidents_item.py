import pydantic
import typing
import typing_extensions


class MotorVehicleReportLicenseReportsItemAccidentsItem(pydantic.BaseModel):
    """
    MotorVehicleReportLicenseReportsItemAccidentsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    accident_date: typing.Optional[str] = pydantic.Field(
        alias="accident_date", default=None
    )
    acd_code: typing.Optional[str] = pydantic.Field(alias="acd_code", default=None)
    action_taken: typing.Optional[str] = pydantic.Field(
        alias="action_taken", default=None
    )
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    county: typing.Optional[str] = pydantic.Field(alias="county", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    enforcing_agency: typing.Optional[str] = pydantic.Field(
        alias="enforcing_agency", default=None
    )
    fatality_accident: typing.Optional[bool] = pydantic.Field(
        alias="fatality_accident", default=None
    )
    fatality_count: typing.Optional[int] = pydantic.Field(
        alias="fatality_count", default=None
    )
    fine_amount: typing.Optional[float] = pydantic.Field(
        alias="fine_amount", default=None
    )
    group: typing.Optional[
        typing_extensions.Literal[
            "fatality", "personal injury", "property damage", "unspecified"
        ]
    ] = pydantic.Field(alias="group", default=None)
    """
    Displays category type for an accident.
    """
    injury_accident: typing.Optional[bool] = pydantic.Field(
        alias="injury_accident", default=None
    )
    injury_count: typing.Optional[int] = pydantic.Field(
        alias="injury_count", default=None
    )
    jurisdiction: typing.Optional[str] = pydantic.Field(
        alias="jurisdiction", default=None
    )
    license_plate: typing.Optional[str] = pydantic.Field(
        alias="license_plate", default=None
    )
    note: typing.Optional[str] = pydantic.Field(alias="note", default=None)
    """
    A note that is added if an accident appears on a candidate’s MVR.
    """
    order_number: typing.Optional[str] = pydantic.Field(
        alias="order_number", default=None
    )
    points: typing.Optional[typing.Any] = pydantic.Field(alias="points", default=None)
    policy_number: typing.Optional[str] = pydantic.Field(
        alias="policy_number", default=None
    )
    reinstatement_date: typing.Optional[str] = pydantic.Field(
        alias="reinstatement_date", default=None
    )
    report_number: typing.Optional[str] = pydantic.Field(
        alias="report_number", default=None
    )
    severity: typing.Optional[str] = pydantic.Field(alias="severity", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    State.
    Format: `ISO 3166-2:US`
    
    """
    state_code: typing.Optional[str] = pydantic.Field(alias="state_code", default=None)
    ticket_number: typing.Optional[str] = pydantic.Field(
        alias="ticket_number", default=None
    )
    vehicle_speed: typing.Optional[float] = pydantic.Field(
        alias="vehicle_speed", default=None
    )
    vehicles_involved_count: typing.Optional[int] = pydantic.Field(
        alias="vehicles_involved_count", default=None
    )
    violation_number: typing.Optional[str] = pydantic.Field(
        alias="violation_number", default=None
    )
