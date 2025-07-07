import pydantic
import typing
import typing_extensions


class StateCriminalSearchRecordsItemChargesItem(pydantic.BaseModel):
    """
    StateCriminalSearchRecordsItemChargesItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    arrest_date: typing.Optional[typing.Any] = pydantic.Field(
        alias="arrest_date", default=None
    )
    assessment: typing.Optional[str] = pydantic.Field(alias="assessment", default=None)
    category: typing.Optional[
        typing_extensions.Literal[
            "criminal_intent",
            "drugs_and_alcohol",
            "fraud_and_deception",
            "homicide",
            "security",
            "sexual",
            "statutory",
            "theft_and_property",
            "unclassified",
            "vehicles_and_traffic",
            "violence",
        ]
    ] = pydantic.Field(alias="category", default=None)
    """
    The Checkr Assess category assigned to this criminal charge. This field will be included only if Checkr Assess is enabled for your account.
    
    """
    charge: typing.Optional[typing.Any] = pydantic.Field(alias="charge", default=None)
    charge_date: typing.Optional[str] = pydantic.Field(
        alias="charge_date", default=None
    )
    charge_id: typing.Optional[str] = pydantic.Field(alias="charge_id", default=None)
    charge_type: typing.Optional[str] = pydantic.Field(
        alias="charge_type", default=None
    )
    classification: typing.Optional[str] = pydantic.Field(
        alias="classification", default=None
    )
    conviction_date: typing.Optional[str] = pydantic.Field(
        alias="conviction_date", default=None
    )
    court: typing.Optional[str] = pydantic.Field(alias="court", default=None)
    defendant: typing.Optional[typing.Any] = pydantic.Field(
        alias="defendant", default=None
    )
    deposition: typing.Optional[str] = pydantic.Field(alias="deposition", default=None)
    deposition_date: typing.Optional[str] = pydantic.Field(
        alias="deposition_date", default=None
    )
    disposition: typing.Optional[str] = pydantic.Field(
        alias="disposition", default=None
    )
    disposition_date: typing.Optional[str] = pydantic.Field(
        alias="disposition_date", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    jail_time: typing.Optional[str] = pydantic.Field(alias="jail_time", default=None)
    """
    Sentenced to jail time.
    """
    next_court_date: typing.Optional[str] = pydantic.Field(
        alias="next_court_date", default=None
    )
    offense_date: typing.Optional[str] = pydantic.Field(
        alias="offense_date", default=None
    )
    plaintiff: typing.Optional[str] = pydantic.Field(alias="plaintiff", default=None)
    plea: typing.Optional[str] = pydantic.Field(alias="plea", default=None)
    prison_time: typing.Optional[str] = pydantic.Field(
        alias="prison_time", default=None
    )
    """
    Sentenced to prison time.
    """
    probation_status: typing.Optional[str] = pydantic.Field(
        alias="probation_status", default=None
    )
    probation_time: typing.Optional[str] = pydantic.Field(
        alias="probation_time", default=None
    )
    """
    Sentenced to probation time.
    """
    release_date: typing.Optional[str] = pydantic.Field(
        alias="release_date", default=None
    )
    restitution: typing.Optional[str] = pydantic.Field(
        alias="restitution", default=None
    )
    """
    Sentenced to restitution.
    """
    sentence: typing.Optional[str] = pydantic.Field(alias="sentence", default=None)
    sentence_date: typing.Optional[typing.Any] = pydantic.Field(
        alias="sentence_date", default=None
    )
