# ProviderRequest
# Identification
# ---------------------
# provider
# model
# request_id
# Generation
# ---------------------
# prompt
# system_prompt
# temperature
# max_tokens
# top_p
# stop_sequences
# response_format
# Execution
# ---------------------
# timeout
# retry_count
# stream
# Framework
# ---------------------
# metadata
# tags



from dataclasses import dataclass, field
from typing import Any

@dataclass(slots=True)
class provider_request:
    prompt: str
    provider: str
    model: str 
    temprature: float = 0.0
    max_tokens: int = 512
    timeout: int = 30
    metadata:dict[str,Any] = field(default_factory=dict)