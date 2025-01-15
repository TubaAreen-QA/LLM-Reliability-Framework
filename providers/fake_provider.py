from framework.models.provider_request import provider_request
from framework.models.provider_response import provider_Response

class Fakeprovider:
        def ask(self, request:provider_request):
                if request.prompt =="What is the capital of france?":
                    answer = "paris"
                else:
                    answer = "I dont know"
                return provider_Response(
                    provider="fake"
                    model = "fakegpt"
                    prompt="request.prompt"
                    answer=answer
                    response_time_ms= 120
                    token_usage={
                          "input":8,
                          "output":1
                    }
                    )
