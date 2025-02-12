DOMAIN = "openkarotz"

ATTR_NAME = "OpenKarotz"
DEFAULT_NAME = "Open Karotz"


def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""

    def handle_hello(call):
        """Handle the service action call."""
        name = call.data.get(ATTR_NAME, DEFAULT_NAME)

        hass.states.set("openkarotz.hello", name)

    hass.services.register(DOMAIN, "hello", handle_hello)

    # Return boolean to indicate that initialization was successful.
    return True 