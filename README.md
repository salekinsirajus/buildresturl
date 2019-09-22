# Build REST URL
Intuitive REST API URL formulation.

Building a URL for a rest API can get annoying. This library provides a function
to easily build a URL.

## How To
Let's take a look at a couple examples.

```
>>> from buildresturl import build_url
>>> build_url("https://api.stipe.com/v1", ("customers",), {"limit": 3})
'https://api.stipe.com/v1/customers?limit=3'

>>> build_url("https://yourapi.com/v1", ["jobs",], {"city": "new-york", "level":"senior"})
'https://yourapi.com/v1/jobs?city=new-york&level=senior'

>>> build_url(
...     hostname="api.yourdomain.com/v1",
...     resource_location=("resource", 10, "subresource", 12),
...     params={"filter_x": "true", "filter_y": "open", "expand": "resource_z"}
... )
'http://api.yourdomain.com/v1/resource/10/subresource/12?filter_x=true&expand=resource_z&filter_y=open'

>>> build_url("https://yourapi.com/v1", ["jobs",])
'https://yourapi.com/v1/jobs'

```

- Include your API versions in the hostname. We assume the hostname starts with
  `http`
- Use the `resource_location` parameter to generate REST style resource
  location. Just make sure to pass an ordered iterable, e.g., list or tuple
- pass the query parameters in a dict, i.e., the `params` argument.
