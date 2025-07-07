import pydantic
import typing


class EmployerManager(pydantic.BaseModel):
    """
    EmployerManager
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    Candidate's manager's email address.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Candidate's manager's name.
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    Candidate's manager's phone number.
    """
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    """
    Candidate's manager's title.
    """
