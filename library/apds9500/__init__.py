 from i2cdevice import Device, Register, BitField
from i2cdevice.adapter import Adapter, LookupAdapter



__version__ = '0.0.1'






class APDS9500:
    def __init__(self, i2c_addr=0x73, i2c_dev=None):
        self._i2c_addr = i2c_addr
        self._i2c_dev = i2c_dev
        self._is_setup = False
        self._current_bank = 0 
        # Device definition
        self._apds9500 = Device([0x73], i2c_dev=self._i2c_dev, bit_width=8, registers=(
            Register('BANK_SELECT', 0xEF, fields=(
                BitField('bank', 0b00000001),    
            )),
            #BANK 0 Registers 
            Register('PARTID_LSB', 0x00, bank=0, fields=(
            	BitField('id', 0xFF),
            )),
            Register('PARTID_MSB', 0x01, bank=0, fields=(
            	BitField('id', 0xFF),
            )),
             Register('VERSIONID', 0x02, bank=0, fields=(
            	BitField('version', 0xFF),
            )),
             Register('SUSPEND', 0x03, bank=0, fields=(
            	BitField('suspend', 0xFF),
            )),

            #CURSOR MODES
			Register('CURSOR_MODE', 0x32, bank=0, fields=(
                BitField('mode', 0xFF, read_only=False, adapter=InterruptLookupAdapter({
                    'cursor_use_top': 0b00000001,
                    'cursor_use_bg_model': 0b00000010,
                    'cursor_invert_y': 0b00000100,
                    'cursor_invert_x': 0b00001000,
                    'cursor_top_ratio': 0b00110000
                })),
            )),
            Register('POS_FILTER_START_SIZE_LSB', 0x33, bank=0, fields=(
            	BitField('value', 0xFF),
            )),	
            Register('POS_FILTER_START_SIZE_MSB', 0x34, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('PRO_FILTER_START_SIZE_LSB', 0x35, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('PRO_FILTER_START_SIZE_MSB', 0x36, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_LEFT', 0x37, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_RIGHT', 0x38, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_UP', 0x39, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_DOWN', 0x3A, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_CENTER_X_LSB', 0x3B, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_CENTER_X_MSB', 0x3C, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_CENTER_Y_LSB', 0x3D, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_CENTER_Y_MSB', 0x3E, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_OBJECT_SIZE', 0x8B, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_POSITION_RESOLUTION', 0x8C, bank=0, fields=(
            	BitField('value', 0xFF),
            )),

            #Proximity Mode
            Register('PROX_UPPER_BOUND', 0x69, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('PROX_LOWER_BOUND', 0x6A, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('PROX_S_STATE', 0x6B, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('PROX_AGV_Y', 0x6C, bank=0, fields=(
            	BitField('value', 0xFF),
            )),

            #Automatic Gain and Exposure Controls BANK 0 
            Register('AE_LED_OFF_UB', 0x46, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AE_LED_OFF_LB', 0x47, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AE_EXPOSURE_UB_LSB', 0x48, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AE_EXPOSURE_UB_MSB', 0x49, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AE_EXPOSURE_LB_LSB', 0x4A, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AE_EXPOSURE_LB_MSB', 0x4B, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AG_GAIN_UB', 0x4C, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AG_GAIN_LB', 0x4D, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AG_GAIN_CONTROL', 0x4E, bank=0, fields=(
            	BitField('step', 0x0F),
                BitField('wakeup_ae_mode', 0x10),
            )),
            Register('AG_GAIN_DEFAULT', 0x4F, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AE_EXPOSURE_SELECT', 0x50, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AEAG_MODE', 0x51, bank=0, fields=(
            	BitField('manual_global_gain', 0b00000001),
                BitField('manual_exposure', 0b00000010),
                BitField('maunal_exposure_default', 0b00000100),
                BitField('auto_exposure_enable', 0b00001000),
            )),
            Register('AG_GAIN_ANALOGUE', 0x54, bank=0, fields=(
            	BitField('value',read_only=True , 0xFF),
            )),
            Register('AE_EXPOSURE_TIME_LSB', 0x55, bank=0, fields=(
            	BitField('value',read_only=True , 0xFF),
            )),
            Register('AE_EXPOSURE_TIME_MSB', 0x56, bank=0, fields=(
            	BitField('value',read_only=True , 0xFF),
            )),
            Register('AG_GLOBAL_GAIN', 0x57, bank=0, fields=(
            	BitField('ggn',read_only=True , 0b00000011),
                BitField('global_gain',read_only=True , 0b11110000),
            )),
            Register('LED_OFF_FRAME_AVERAGE_BRIGHTNESS', 0x58, bank=0, fields=(
            	BitField('value',read_only=True , 0xFF),
            )),
            Register('AE_DIRECTION', 0x59, bank=0, fields=(
            	BitField('decrease', 0b00000001),
                BitField('increase', 0b00000010),
            )),
            #Automatic Gain and Exposure Controls BANK 1
            Register('PGA_GAIN_GLOBAL:', 0x42, bank=1, fields=(
            	BitField('value',read_only=True , 0xFF),
            )),
            Register('PGA_GAIN_GGH:', 0x44, bank=1, fields=(
            	BitField('value',read_only=True , 0xFF),
            )),


            #Interupt Controls BANK0
            Register('INTERUPT_MODE', 0x40, bank=0, fields=(
            	BitField('auto_clear', 0b00000001),
                BitField('active_high', 0b00010000),
            )),
            Register('INT_ENABLE_1', 0x41, bank=0, fields=(
                BitField('mode', 0xFF, read_only=False, adapter=InterruptLookupAdapter({
                    'event_up': 0b00000001,
                    'event_down': 0b00000010,
                    'event_left': 0b00000100,
                    'event_right': 0b00001000,
                    'event_forward': 0b00010000,
                    'event_backward': 0b00100000,
                    'event_clockwise': 0b01000000,
                    'event_counterclockwise': 0b10000000
                })),
            Register('INT_ENABLE_2', 0x42, bank=0, fields=(
                BitField('mode', 0xFF, read_only=False, adapter=InterruptLookupAdapter({
                    'event_wave': 0b00000001,
                    'event_proximity': 0b00000010,
                    'event_has_object': 0b00000100,
                    'event_wake_up': 0b00001000,
                    'no_object': 0b10000000
                })),
            Register('INT_FLAG_1', 0x43, bank=0, fields=(
                BitField('mode', 0xFF, read_only=True, adapter=InterruptLookupAdapter({
                    'event_up': 0b00000001,
                    'event_down': 0b00000010,
                    'event_left': 0b00000100,
                    'event_right': 0b00001000,
                    'event_forward': 0b00010000,
                    'event_backward': 0b00100000,
                    'event_clockwise': 0b01000000,
                    'event_counterclockwise': 0b10000000
                })),
            Register('INT_FLAG_2', 0x44, bank=0, fields=(
                BitField('mode', 0xFF, read_only=True, adapter=InterruptLookupAdapter({
                    'event_wave': 0b00000001,
                    'event_proximity': 0b00000010,
                    'event_has_object': 0b00000100,
                    'event_wake_up': 0b00001000,
                    'no_object': 0b10000000
                })),


                
            


            






            #Image Regs BANK 0  
            Register('IMAGE_HEIGHT', 0xAA, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            Register('IMAGE_WIDTH', 0xAB, bank=0, fields=(
            	BitField('value', 0xFF),
            )),
            #Image Regs BANK 1
            Register('IMAGE_H_SCALE', 0x00, bank=1, fields=(
            	BitField('value', 0xFF),
            )),
            Register('IMAGE_V_SCALE', 0x01, bank=1, fields=(
            	BitField('value', 0xFF),
            )),
             Register('IMAGE_H_START', 0x02, bank=1, fields=(
            	BitField('value', 0xFF),
            )),
             Register('IMAGE_V_START', 0x03, bank=1, fields=(
            	BitField('value', 0xFF),
            )),
            Register('IMAGE_TRANSLATION', 0x09, bank=1, fields=(
                BitField('translations', 0xFF, read_only=False, adapter=LookupAdapter({
                    'a_skip_v': 0b00100000,
                    'a_skip_h': 0b00010000,
                    'd_avg_v': 0b0001000,
                    'v_flip': 0b00000010,
                    'h_flip': 0b00000001
                })),
            )),



        ))

	def setBank(self, bank=0):
		self._apds9500.BANK_SELECT.set_bank(bank)
		

	def getBank(self):
		return self._apds9500.BANK_SELECT.get_bank()

