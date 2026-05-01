import utime
import math
from machine import ADC, Pin

SAMPLES = 500
SAMPLE_DELAY_US = 200
ADC_VREF = 3.3
ADC_COUNTS = 65535
ICAL = 16.667 / 3

adc_i = ADC(Pin(27))

def print_header():
    print(r"""
===============================================================
   _____   ______          ________ _____  
  |  __ \ / __ \ \        / /  ____|  __ \ 
  | |__) | |  | \ \  /\  / /| |__  | |__) |
  |  ___/| |  | |\ \/  \/ / |  __| |  _  / 
  | |    | |__| | \  /\  /  | |____| | \ \ 
  |_|     \____/   \/  \/   |______|_|  \_\
  
   __  __ ______ _______ ______ _____  
  |  \/  |  ____|__   __|  ____|  __ \ 
  | \  / | |__     | |  | |__  | |__) |
  | |\/| |  __|    | |  |  __| |  _  / 
  | |  | | |____   | |  | |____| | \ \ 
  |_|  |_|______|  |_|  |______|_|  \_\
  
                 POWER METER V.1
       TEAM MEMBERS:
       1)Dwaipayan Shikari
       2)Shramana Mondal
       3)Prattay Barua
       4)Jayrup Das
===============================================================
    """)

def capture_samples():
    raw_sum = 0
    buffer = []
    for _ in range(SAMPLES):
        val = adc_i.read_u16()
        buffer.append(val)
        raw_sum += val
        utime.sleep_us(SAMPLE_DELAY_US)
    offset = raw_sum / SAMPLES
    scaled = [(v - offset) * (ADC_VREF / ADC_COUNTS) * ICAL for v in buffer]
    return scaled

def calc_rms(samples):
    sum_sq = sum(s * s for s in samples)
    return math.sqrt(sum_sq / len(samples))

def calc_frequency(samples):
    crossings = 0
    offset = sum(samples) / len(samples)
    for k in range(1, len(samples)):
        if (samples[k - 1] - offset) <= 0 and (samples[k] - offset) > 0:
            crossings += 1
    if crossings < 2:
        return 0.0
    sample_rate = 1_000_000 / SAMPLE_DELAY_US
    return sample_rate * crossings / (SAMPLES - 1)

def calc_thd(samples):
    N = len(samples)
    fund_real = 0.0
    fund_imag = 0.0
    harm_power = 0.0
    for n in range(N):
        angle = 2 * math.pi * n / N
        fund_real += samples[n] * math.cos(angle)
        fund_imag += samples[n] * math.sin(angle)
    fund_mag = 2 * math.sqrt(fund_real ** 2 + fund_imag ** 2) / N
    for h in range(2, 11):
        h_real = 0.0
        h_imag = 0.0
        for n in range(N):
            angle = 2 * math.pi * h * n / N
            h_real += samples[n] * math.cos(angle)
            h_imag += samples[n] * math.sin(angle)
        h_mag = 2 * math.sqrt(h_real ** 2 + h_imag ** 2) / N
        harm_power += h_mag ** 2
    return math.sqrt(harm_power) / fund_mag * 100 if fund_mag > 0 else 0.0

print_header()
utime.sleep(1)
print("Starting Current, Frequency & THD Measurements...")

while True:
    try:
        samples = capture_samples()
        irms = calc_rms(samples)
        freq = calc_frequency(samples)
        thd = calc_thd(samples)
        print("-" * 40)
        print(f"Current:  {irms:6.3f} A")
        print(f"Freq:     {freq:6.2f} Hz")
        print(f"THD:      {thd:6.2f} %")
        utime.sleep_ms(500)
    except Exception as e:
        print(f"Error: {e}")
        utime.sleep_ms(2000)
