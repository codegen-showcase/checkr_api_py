import pydantic
import typing

from .user_roles_item import UserRolesItem


class User(pydantic.BaseModel):
    """
    User
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the User was created.
    """
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    User's email address.
    """
    full_name: typing.Optional[str] = pydantic.Field(alias="full_name", default=None)
    """
    User's full name.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    roles: typing.Optional[typing.List[UserRolesItem]] = pydantic.Field(
        alias="roles", default=None
    )
