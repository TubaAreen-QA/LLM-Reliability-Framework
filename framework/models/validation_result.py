# validator
# status
# actual
# expected
# message
# score

from dataclasses import dataclass
@dataclass(slots=True)

class validation_Result:
    validator:str
    status:str
    actual:float|str
    expected:float|str
    message:str
    score:float