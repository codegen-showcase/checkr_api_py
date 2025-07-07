import pydantic
import typing
import typing_extensions


class Candidate(typing_extensions.TypedDict):
    """
    Candidate
    """

    adjudication: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "engaged", "post_adverse_action", "pre_adverse_action"
        ]
    ]
    """
    The adjudication for the Candidate’s most recently created Report.
    """

    copy_requested: typing_extensions.NotRequired[bool]
    """
    If `true`, the candidate has asked to receive a copy of their report.
    """

    custom_id: typing_extensions.NotRequired[str]
    """
    Client-assigned unique ID for the Candidate. Can be used to map Checkr Candidate IDs to your internal tracking system, and to search for Candidates through both the Dashboard and the API.
    """

    dob: typing_extensions.NotRequired[str]
    """
    Candidate’s date of birth.
    """

    driver_license_number: typing_extensions.NotRequired[str]
    """
    Candidate’s driver license number.
    """

    driver_license_state: typing_extensions.NotRequired[str]
    """
    Candidate’s driver license state of issue.
    Format: `ISO 3166-2:US`.
    
    """

    email: typing_extensions.NotRequired[str]
    """
    Candidate’s email address.
    
    """

    first_name: typing_extensions.NotRequired[str]
    """
    Candidate’s first name.
    
    """

    geo_ids: typing_extensions.NotRequired[typing.List[str]]
    """
    Array of Geo IDs.
    """

    id: typing_extensions.NotRequired[str]
    """
    ID of the resource.
    """

    last_name: typing_extensions.NotRequired[str]
    """
    Candidate’s last name.
    """

    metadata: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    Up to 50 customer-defined key-value pairs. Use this parameter to store additional information on your candidate. For example: Use the key to map candidates to `job_req_id`, `application_id`, or `branch_id`. Keys must be 40 characters or less. Values must be 500 characters or less.
    For example: { "job_req_id": "12345" }
    """

    middle_name: typing_extensions.NotRequired[str]
    """
    Candidate’s middle name. This field is required if `no_middle_name` is `false`.
    
    """

    mother_maiden_name: typing_extensions.NotRequired[str]
    """
    Candidate’s mother’s maiden name.
    
    """

    no_middle_name: typing_extensions.NotRequired[bool]
    """
    Required if no `middle_name` is provided. `true` if the candidate has no middle name.
    
    """

    object: typing_extensions.NotRequired[typing_extensions.Literal["candidate"]]

    phone: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Candidate’s phone number.
    """

    postal_address: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    Candidate's postal address.
    """

    previous_driver_license_number: typing_extensions.NotRequired[str]
    """
    Candidate’s previous driver license number.
    """

    previous_driver_license_state: typing_extensions.NotRequired[str]
    """
    State that issued the candidate’s previous driver license.
    Format: `ISO 3166-2:US`.
    
    """

    report_ids: typing_extensions.NotRequired[typing.List[str]]
    """
    Array of Report IDs.
    """

    ssn: typing_extensions.NotRequired[str]
    """
    Candidate’s Social Security Number. This value will be redacted in all return calls, except for the last four digits.
    """

    uri: typing_extensions.NotRequired[str]
    """
    URI of the resource.
    """

    zipcode: typing_extensions.NotRequired[str]
    """
    Candidate’s 5-digit zip code.
    """


class _SerializerCandidate(pydantic.BaseModel):
    """
    Serializer for Candidate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    adjudication: typing.Optional[
        typing_extensions.Literal[
            "engaged", "post_adverse_action", "pre_adverse_action"
        ]
    ] = pydantic.Field(alias="adjudication", default=None)
    copy_requested: typing.Optional[bool] = pydantic.Field(
        alias="copy_requested", default=None
    )
    custom_id: typing.Optional[str] = pydantic.Field(alias="custom_id", default=None)
    dob: typing.Optional[str] = pydantic.Field(alias="dob", default=None)
    driver_license_number: typing.Optional[str] = pydantic.Field(
        alias="driver_license_number", default=None
    )
    driver_license_state: typing.Optional[str] = pydantic.Field(
        alias="driver_license_state", default=None
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    first_name: typing.Optional[str] = pydantic.Field(alias="first_name", default=None)
    geo_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="geo_ids", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    last_name: typing.Optional[str] = pydantic.Field(alias="last_name", default=None)
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="metadata", default=None
    )
    middle_name: typing.Optional[str] = pydantic.Field(
        alias="middle_name", default=None
    )
    mother_maiden_name: typing.Optional[str] = pydantic.Field(
        alias="mother_maiden_name", default=None
    )
    no_middle_name: typing.Optional[bool] = pydantic.Field(
        alias="no_middle_name", default=None
    )
    object: typing.Optional[typing_extensions.Literal["candidate"]] = pydantic.Field(
        alias="object", default=None
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    postal_address: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="postal_address", default=None
    )
    previous_driver_license_number: typing.Optional[str] = pydantic.Field(
        alias="previous_driver_license_number", default=None
    )
    previous_driver_license_state: typing.Optional[str] = pydantic.Field(
        alias="previous_driver_license_state", default=None
    )
    report_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="report_ids", default=None
    )
    ssn: typing.Optional[str] = pydantic.Field(alias="ssn", default=None)
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    zipcode: typing.Optional[str] = pydantic.Field(alias="zipcode", default=None)
