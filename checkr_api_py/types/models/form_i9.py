import pydantic
import typing
import typing_extensions


class FormI9(pydantic.BaseModel):
    """
    FormI9
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    authorized_representative_email: typing.Optional[str] = pydantic.Field(
        alias="authorized_representative_email", default=None
    )
    """
    Email address of authorized representative.
    """
    authorized_representative_first_name: typing.Optional[str] = pydantic.Field(
        alias="authorized_representative_first_name", default=None
    )
    """
    First name of authorized representative.
    """
    authorized_representative_last_name: typing.Optional[str] = pydantic.Field(
        alias="authorized_representative_last_name", default=None
    )
    """
    Last name of authorized representative.
    """
    candidate_id: typing.Optional[str] = pydantic.Field(
        alias="candidate_id", default=None
    )
    """
    ID of the candidate
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Form I-9 date of creation.
    """
    form_i9_url: typing.Optional[str] = pydantic.Field(
        alias="form_i9_url", default=None
    )
    """
    Form I-9 link to Tracker UI.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource
    """
    object: typing.Optional[typing_extensions.Literal["form_i9"]] = pydantic.Field(
        alias="object", default=None
    )
    open_tasks: typing.Optional[
        typing_extensions.Literal[
            "accept_reject_i9",
            "appoint_section_2_representative",
            "check_user_email",
            "complete_section_2",
            "no_action",
        ]
    ] = pydantic.Field(alias="open_tasks", default=None)
    """
    Form I-9 open task.
    
    More details on [Form I-9 definitions](#section/Reference/Form-I-9-definitions-lessBETAgreater).
    
    """
    open_tasks_url: typing.Optional[str] = pydantic.Field(
        alias="open_tasks_url", default=None
    )
    """
    Form I-9 open task link.
    """
    order_progress: typing.Optional[
        typing_extensions.Literal[
            "awaiting_approval",
            "everify_pending",
            "everify_tnc_issued",
            "i9_complete",
            "section_1_incomplete",
            "section_2_incomplete",
        ]
    ] = pydantic.Field(alias="order_progress", default=None)
    """
    Form I-9 order progress.
    
    More details on [Form I-9 definitions](#section/Reference/Form-I-9-definitions-lessBETAgreater).
    
    """
    start_date: typing.Optional[str] = pydantic.Field(alias="start_date", default=None)
    """
    Candidate start date.
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource
    """
    workflow_type: typing.Optional[
        typing_extensions.Literal[
            "employee_appointment", "employer_appointment", "remote_section_1_only"
        ]
    ] = pydantic.Field(alias="workflow_type", default=None)
    """
    Type of workflow.
    
    More details on [Form I-9 definitions](#section/Reference/Form-I-9-definitions-lessBETAgreater).
    
    """
    worksite_id: typing.Optional[str] = pydantic.Field(
        alias="worksite_id", default=None
    )
    """
    Worksite resource Id.
    """
    worksite_uri: typing.Optional[str] = pydantic.Field(
        alias="worksite_uri", default=None
    )
    """
    URI of the worksite
    """
