from resturlparse import (build_url, build_hostname, build_params,
                          build_resource_locator)
import pytest


def test_build_hostname():
    func = build_hostname

    assert func("google.com") == "http://google.com/"
    assert func("http://google.com") == "http://google.com/"
    assert func("https://google.com") == "https://google.com/"
    assert func("some_string") == "http://some_string/"
    # Not testing empty hostname since this is mandatory


def test_build_params():
    func = build_params

    assert func({}) == ""

    assert func({"resource":1}) == "?resource=1"

    permutations = [
        "?expand=all&is_closed=false",
        "?is_closed=false&expand=all"
    ]
    assert func({"expand":"all", "is_closed":"false"}) in permutations


def test_build_resource_locator():
    func = build_resource_locator

    assert func(()) == ""
    assert func(["author", ]) == "author"
    assert func(("author", )) == "author"
    assert func(["author", 10]) == "author/10"
    assert func(("author", 10)) == "author/10"
    assert func(["author", 10, "book", 112, "title"]) == "author/10/book/112/title"


def test_build_url():
    # Alternatively, how to use the library

    expected = "https://api.yelp.com/v3/transactions/food_delivery/search"
    actual = build_url(
        hostname="https://api.yelp.com/v3",
        resource_location=("transactions", "food_delivery", "search")
    )

    expected = "http://onlinebookstore.com/authors/10/books/112/title"
    actual = build_url(
        hostname="http://onlinebookstore.com",
        resource_location=("authors", 10, "books", 112, "title")
    )
    assert expected == actual

    expected = "http://apartments.com/53142?filter=studios"
    actual = build_url(
        hostname="apartments.com",
        resource_location=(53142,),
        params={"filter": "studios"}
    )
    assert expected == actual
