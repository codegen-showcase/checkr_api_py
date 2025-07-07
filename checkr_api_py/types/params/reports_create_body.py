import pydantic
import typing
import typing_extensions

from .self_disclosure import SelfDisclosure, _SerializerSelfDisclosure
from .work_location import WorkLocation, _SerializerWorkLocation


class ReportsCreateBody(typing_extensions.TypedDict):
    """
    ReportsCreateBody
    """

    candidate_id: typing_extensions.Required[str]
    """
    ID of the Candidate screened.
    """

    node: typing_extensions.NotRequired[str]
    """
    <font color="red">Required</font> for hierarchy-enabled accounts.
    
    `custom_id` of the associated node.
    
    """

    package: typing_extensions.Required[str]
    """
    `slug` of the associated package.
    Example: `driver_pro`
    
    """

    self_disclosures: typing_extensions.NotRequired[typing.List[SelfDisclosure]]
    """
    Array of SelfDisclosures
    
    **Note:** Self Disclosures may not be added, updated, or deleted after a Report has been created. The information provided in a Self Disclosure will not be included in the completed Report, and may be retrieved using [GET](#operation/getReport) `/v1/reports/{id}?include=documents`. See the [Documents](#tag/Documents) resource for more information.
    
    Removing the requirement for the description, date, and location parameters greatly reduces the value of Self Disclosures. If your system mandates that these parameters be optional, work with your Checkr Customer Success Manager to disable the requirement.
    
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


class _SerializerReportsCreateBody(pydantic.BaseModel):
    """
    Serializer for ReportsCreateBody handling case conversions
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
    self_disclosures: typing.Optional[typing.List[_SerializerSelfDisclosure]] = (
        pydantic.Field(alias="self_disclosures", default=None)
    )
    tags: typing.Optional[typing.List[str]] = pydantic.Field(alias="tags", default=None)
    work_locations: typing.Optional[typing.List[_SerializerWorkLocation]] = (
        pydantic.Field(alias="work_locations", default=None)
    )
