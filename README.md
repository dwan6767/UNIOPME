# Power Meter V.0

An AC power meter project that measures RMS voltage and current using MicroPython on a Raspberry Pi Pico.

![Power Meter](Models/0.png)

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

**Schematic:** [View PDF](Designs/schematic.pdf)

![2D Model](Models/2d_model.jpeg)

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

## Gallery

| 3D Renders | Test Setup |
|------------|------------|
| ![Model 1](Models/1.png) | ![Test Setup](Models/test_setup.jpeg) |
| ![Model 2](Models/2.png) | ![Test](Models/test.jpeg) |
| ![Model 3](Models/3.png) | ![Test Software](Models/test_soft.jpeg) |

## License
