from formatar_erro import resumir_erro


class RetryProviderError(Exception):
    pass


def test_resume_retry_provider():
    msg = (
        "RetryProvider failed:\n"
        "ChatGPTLightweight: RuntimeError: no reply received\n"
        "Airforce: PaymentRequiredError: Error 402: subscription required\n"
        "OpenRouter: MissingAuthError: Add a api_key"
    )
    info = resumir_erro(RetryProviderError(msg))
    assert len(info.falhas) == 3
    assert info.falhas[0].provedor == "ChatGPTLightweight"
    assert info.sugerir_docker is True
    assert "Nenhum provedor" in info.titulo
