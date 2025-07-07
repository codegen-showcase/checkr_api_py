import pydantic
import typing
import typing_extensions


class ReportDrugScreeningEventsItem(pydantic.BaseModel):
    """
    ReportDrugScreeningEventsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time the event was created
    """
    text: typing.Optional[str] = pydantic.Field(alias="text", default=None)
    """
    Additional note for event type
    """
    type_: typing.Optional[
        typing_extensions.Literal[
            "completed",
            "screening_invitation_sent",
            "screening_notice",
            "screening_pass_extended",
            "screening_scheduled",
            "status_update",
        ]
    ] = pydantic.Field(alias="type", default=None)
    """
    Type of event
    """
