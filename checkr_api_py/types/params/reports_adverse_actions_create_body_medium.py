import pydantic
import typing
import typing_extensions

from .reports_adverse_actions_create_body_medium_email import (
    ReportsAdverseActionsCreateBodyMediumEmail,
    _SerializerReportsAdverseActionsCreateBodyMediumEmail,
)
from .reports_adverse_actions_create_body_medium_postal import (
    ReportsAdverseActionsCreateBodyMediumPostal,
    _SerializerReportsAdverseActionsCreateBodyMediumPostal,
)


class ReportsAdverseActionsCreateBodyMedium(typing_extensions.TypedDict):
    """
    The medium through which the Adverse Action notification should be sent.

    """

    email: typing_extensions.NotRequired[ReportsAdverseActionsCreateBodyMediumEmail]
    """
    The email medium is used to send an adverse action via email to the candidate.
    
    """

    postal: typing_extensions.NotRequired[ReportsAdverseActionsCreateBodyMediumPostal]
    """
    The postal medium is used to send an adverse action via physical mail to the candidate.
    
    """


class _SerializerReportsAdverseActionsCreateBodyMedium(pydantic.BaseModel):
    """
    Serializer for ReportsAdverseActionsCreateBodyMedium handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email: typing.Optional[_SerializerReportsAdverseActionsCreateBodyMediumEmail] = (
        pydantic.Field(alias="email", default=None)
    )
    postal: typing.Optional[_SerializerReportsAdverseActionsCreateBodyMediumPostal] = (
        pydantic.Field(alias="postal", default=None)
    )
