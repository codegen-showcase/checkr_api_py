import pydantic
import typing
import typing_extensions

from .international_address import InternationalAddress
from .international_employment_verification_records_item_employer_manager import (
    InternationalEmploymentVerificationRecordsItemEmployerManager,
)


class InternationalEmploymentVerificationRecordsItemEmployer(pydantic.BaseModel):
    """
    InternationalEmploymentVerificationRecordsItemEmployer
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
    ID of the Candidate being screened.
    """
    contract_type: typing.Optional[
        typing_extensions.Literal["contract", "full_time", "internship", "part_time"]
    ] = pydantic.Field(alias="contract_type", default=None)
    """
    Candidate’s contract type.
    """
    do_not_contact: typing.Optional[bool] = pydantic.Field(
        alias="do_not_contact", default=None
    )
    """
    If `true`, the employer will not be contacted about the Candidate.
    """
    employer_url: typing.Optional[str] = pydantic.Field(
        alias="employer_url", default=None
    )
    """
    Employer’s website.
    """
    end_date: typing.Optional[str] = pydantic.Field(alias="end_date", default=None)
    """
    Candidate’s end date with the employer.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    manager: typing.Optional[
        InternationalEmploymentVerificationRecordsItemEmployerManager
    ] = pydantic.Field(alias="manager", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Candidate’s employer’s name.
    """
    object: typing.Optional[typing_extensions.Literal["employer"]] = pydantic.Field(
        alias="object", default=None
    )
    position: typing.Optional[str] = pydantic.Field(alias="position", default=None)
    """
    Candidate’s position or title.
    """
    salary: typing.Optional[int] = pydantic.Field(alias="salary", default=None)
    """
    Candidate’s gross salary in dollars annually.
    """
    start_date: typing.Optional[str] = pydantic.Field(alias="start_date", default=None)
    """
    Candidate’s start date with the employer.
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """
