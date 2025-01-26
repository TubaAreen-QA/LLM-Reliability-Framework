from providers.fake_provider import FakeProvider
from framework.models.provider_request import ProviderRequest


provider = FakeProvider()


def test_fake_provider_returns_paris():

    request = ProviderRequest(
        provider="fake",
        model="fake-gpt",
        prompt="What is the capital of France?"
    )

    response = provider.ask(request)

    assert response.answer == "Paris"

    assert response.provider == "fake"

    assert response.model == "fake-gpt"

    assert response.provider_confidence == 0.99

def test_unknown_prompt():

    request = ProviderRequest(
        provider="fake",
        model="fake-gpt",
        prompt="Unknown Prompt"
    )

    response = provider.ask(request)

    assert response.answer == "Unknown"

    assert response.provider_confidence == 0.0