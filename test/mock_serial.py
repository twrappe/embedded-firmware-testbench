class MockSerial:
    def __init__(self, *args, **kwargs):
        self.last_cmd = None

    def write(self, data):
        self.last_cmd = data.decode().strip()

    def readline(self):
        if self.last_cmd == '1':
            return b"LED_ON\n"
        elif self.last_cmd == '0':
            return b"LED_OFF\n"
        elif self.last_cmd == 'S':
            return b"SENSOR:512\n"
        return b"ERR_CMD\n"

    def close(self):
        pass
