import pydantic
import typing
import typing_extensions

from .address import Address, _SerializerAddress
from .candidates_employers_create_body_manager import (
    CandidatesEmployersCreateBodyManager,
    _SerializerCandidatesEmployersCreateBodyManager,
)


class CandidatesEmployersCreateBody(typing_extensions.TypedDict):
    """
    CandidatesEmployersCreateBody
    """

    address: typing_extensions.Required[Address]

    candidate_id: typing_extensions.NotRequired[str]
    """
    ID of the Candidate being screened.
    """

    contract_type: typing_extensions.Required[
        typing_extensions.Literal["contract", "full_time", "internship", "part_time"]
    ]
    """
    Candidate’s contract type.
    """

    do_not_contact: typing_extensions.NotRequired[bool]
    """
    If `true`, the employer will not be contacted about the Candidate.
    """

    employer_url: typing_extensions.NotRequired[str]
    """
    Employer’s website.
    """

    end_date: typing_extensions.NotRequired[str]
    """
    Candidate’s end date with the employer.
    """

    id: typing_extensions.NotRequired[str]
    """
    ID of the resource.
    """

    manager: typing_extensions.NotRequired[CandidatesEmployersCreateBodyManager]

    name: typing_extensions.Required[str]
    """
    Candidate’s employer’s name.
    """

    note: typing_extensions.NotRequired[str]
    """
    A text note used to add context for an employment gap.
    """

    object: typing_extensions.NotRequired[typing_extensions.Literal["employer"]]

    position: typing_extensions.Required[str]
    """
    Candidate’s position or title.
    """

    salary: typing_extensions.NotRequired[int]
    """
    Candidate’s gross salary in dollars annually.
    """

    start_date: typing_extensions.Required[str]
    """
    Candidate’s start date with the employer.
    """

    type_: typing_extensions.NotRequired[typing_extensions.Literal["employer", "gap"]]
    """
    Type of employment history to be created.
    
    If type is set to `gap` only `start_date` is required, and only `start_date`, `end_date`, and `note` will be recorded.
    
    """


class _SerializerCandidatesEmployersCreateBody(pydantic.BaseModel):
    """
    Serializer for CandidatesEmployersCreateBody handling case conversions
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
    contract_type: typing_extensions.Literal[
        "contract", "full_time", "internship", "part_time"
    ] = pydantic.Field(
        alias="contract_type",
    )
    do_not_contact: typing.Optional[bool] = pydantic.Field(
        alias="do_not_contact", default=None
    )
    employer_url: typing.Optional[str] = pydantic.Field(
        alias="employer_url", default=None
    )
    end_date: typing.Optional[str] = pydantic.Field(alias="end_date", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    manager: typing.Optional[_SerializerCandidatesEmployersCreateBodyManager] = (
        pydantic.Field(alias="manager", default=None)
    )
    name: str = pydantic.Field(
        alias="name",
    )
    note: typing.Optional[str] = pydantic.Field(alias="note", default=None)
    object: typing.Optional[typing_extensions.Literal["employer"]] = pydantic.Field(
        alias="object", default=None
    )
    position: str = pydantic.Field(
        alias="position",
    )
    salary: typing.Optional[int] = pydantic.Field(alias="salary", default=None)
    start_date: str = pydantic.Field(
        alias="start_date",
    )
    type_: typing.Optional[typing_extensions.Literal["employer", "gap"]] = (
        pydantic.Field(alias="type", default=None)
    )
