import pydantic
import typing
import typing_extensions


class I9FormsI9CreateBody(typing_extensions.TypedDict):
    """
    I9FormsI9CreateBody
    """

    authorized_representative_email: typing_extensions.NotRequired[str]
    """
    Email address of authorized representative.
    """

    authorized_representative_first_name: typing_extensions.NotRequired[str]
    """
    First name of authorized representative.
    """

    authorized_representative_last_name: typing_extensions.NotRequired[str]
    """
    Last name of authorized representative.
    """

    candidate_id: typing_extensions.Required[str]
    """
    Candidate resource Id.
    
    """

    email: typing_extensions.Required[str]
    """
    Candidate email address.
    """

    start_date: typing_extensions.Required[str]
    """
    Candidate start date.
    """

    workflow_type: typing_extensions.Required[
        typing_extensions.Literal[
            "employee_appointment", "employer_appointment", "remote_section_1_only"
        ]
    ]
    """
    Workflow type.
    
    For additional insights into workflow types, please consider reviewing the [Form I-9 definitions](#section/Reference/Form-I-9-definitions-lessBETAgreater).
    
    """

    worksite_id: typing_extensions.Required[str]
    """
    Worksite resource Id.
    """


class _SerializerI9FormsI9CreateBody(pydantic.BaseModel):
    """
    Serializer for I9FormsI9CreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    authorized_representative_email: typing.Optional[str] = pydantic.Field(
        alias="authorized_representative_email", default=None
    )
    authorized_representative_first_name: typing.Optional[str] = pydantic.Field(
        alias="authorized_representative_first_name", default=None
    )
    authorized_representative_last_name: typing.Optional[str] = pydantic.Field(
        alias="authorized_representative_last_name", default=None
    )
    candidate_id: str = pydantic.Field(
        alias="candidate_id",
    )
    email: str = pydantic.Field(
        alias="email",
    )
    start_date: str = pydantic.Field(
        alias="start_date",
    )
    workflow_type: typing_extensions.Literal[
        "employee_appointment", "employer_appointment", "remote_section_1_only"
    ] = pydantic.Field(
        alias="workflow_type",
    )
    worksite_id: str = pydantic.Field(
        alias="worksite_id",
    )
