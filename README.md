# Power Meter V.0

[![Open Source Hardware](https://img.shields.io/badge/Open%20Source-Hardware-green.svg)](https://oshwa.org/)
[![MicroPython](https://img.shields.io/badge/MicroPython-3.3V-blue.svg)](https://micropython.org/)
[![Raspberry Pi Pico](https://img.shields.io/badge/Raspberry%20Pi-Pico-EC1D24.svg)](https://www.raspberrypi.com/products/raspberry-pi-pico/)
[![License: CERN-OHL-P](https://img.shields.io/badge/License-CERN--OHL--P-red.svg)](https://ohwr.org/cern-ohl)

An AC power meter project that measures RMS current, frequency, and THD using MicroPython on a Raspberry Pi Pico.

![Power Meter](Models/0.png)

## Hardware

| Component | Description |
|-----------|-------------|
| Raspberry Pi Pico | Microcontroller |
| ZMPT101B | AC Voltage Sensor (GPIO 26) |
| ZMCT103C | AC Current Sensor (GPIO 27) |

**Schematic:** [View PDF](Designs/schematic.pdf)

![2D Model](Models/2d_model.jpeg)

## Firmware

Written in MicroPython. Samples at 5 kHz (500 samples per reading) and computes RMS values after DC offset removal.

### Features

- **RMS Current** measurement
- **Frequency** detection via zero-crossing
- **THD** (Total Harmonic Distortion) via FFT analysis
- Real-time serial output

### Calibration Factors

- `ICAL = 16.667 / 3` — Current calibration

### Usage

Flash `Firmware/main.py` to the Pico and monitor via serial REPL.

## Project Structure

```
Hardware/
├── Designs/        # Schematic (schematic.pdf), EasyEDA project (rp.eprj), Gerber files (power.zip)
├── Docs/           # Project report and documentation
├── Firmware/       # MicroPython source (main.py)
├── Models/         # 3D renders, photos, and enclosure PDFs
└── README.md       # This file
```

## Gallery

| 3D Renders | Test Setup |
|------------|------------|
| ![Model 1](Models/1.png) | ![Test Setup](Models/test_setup.jpeg) |
| ![Model 2](Models/2.png) | ![Test](Models/test.jpeg) |
| ![Model 3](Models/3.png) | ![Test Software](Models/test_soft.jpeg) |

## License

This project is certified [Open Source Hardware](https://oshwa.org/definition/) under the [CERN Open Hardware License v2.0](https://ohwr.org/cern-ohl).

[![OSHW](https://img.shields.io/badge/OSHW-Certified-brightgreen.svg)](https://oshwa.org/)
