from app import get_joke

def test_get_joke():
    joke = get_joke()
    assert isinstance(joke, str)
