from framework.bootstrap.provider_bootstrap import (
    ProviderBootstrap,
)

from framework.factory.provider_factory import (
    ProviderFactory,
)


def test_builtin_providers_registered():

    ProviderBootstrap.initialize()

    providers = ProviderFactory.available()

    assert "fake" in providers

    assert "openai" in providers

    assert "claude" in providers

    assert "gemini" in providers