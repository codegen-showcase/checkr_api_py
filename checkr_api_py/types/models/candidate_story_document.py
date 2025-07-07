import pydantic
import typing
import typing_extensions


class CandidateStoryDocument(pydantic.BaseModel):
    """
    CandidateStoryDocument
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    content_type: typing.Optional[str] = pydantic.Field(
        alias="content_type", default=None
    )
    """
    File’s content type.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the Document was created.
    """
    download_uri: typing.Optional[str] = pydantic.Field(
        alias="download_uri", default=None
    )
    """
    JSON encoded URL of the document. This URL is valid for 15 minutes.
    """
    filename: typing.Optional[str] = pydantic.Field(alias="filename", default=None)
    """
    File’s name.
    """
    filesize: typing.Optional[int] = pydantic.Field(alias="filesize", default=None)
    """
    File’s size in bytes.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    object: typing.Optional[typing_extensions.Literal["document"]] = pydantic.Field(
        alias="object", default=None
    )
    type_: typing.Optional[typing_extensions.Literal["candidate_story_document"]] = (
        pydantic.Field(alias="type", default=None)
    )
    """
    The type of Document.
    """
