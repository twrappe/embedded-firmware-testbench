# 🔧 Embedded Firmware Test Bench

This project demonstrates an **automated test framework** for validating embedded firmware via **serial communication**.  
It’s designed to simulate real-world SDET Embedded workflows — testing device behavior, automation, and CI integration.

---

## 🧩 System Overview

| Command | Description | Expected Response |
|----------|--------------|-------------------|
| `1` | Turn LED on | `LED_ON` |
| `0` | Turn LED off | `LED_OFF` |
| `S` | Read sensor | `SENSOR:<value>` |
| other | Invalid command | `ERR_CMD` |

---

## ⚙️ How to Run Tests (Real Hardware)

1. Flash the Arduino with `firmware/firmware_test.ino`.
2. Connect the device via USB.
3. Update the correct COM port in `test_firmware.py`.
4. Run:
   ```bash
   cd tests
   pip install -r requirements.txt
   pytest -v --html=report.html