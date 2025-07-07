import pydantic
import typing
import typing_extensions

from .invitation_archived_info import InvitationArchivedInfo


class Invitation(pydantic.BaseModel):
    """
    Invitation
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    archived: typing.Optional[bool] = pydantic.Field(alias="archived", default=None)
    """
    Returns `true` if the invitation is archived.
    """
    archived_info: typing.Optional[InvitationArchivedInfo] = pydantic.Field(
        alias="archived_info", default=None
    )
    """
    Information relating to an archived report or invitation
    """
    candidate_id: typing.Optional[str] = pydantic.Field(
        alias="candidate_id", default=None
    )
    """
    ID of the Candidate to whom the Invitation was sent.
    """
    completed_at: typing.Optional[str] = pydantic.Field(
        alias="completed_at", default=None
    )
    """
    Time at which the Invitation was completed by the candidate.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the Invitation was created.
    """
    deleted_at: typing.Optional[str] = pydantic.Field(alias="deleted_at", default=None)
    """
    Time at which the Invitation was deleted.
    """
    expires_at: typing.Optional[str] = pydantic.Field(alias="expires_at", default=None)
    """
    Time at which the Invitation will expire.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    invitation_url: typing.Optional[str] = pydantic.Field(
        alias="invitation_url", default=None
    )
    """
    URL for the Invitation.
    """
    object: typing.Optional[typing_extensions.Literal["invitation"]] = pydantic.Field(
        alias="object", default=None
    )
    package: typing.Optional[str] = pydantic.Field(alias="package", default=None)
    """
    Package associated with the Invitation.
    """
    report_id: typing.Optional[str] = pydantic.Field(alias="report_id", default=None)
    """
    ID of the Report created by the completion of this Invitation. Will be null if the Invitation has not yet been completed.
    """
    status: typing.Optional[
        typing_extensions.Literal["completed", "expired", "pending"]
    ] = pydantic.Field(alias="status", default=None)
    """
    Status of the Invitation.
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """
