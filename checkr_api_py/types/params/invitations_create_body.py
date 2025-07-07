import pydantic
import typing
import typing_extensions

from .work_location import WorkLocation, _SerializerWorkLocation


class InvitationsCreateBody(typing_extensions.TypedDict):
    """
    InvitationsCreateBody
    """

    candidate_id: typing_extensions.Required[str]
    """
    ID of the Candidate for whom the Invitation is created.
    """

    node: typing_extensions.NotRequired[str]
    """
    <font color="red">Required</font> for hierarchy-enabled accounts.
    
    `custom_id` of the associated node.
    
    """

    package: typing_extensions.Required[str]
    """
    `slug` of the associated package.
    
    """

    tags: typing_extensions.NotRequired[typing.List[str]]
    """
    Array of tags for the Report.
    """

    work_locations: typing_extensions.NotRequired[typing.List[WorkLocation]]
    """
    <font color="red">Required</font> for hierarchy-enabled accounts.
    
    Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.
    
    """


class _SerializerInvitationsCreateBody(pydantic.BaseModel):
    """
    Serializer for InvitationsCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    candidate_id: str = pydantic.Field(
        alias="candidate_id",
    )
    node: typing.Optional[str] = pydantic.Field(alias="node", default=None)
    package: str = pydantic.Field(
        alias="package",
    )
    tags: typing.Optional[typing.List[str]] = pydantic.Field(alias="tags", default=None)
    work_locations: typing.Optional[typing.List[_SerializerWorkLocation]] = (
        pydantic.Field(alias="work_locations", default=None)
    )
