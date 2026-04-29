import utime
import math
from machine import ADC, Pin

# ─── Configuration ───────────────────────────────────────────
SAMPLES         = 500       # Number of samples per reading
SAMPLE_DELAY_US = 200       # 200us = 5000Hz sample rate
ADC_VREF        = 3.3
ADC_COUNTS      = 65535

# ─── Calibration ─────────────────────────────────────────────
VCAL = 268.97  # Voltage calibration factor
ICAL = 16.667/3  # Current calibration factor

# ─── Hardware Init ───────────────────────────────────────────
adc_v = ADC(Pin(26))  # ZMPT101B
adc_i = ADC(Pin(27))  # ZMCT103C

def print_header():
   
    print(r"""
================================================================
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
  
                 POWER METER V.0
       TEAM MEMBERS:
       1)Dwaipayan Shikari
       2)Shramana Mondal
       3)Prattay Barua
       4)Jayrup Das
================================================================
    """)

def get_rms_readings():
    v_sum_sq = 0
    i_sum_sq = 0
    v_raw_sum = 0
    i_raw_sum = 0
    
    v_buffer = []
    i_buffer = []

    # 1. Capture Raw Samples
    for _ in range(SAMPLES):
        v_val = adc_v.read_u16()
        i_val = adc_i.read_u16()
        
        v_buffer.append(v_val)
        i_buffer.append(i_val)
        
        v_raw_sum += v_val
        i_raw_sum += i_val
        utime.sleep_us(SAMPLE_DELAY_US)

    # 2. Calculate DC Offset (the 1.65V bias of the sensors)
    v_offset = v_raw_sum / SAMPLES
    i_offset = i_raw_sum / SAMPLES

    # 3. Calculate RMS
    for k in range(SAMPLES):
        # Subtract DC offset and scale to Volts
        v_acc = (v_buffer[k] - v_offset) * (ADC_VREF / ADC_COUNTS) * VCAL
        i_acc = (i_buffer[k] - i_offset) * (ADC_VREF / ADC_COUNTS) * ICAL
        
        v_sum_sq += v_acc * v_acc
        i_sum_sq += i_acc * i_acc

    v_rms = math.sqrt(v_sum_sq / SAMPLES)
    i_rms = math.sqrt(i_sum_sq / SAMPLES)
    
    return v_rms, i_rms

# ─── Main Execution ──────────────────────────────────────────
print_header()
utime.sleep(1)
print("Starting AC Measurements (Vrms & Irms)...")

while True:
    try:
        v_rms, i_rms = get_rms_readings()
        
        # ─── Output & Corruption Logic ───────────────────────
        print("-" * 40)
        
        # Warning if voltage is suspiciously high or out of normal bounds
        if v_rms > 280.0:
            print("![WARNING]! : VOLTAGE READING IS CORRUPTED!")
            print(f"Check Connections. Raw detected: {v_rms:.2f} V")
        else:
           
            print(f"Voltage: {v_rms:6.2f} V (Voltage reading is corrupted ,ask the builder)")
            print(f"Current: {i_rms:6.3f} A")
        
        utime.sleep_ms(500)
        
    except Exception as e:
        print(f"Error: {e}")
        utime.sleep_ms(2000)
