# resturlparse
Formulate a URL for a REST API from different parts

Building a URL for a rest API can get annoying. This library provides a function
to easily parse a URL.

## How To
It's pretty simple to use
```
>>> from resturlparse import build_url
>>> build_url("https://api.stipe.com/v1", ("customers",), {"limit": 3})
'https://api.stipe.com/v1/customers?limit=3'

```
