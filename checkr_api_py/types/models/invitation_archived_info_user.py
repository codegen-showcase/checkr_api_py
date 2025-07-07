import pydantic
import typing


class InvitationArchivedInfoUser(pydantic.BaseModel):
    """
    User information about the archiver
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    User's email address
    
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    User's ID
    
    """
