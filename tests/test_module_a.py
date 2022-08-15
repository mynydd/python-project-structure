from famousworkflow import module_a

def test_simple() -> None:
    assert module_a.somefunc("abc") == "abc added value"
