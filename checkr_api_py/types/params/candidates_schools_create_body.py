import pydantic
import typing
import typing_extensions

from .address import Address, _SerializerAddress


class CandidatesSchoolsCreateBody(typing_extensions.TypedDict):
    """
    CandidatesSchoolsCreateBody
    """

    address: typing_extensions.Required[Address]

    candidate_id: typing_extensions.NotRequired[str]
    """
    Candidate linked to this School resource.
    """

    current: typing_extensions.NotRequired[bool]
    """
    Defines whether the Candidate is currently enrolled.
    """

    degree: typing_extensions.Required[str]
    """
    Degree awarded to the Candidate.
    """

    end_date: typing_extensions.NotRequired[str]
    """
    Candidate’s end date with the School.
    """

    id: typing_extensions.NotRequired[str]
    """
    ID of the resource.
    """

    major: typing_extensions.Required[str]
    """
    Candidate’s major.
    """

    minor: typing_extensions.NotRequired[str]
    """
    Candidate’s minor.
    """

    name: typing_extensions.Required[str]
    """
    Name of the School.
    """

    object: typing_extensions.NotRequired[typing_extensions.Literal["school"]]

    phone: typing_extensions.NotRequired[typing.Optional[str]]
    """
    School's phone number.
    """

    school_url: typing_extensions.NotRequired[str]
    """
    School’s website.
    """

    start_date: typing_extensions.NotRequired[str]
    """
    Candidate’s start date with the School.
    """

    year_awarded: typing_extensions.NotRequired[int]
    """
    Year in which the degree was awarded.
    """


class _SerializerCandidatesSchoolsCreateBody(pydantic.BaseModel):
    """
    Serializer for CandidatesSchoolsCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerAddress = pydantic.Field(
        alias="address",
    )
    candidate_id: typing.Optional[str] = pydantic.Field(
        alias="candidate_id", default=None
    )
    current: typing.Optional[bool] = pydantic.Field(alias="current", default=None)
    degree: str = pydantic.Field(
        alias="degree",
    )
    end_date: typing.Optional[str] = pydantic.Field(alias="end_date", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    major: str = pydantic.Field(
        alias="major",
    )
    minor: typing.Optional[str] = pydantic.Field(alias="minor", default=None)
    name: str = pydantic.Field(
        alias="name",
    )
    object: typing.Optional[typing_extensions.Literal["school"]] = pydantic.Field(
        alias="object", default=None
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    school_url: typing.Optional[str] = pydantic.Field(alias="school_url", default=None)
    start_date: typing.Optional[str] = pydantic.Field(alias="start_date", default=None)
    year_awarded: typing.Optional[int] = pydantic.Field(
        alias="year_awarded", default=None
    )
