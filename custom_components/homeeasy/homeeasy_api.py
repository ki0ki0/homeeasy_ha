"""Home Easy HVAC integration API modile."""
from homeeasy.DeviceState import DeviceState
from homeeasy.HomeEasyLib import HomeEasyLib


class HomeEasyApi:
    mac: str
    _lib: HomeEasyLib
    _state: DeviceState

    def __init__(self, mac):
        """Initialize."""
        self.mac = mac
        self._lib = HomeEasyLib()
        self._lib.connect()
        data = bytes([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self._state = DeviceState(data)

    async def check_mac(self):
        status: DeviceState = await self._lib.request_status_async(self.mac)
        self._lib.disconnect()
        return status.power is not None
