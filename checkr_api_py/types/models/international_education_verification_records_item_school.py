import pydantic
import typing
import typing_extensions

from .international_address import InternationalAddress


class InternationalEducationVerificationRecordsItemSchool(pydantic.BaseModel):
    """
    InternationalEducationVerificationRecordsItemSchool
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[InternationalAddress] = pydantic.Field(
        alias="address", default=None
    )
    candidate_id: typing.Optional[str] = pydantic.Field(
        alias="candidate_id", default=None
    )
    """
    Candidate linked to this School resource.
    """
    current: typing.Optional[bool] = pydantic.Field(alias="current", default=None)
    """
    Defines whether the Candidate is currently enrolled.
    """
    degree: typing.Optional[str] = pydantic.Field(alias="degree", default=None)
    """
    Degree awarded to the Candidate.
    """
    end_date: typing.Optional[str] = pydantic.Field(alias="end_date", default=None)
    """
    Candidate’s end date with the School.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    major: typing.Optional[str] = pydantic.Field(alias="major", default=None)
    """
    Candidate’s major.
    """
    minor: typing.Optional[str] = pydantic.Field(alias="minor", default=None)
    """
    Candidate’s minor.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Name of the School.
    """
    object: typing.Optional[typing_extensions.Literal["school"]] = pydantic.Field(
        alias="object", default=None
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    School's phone number.
    """
    school_url: typing.Optional[str] = pydantic.Field(alias="school_url", default=None)
    """
    School’s website.
    """
    start_date: typing.Optional[str] = pydantic.Field(alias="start_date", default=None)
    """
    Candidate’s start date with the School.
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """
    year_awarded: typing.Optional[int] = pydantic.Field(
        alias="year_awarded", default=None
    )
    """
    Year in which the degree was awarded.
    """
