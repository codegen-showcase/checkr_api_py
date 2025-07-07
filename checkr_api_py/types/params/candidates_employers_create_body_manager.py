import pydantic
import typing
import typing_extensions


class CandidatesEmployersCreateBodyManager(typing_extensions.TypedDict):
    """
    CandidatesEmployersCreateBodyManager
    """

    email: typing_extensions.NotRequired[str]
    """
    Candidate's manager's email address.
    """

    name: typing_extensions.NotRequired[str]
    """
    Candidate's manager's name.
    """

    phone: typing_extensions.NotRequired[str]
    """
    Candidate's manager's phone number.
    """

    title: typing_extensions.NotRequired[str]
    """
    Candidate's manager's title.
    """


class _SerializerCandidatesEmployersCreateBodyManager(pydantic.BaseModel):
    """
    Serializer for CandidatesEmployersCreateBodyManager handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
