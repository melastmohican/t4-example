import machine
import time

# https://github.com/PaulStoffregen/cores/blob/master/teensy4/tempmon.c
# https://github.com/PaulStoffregen/cores/blob/master/teensy4/imxrt.h

class TempMon:
    TEMPMON_BASE = 0x400D8180
    TEMPSENSE0 = TEMPMON_BASE + 0x0
    TEMPSENSE1 = TEMPMON_BASE + 0x4
    TEMPSENSE2 = TEMPMON_BASE + 0x8
    OCOTP_ANA1 = 0x401F44E0

    def __init__(self):
        self.frequency = 0x03
        self.highAlarmTemp = 85
        self.lowAlarmTemp = 25
        self.panicAlarmTemp = 90

        # Read calibration data from OCOTP fuse
        calibration = machine.mem32[self.OCOTP_ANA1]
        self.s_hotTemp = calibration & 0xFF
        self.s_hotCount = (calibration >> 8) & 0xFFF
        roomCount = (calibration >> 20) & 0xFFF
        self.s_hot_ROOM = float(self.s_hotTemp) - 25.0
        self.s_roomC_hotC = float(roomCount) - float(self.s_hotCount)
        
        ##print("Calibration values:")
        ##print("  HOT TEMP:", self.s_hotTemp)
        ##print("  HOT COUNT:", self.s_hotCount)
        ##print("  ROOM COUNT:", roomCount)

        # Power on temp sensor (clear power-down bit)
        machine.mem32[self.TEMPSENSE0] &= ~0x1

        # Set monitoring frequency
        machine.mem32[self.TEMPSENSE1] = self.frequency & 0xFFFF

        # Configure alarm values
        self.set_alarm_thresholds()

        # Start monitoring (set bit 1)
        machine.mem32[self.TEMPSENSE0] |= 0x2

    def set_alarm_thresholds(self):
        def encode_temp(temp_c):
            return int(self.s_hotCount + ((self.s_hotTemp - temp_c) * self.s_roomC_hotC / self.s_hot_ROOM))

        high = encode_temp(self.highAlarmTemp)
        low = encode_temp(self.lowAlarmTemp)
        panic = encode_temp(self.panicAlarmTemp)

        # Apply encoded values
        machine.mem32[self.TEMPSENSE0] |= (high << 20) & 0xFFF00000
        machine.mem32[self.TEMPSENSE2] |= (panic << 16) & 0x0FFF0000
        machine.mem32[self.TEMPSENSE2] |= (low << 0) & 0x00000FFF

    def read_temp(self):
        # Wait for data ready (bit 2 of TEMPSENSE0)
        while (machine.mem32[self.TEMPSENSE0] & 0x4) == 0:
            time.sleep_ms(1)

        nmeas = (machine.mem32[self.TEMPSENSE0] >> 8) & 0xFFF
        tmeas = self.s_hotTemp - ((float(nmeas) - float(self.s_hotCount)) * self.s_hot_ROOM / self.s_roomC_hotC)
        return tmeas

    def stop(self):
        machine.mem32[self.TEMPSENSE0] &= ~0x2

    def power_down(self):
        machine.mem32[self.TEMPSENSE0] |= 0x1


if __name__ == "__main__":
    print("Teensy 4 Temperature Monitor")
    print("----------------------------")
    
    # Create temperature monitor instance
    tempmon = TempMon()
    
    try:
        while True:
            # Get current temperature
            current_temp = tempmon.read_temp()
            print(f"Current: {current_temp:.2f}°C")
            
            
            # Wait before next reading
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

