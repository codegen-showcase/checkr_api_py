import pydantic
import typing
import typing_extensions


class ReportsCandidateStoriesCreateBodyDocumentsItem(typing_extensions.TypedDict):
    """
    ReportsCandidateStoriesCreateBodyDocumentsItem
    """

    filename: typing_extensions.NotRequired[str]
    """
    File name
    """

    tempfile: typing_extensions.NotRequired[str]
    """
    Accessible resource from which the document will be copied.
    """

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "application/pdf",
            "image/bmp",
            "image/gif",
            "image/heic",
            "image/jpeg",
            "image/jpg",
            "image/png",
            "image/tiff",
        ]
    ]
    """
    Document MIME type
    """


class _SerializerReportsCandidateStoriesCreateBodyDocumentsItem(pydantic.BaseModel):
    """
    Serializer for ReportsCandidateStoriesCreateBodyDocumentsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    filename: typing.Optional[str] = pydantic.Field(alias="filename", default=None)
    tempfile: typing.Optional[str] = pydantic.Field(alias="tempfile", default=None)
    type_: typing.Optional[
        typing_extensions.Literal[
            "application/pdf",
            "image/bmp",
            "image/gif",
            "image/heic",
            "image/jpeg",
            "image/jpg",
            "image/png",
            "image/tiff",
        ]
    ] = pydantic.Field(alias="type", default=None)
