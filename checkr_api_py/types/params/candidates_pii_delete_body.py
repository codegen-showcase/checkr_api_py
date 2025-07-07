import pydantic
import typing
import typing_extensions


class CandidatesPiiDeleteBody(typing_extensions.TypedDict):
    """
    CandidatesPiiDeleteBody
    """

    deletion_contact_email_address: typing_extensions.Required[str]
    """
    Email address of person requesting candidate's PII removal.
    """

    deletion_contact_first_name: typing_extensions.NotRequired[str]
    """
    First name of person requesting candidate's PII removal.
    """

    deletion_contact_last_name: typing_extensions.NotRequired[str]
    """
    Last name of person requesting candidate's PII removal.
    """


class _SerializerCandidatesPiiDeleteBody(pydantic.BaseModel):
    """
    Serializer for CandidatesPiiDeleteBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    deletion_contact_email_address: str = pydantic.Field(
        alias="deletion_contact_email_address",
    )
    deletion_contact_first_name: typing.Optional[str] = pydantic.Field(
        alias="deletion_contact_first_name", default=None
    )
    deletion_contact_last_name: typing.Optional[str] = pydantic.Field(
        alias="deletion_contact_last_name", default=None
    )
