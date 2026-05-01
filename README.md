# Power Meter V.0

An AC power meter project that measures RMS voltage and current using MicroPython on a Raspberry Pi Pico.

## Team

- Dwaipayan Shikari
- Shramana Mondal
- Prattay Barua
- Jayrup Das

## Hardware

| Component | Description |
|-----------|-------------|
| Raspberry Pi Pico | Microcontroller |
| ZMPT101B | AC Voltage Sensor (GPIO 26) |
| ZMCT103C | AC Current Sensor (GPIO 27) |

## Firmware

Written in MicroPython. Samples at 5 kHz (500 samples per reading) and computes RMS values after DC offset removal.

### Calibration Factors

- `VCAL = 268.97` — Voltage calibration
- `ICAL = 16.667 / 3` — Current calibration

### Usage

Flash `Firmware/main.py` to the Pico and monitor via serial REPL.

## Project Structure

```
Hardware/
├── Designs/        # Schematic (schematic.pdf), Easypower project (rp.eprj)
├── Docs/           # Project report and documentation
├── Firmware/       # MicroPython source (main.py)
├── Models/         # 3D renders, photos, and enclosure PDFs
└── README.md       # This file
```

## License
