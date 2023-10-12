from hello import answer


def test_answer() -> None:
    assert answer() == "Hello World!"
