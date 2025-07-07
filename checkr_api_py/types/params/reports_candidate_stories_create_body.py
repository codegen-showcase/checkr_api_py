import pydantic
import typing
import typing_extensions

from .reports_candidate_stories_create_body_documents_item import (
    ReportsCandidateStoriesCreateBodyDocumentsItem,
    _SerializerReportsCandidateStoriesCreateBodyDocumentsItem,
)


class ReportsCandidateStoriesCreateBody(typing_extensions.TypedDict):
    """
    ReportsCandidateStoriesCreateBody
    """

    content: typing_extensions.Required[str]
    """
    Additional information provided by Candidate.
    """

    documents: typing_extensions.Required[
        typing.List[ReportsCandidateStoriesCreateBodyDocumentsItem]
    ]
    """
    An array of documents to attach to the Candidate Story. Can be empty.
    """

    record_id: typing_extensions.NotRequired[str]
    """
    ID of the Record existing on a Screening to which the Candidate Story is linked.
    When no record ID is provided, the Candidate Story is considered General Information.
    
    """


class _SerializerReportsCandidateStoriesCreateBody(pydantic.BaseModel):
    """
    Serializer for ReportsCandidateStoriesCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    content: str = pydantic.Field(
        alias="content",
    )
    documents: typing.List[
        _SerializerReportsCandidateStoriesCreateBodyDocumentsItem
    ] = pydantic.Field(
        alias="documents",
    )
    record_id: typing.Optional[str] = pydantic.Field(alias="record_id", default=None)
