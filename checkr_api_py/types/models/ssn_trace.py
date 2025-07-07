import pydantic
import typing


class SsnTrace(pydantic.BaseModel):
    """
    SsnTrace
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cancellation_reason: typing.Optional[str] = pydantic.Field(
        alias="cancellation_reason", default=None
    )
    """
    See [cancellation reasons](#section/Reference/Cancellation-Reasons) section for possible values.
    """
    cancellation_reason_description: typing.Optional[str] = pydantic.Field(
        alias="cancellation_reason_description", default=None
    )
    """
    See [cancellation reasons](#section/Reference/Cancellation-Reasons) section for possible values.
    """
    completed_at: typing.Optional[str] = pydantic.Field(
        alias="completed_at", default=None
    )
    """
    Time at which the screening was completed.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the screening was created.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    object: typing.Optional[typing.Any] = pydantic.Field(alias="object", default=None)
    result: typing.Optional[str] = pydantic.Field(alias="result", default=None)
    """
    Outcome of the screening.  Screenings completed before April 2021 may return `"clear"` or `"consider"`.
    """
    status: typing.Optional[typing.Any] = pydantic.Field(alias="status", default=None)
    turnaround_time: typing.Optional[typing.Any] = pydantic.Field(
        alias="turnaround_time", default=None
    )
    uri: typing.Optional[typing.Any] = pydantic.Field(alias="uri", default=None)
    addresses: typing.Optional[typing.Any] = pydantic.Field(
        alias="addresses", default=None
    )
    """
    This field has been deprecated and will return an empty array.
    """
    aliases: typing.Optional[typing.Any] = pydantic.Field(alias="aliases", default=None)
    """
    This field has been deprecated and will return an empty array.
    """
    data_mismatch: typing.Optional[bool] = pydantic.Field(
        alias="data_mismatch", default=None
    )
    """
    If true, information returned from the SSN Trace does not match any of the candidate’s provided information.
    """
    death_index: typing.Optional[bool] = pydantic.Field(
        alias="death_index", default=None
    )
    """
    If true, the input SSN is listed on the Social Security Administration's “Death Master File”.
    """
    dob_mismatch: typing.Optional[bool] = pydantic.Field(
        alias="dob_mismatch", default=None
    )
    """
    If true, the name on the SSN Trace matches the candidate's provided information, but the DOB does not.
    """
    invalid_issuance_year: typing.Optional[bool] = pydantic.Field(
        alias="invalid_issuance_year", default=None
    )
    """
    If true, the input SSN has a year of issuance that precedes the candidate's reported year of birth.
    """
    issued_state: typing.Optional[str] = pydantic.Field(
        alias="issued_state", default=None
    )
    """
    The US state where the ID was issued.
    """
    issued_year: typing.Optional[int] = pydantic.Field(
        alias="issued_year", default=None
    )
    """
    The year the ID was issued.
    """
    name_mismatch: typing.Optional[bool] = pydantic.Field(
        alias="name_mismatch", default=None
    )
    """
    If true, the DOB associated with the addresses returned from the SSN Trace matches the candidate's input DOB, but the name does not.
    """
    no_data: typing.Optional[bool] = pydantic.Field(alias="no_data", default=None)
    """
    No data was returned for the input Candidate PII.
    """
    ssn: typing.Optional[str] = pydantic.Field(alias="ssn", default=None)
    """
    Candidate’s social security number. This value will be redacted in all return calls, except for the last four digits.
    """
    ssn_already_taken: typing.Optional[bool] = pydantic.Field(
        alias="ssn_already_taken", default=None
    )
    """
    If true, another Candidate with same SSN already exists in our system.
    """
    thin_file: typing.Optional[bool] = pydantic.Field(alias="thin_file", default=None)
    """
    No information found.
    """
