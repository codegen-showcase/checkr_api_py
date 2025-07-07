import pydantic
import typing
import typing_extensions


class Candidate(pydantic.BaseModel):
    """
    Candidate
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    adjudication: typing.Optional[
        typing_extensions.Literal[
            "engaged", "post_adverse_action", "pre_adverse_action"
        ]
    ] = pydantic.Field(alias="adjudication", default=None)
    """
    The adjudication for the Candidate’s most recently created Report.
    """
    copy_requested: typing.Optional[bool] = pydantic.Field(
        alias="copy_requested", default=None
    )
    """
    If `true`, the candidate has asked to receive a copy of their report.
    """
    custom_id: typing.Optional[str] = pydantic.Field(alias="custom_id", default=None)
    """
    Client-assigned unique ID for the Candidate. Can be used to map Checkr Candidate IDs to your internal tracking system, and to search for Candidates through both the Dashboard and the API.
    """
    dob: typing.Optional[str] = pydantic.Field(alias="dob", default=None)
    """
    Candidate’s date of birth.
    """
    driver_license_number: typing.Optional[str] = pydantic.Field(
        alias="driver_license_number", default=None
    )
    """
    Candidate’s driver license number.
    """
    driver_license_state: typing.Optional[str] = pydantic.Field(
        alias="driver_license_state", default=None
    )
    """
    Candidate’s driver license state of issue.
    Format: `ISO 3166-2:US`.
    
    """
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    Candidate’s email address.
    
    """
    first_name: typing.Optional[str] = pydantic.Field(alias="first_name", default=None)
    """
    Candidate’s first name.
    
    """
    geo_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="geo_ids", default=None
    )
    """
    Array of Geo IDs.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    last_name: typing.Optional[str] = pydantic.Field(alias="last_name", default=None)
    """
    Candidate’s last name.
    """
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Up to 50 customer-defined key-value pairs. Use this parameter to store additional information on your candidate. For example: Use the key to map candidates to `job_req_id`, `application_id`, or `branch_id`. Keys must be 40 characters or less. Values must be 500 characters or less.
    For example: { "job_req_id": "12345" }
    """
    middle_name: typing.Optional[str] = pydantic.Field(
        alias="middle_name", default=None
    )
    """
    Candidate’s middle name. This field is required if `no_middle_name` is `false`.
    
    """
    mother_maiden_name: typing.Optional[str] = pydantic.Field(
        alias="mother_maiden_name", default=None
    )
    """
    Candidate’s mother’s maiden name.
    
    """
    no_middle_name: typing.Optional[bool] = pydantic.Field(
        alias="no_middle_name", default=None
    )
    """
    Required if no `middle_name` is provided. `true` if the candidate has no middle name.
    
    """
    object: typing.Optional[typing_extensions.Literal["candidate"]] = pydantic.Field(
        alias="object", default=None
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    Candidate’s phone number.
    """
    postal_address: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="postal_address", default=None
    )
    """
    Candidate's postal address.
    """
    previous_driver_license_number: typing.Optional[str] = pydantic.Field(
        alias="previous_driver_license_number", default=None
    )
    """
    Candidate’s previous driver license number.
    """
    previous_driver_license_state: typing.Optional[str] = pydantic.Field(
        alias="previous_driver_license_state", default=None
    )
    """
    State that issued the candidate’s previous driver license.
    Format: `ISO 3166-2:US`.
    
    """
    report_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="report_ids", default=None
    )
    """
    Array of Report IDs.
    """
    ssn: typing.Optional[str] = pydantic.Field(alias="ssn", default=None)
    """
    Candidate’s Social Security Number. This value will be redacted in all return calls, except for the last four digits.
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """
    zipcode: typing.Optional[str] = pydantic.Field(alias="zipcode", default=None)
    """
    Candidate’s 5-digit zip code.
    """
