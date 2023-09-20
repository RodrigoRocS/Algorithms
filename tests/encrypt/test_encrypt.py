from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("1", "b")

    assert encrypt_message("roquew", 3) == "qor_weu"

    assert encrypt_message("roquew", 33) == "weuqor"

    assert encrypt_message("roquew", 4) == "we_uqor"
    pass
