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