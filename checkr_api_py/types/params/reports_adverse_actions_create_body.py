import pydantic
import typing
import typing_extensions

from .reports_adverse_actions_create_body_medium import (
    ReportsAdverseActionsCreateBodyMedium,
    _SerializerReportsAdverseActionsCreateBodyMedium,
)


class ReportsAdverseActionsCreateBody(typing_extensions.TypedDict):
    """
    ReportsAdverseActionsCreateBody
    """

    adverse_item_ids: typing_extensions.Required[typing.List[str]]
    """
    IDs of Adverse Items selected for the Adverse Action.
    """

    medium: typing_extensions.NotRequired[ReportsAdverseActionsCreateBodyMedium]
    """
    The medium through which the Adverse Action notification should be sent.
    
    """

    post_notice_scheduled_at: typing_extensions.NotRequired[str]
    """
    Time at which the Post-Adverse Action notification will be sent. Default is 7 days after creation.
    """


class _SerializerReportsAdverseActionsCreateBody(pydantic.BaseModel):
    """
    Serializer for ReportsAdverseActionsCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    adverse_item_ids: typing.List[str] = pydantic.Field(
        alias="adverse_item_ids",
    )
    medium: typing.Optional[_SerializerReportsAdverseActionsCreateBodyMedium] = (
        pydantic.Field(alias="medium", default=None)
    )
    post_notice_scheduled_at: typing.Optional[str] = pydantic.Field(
        alias="post_notice_scheduled_at", default=None
    )
