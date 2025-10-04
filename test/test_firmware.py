import pytest
import time
import os

if os.getenv("MOCK_MODE") == "1":
    from tests.mock_serial import MockSerial as Serial
else:
    import serial
    Serial = serial.Serial

@pytest.fixture(scope="module")
def ser():
    s = Serial("COM3", 9600, timeout=1)  # adjust COM port for your system
    time.sleep(2)  # give MCU time to reset
    yield s
    s.close()

def send_and_read(ser, cmd):
    ser.write(cmd.encode())
    return ser.readline().decode().strip()

def test_led_on(ser):
    assert send_and_read(ser, '1') == "LED_ON"

def test_led_off(ser):
    assert send_and_read(ser, '0') == "LED_OFF"

def test_sensor_value(ser):
    response = send_and_read(ser, 'S')
    assert response.startswith("SENSOR:")
    value = int(response.split(":")[1])
    assert 0 <= value <= 1023
