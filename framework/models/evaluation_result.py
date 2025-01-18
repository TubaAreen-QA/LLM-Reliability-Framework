# provider
# model
# overall_score
# confidence_score
# hallucination_score
# quality_score
# results

from dataclasses import dataclass 
from framework.models.validation_result import validation_Result
from framework.models.provider_response import provider_Response

@dataclass(slots=True)
class Evalutation_result:
    provider_response=provider_Response
    validation_result:list[validation_Result]
    overall_score:float



