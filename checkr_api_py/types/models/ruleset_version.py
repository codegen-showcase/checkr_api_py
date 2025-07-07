import pydantic
import typing


class RulesetVersion(pydantic.BaseModel):
    """
    Information about a RulesetVersion. RulesetVersions are complete, distinct
    versions of Rulesets. New RulesetVersions are generated each time a Ruleset
    is published. The most recent 'live' RulesetVersion is used (by default) when
    assessing new Reports.

    RulesetVersions also include metadata about the creator and publisher of the
    version, and timestamps for these events.

    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    number: typing.Optional[int] = pydantic.Field(alias="number", default=None)
    """
    The version number
    """
