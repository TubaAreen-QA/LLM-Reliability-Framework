# provider
# model
# prompt
# answer
# response_timestamp
# response_time_ms
# token_usage
# raw_response


from dataclasses import dataclass ,  field
from typing import Any

@dataclass
class provider_Response:
    provider: str
    model:str
    prompt:str
    answer:str
    response_timestamp:int
    response_time_ms:int
    token_usage:dict[str,int]
    raw_response:dict[str,int]=field(default_Factory= dict)
