import pydantic
import typing

from .ruleset_version import RulesetVersion


class Ruleset(pydantic.BaseModel):
    """
    Information about a Ruleset.

    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    The name of the Ruleset
    """
    version: typing.Optional[RulesetVersion] = pydantic.Field(
        alias="version", default=None
    )
    """
    Information about a RulesetVersion. RulesetVersions are complete, distinct 
    versions of Rulesets. New RulesetVersions are generated each time a Ruleset 
    is published. The most recent 'live' RulesetVersion is used (by default) when 
    assessing new Reports.
    
    RulesetVersions also include metadata about the creator and publisher of the 
    version, and timestamps for these events.
    
    """
