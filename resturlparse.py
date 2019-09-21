
def build_hostname(hostname):
    # NOTE: Add notes about API versions

    if not hostname.startswith("http"):
        hostname = "http://" + hostname
        
    if not hostname.endswith("/"):
        hostname += "/"

    return hostname


def build_params(params):
    # NOTE: take care of the ?
    # Individual functions should take care of the separators only, nothing
    # else.
    formed = ""

    try:
        for (key, value) in params.items():
            formed += "{0}={1}&".format(key, value)
    except ValueError as err:
        print(err)
        return ""
    else:
        final = "?"+formed
        return final[:-1]


def build_resource_locator(ordered_rsc=tuple()):
    # Make sure to note its an ordered iterable so ["string"] or ("string") will
    # be a string
    init_string = ""
    for item in ordered_rsc: 
        init_string += str(item) + "/"

    return init_string[:-1]


def build_url(hostname, resource_location=tuple(), params={}):
    # Be wary about the order of the inputs
    # Depending on the trailing slash situation, return one with trailing slash
    # or not.
    hostnamed = build_hostname(hostname)
    resource_located = build_resource_locator(resource_location)
    parametered = build_params(params)

    return hostnamed + resource_located + parametered
