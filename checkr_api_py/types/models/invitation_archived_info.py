import pydantic
import typing

from .invitation_archived_info_user import InvitationArchivedInfoUser


class InvitationArchivedInfo(pydantic.BaseModel):
    """
    Information relating to an archived report or invitation
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    time: typing.Optional[str] = pydantic.Field(alias="time", default=None)
    """
    Time the report or invitation was archived
    """
    user: typing.Optional[InvitationArchivedInfoUser] = pydantic.Field(
        alias="user", default=None
    )
    """
    User information about the archiver
    """
