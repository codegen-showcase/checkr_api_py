import pydantic
import typing
import typing_extensions


class Verification(pydantic.BaseModel):
    """
    Verification
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    completed_at: typing.Optional[str] = pydantic.Field(
        alias="completed_at", default=None
    )
    """
    Value will be null if the candidate has not uploaded the required documents, otherwise will contain the date and time that the documents were provided.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    object: typing.Optional[typing_extensions.Literal["verification"]] = pydantic.Field(
        alias="object", default=None
    )
    processed_at: typing.Optional[str] = pydantic.Field(
        alias="processed_at", default=None
    )
    """
    Value will be null if the candidate has not uploaded the required documents, otherwise will contain the date and time that the documents were processed.
    """
    report_id: typing.Optional[str] = pydantic.Field(alias="report_id", default=None)
    """
    Value include the report_id
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """
    verification_type: typing.Optional[str] = pydantic.Field(
        alias="verification_type", default=None
    )
    """
    The list of possible verification types can be found [here](#section/Reference/Verification-Types).
    """
    verification_url: typing.Optional[str] = pydantic.Field(
        alias="verification_url", default=None
    )
    """
    URL to direct the candidate to upload documents.
    """
