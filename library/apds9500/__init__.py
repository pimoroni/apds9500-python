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
            Register('PARTID_LSB', 0x00, fields=(
            	BitField('id', 0xFF),
            )),
            Register('PARTID_MSB', 0x01, fields=(
            	BitField('id', 0xFF),
            )),
             Register('VERSIONID', 0x02, fields=(
            	BitField('version', 0xFF),
            )),
             Register('SUSPEND', 0x03, fields=(
            	BitField('suspend', 0xFF),
            )),

            #CURSOR MODES
			Register('CURSOR_MODE', 0x32, fields=(
                BitField('mode', 0xFF, read_only=False, adapter=InterruptLookupAdapter({
                    'cursor_use_top': 0b00000001,
                    'cursor_use_bg_model': 0b00000010,
                    'cursor_invert_y': 0b00000100,
                    'cursor_invert_x': 0b00001000,
                    'cursor_top_ratio': 0b00110000
                })),
            )),
            Register('POS_FILTER_START_SIZE_LSB', 0x33, fields=(
            	BitField('value', 0xFF),
            )),	
            Register('POS_FILTER_START_SIZE_MSB', 0x34, fields=(
            	BitField('value', 0xFF),
            )),
            Register('PRO_FILTER_START_SIZE_LSB', 0x35, fields=(
            	BitField('value', 0xFF),
            )),
            Register('PRO_FILTER_START_SIZE_MSB', 0x36, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_LEFT', 0x37, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_RIGHT', 0x38, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_UP', 0x39, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_DOWN', 0x3A, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_CENTER_X_LSB', 0x3B, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_CENTER_X_MSB', 0x3C, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_CENTER_Y_LSB', 0x3D, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_CLAMP_CENTER_Y_MSB', 0x3E, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_OBJECT_SIZE', 0x8B, fields=(
            	BitField('value', 0xFF),
            )),
            Register('CURSOR_POSITION_RESOLUTION', 0x8C, fields=(
            	BitField('value', 0xFF),
            )),

            #Proximity Mode
            Register('PROX_UPPER_BOUND', 0x69, fields=(
            	BitField('value', 0xFF),
            )),
            Register('PROX_LOWER_BOUND', 0x6A, fields=(
            	BitField('value', 0xFF),
            )),
            Register('PROX_S_STATE', 0x6B, fields=(
            	BitField('value', 0xFF),
            )),
            Register('PROX_AGV_Y', 0x6C, fields=(
            	BitField('value', 0xFF),
            )),

            #Automatic Gain and Exposure Controls 
            Register('AE_LED_OFF_UB', 0x46, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AE_LED_OFF_LB', 0x47, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AE_EXPOSURE_UB_LSB', 0x48, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AE_EXPOSURE_UB_MSB', 0x49, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AE_EXPOSURE_LB_LSB', 0x4A, fields=(
            	BitField('value', 0xFF),
            )),
            Register('AE_EXPOSURE_LB_MSB', 0x4B, fields=(
            	BitField('value', 0xFF),
            )),

            

            Register('IMAGE_HEIGHT', 0xAA, fields=(
            	BitField('value', 0xFF),
            )),
            Register('IMAGE_WIDTH', 0xAB, fields=(
            	BitField('value', 0xFF),
            )),




            #BANK 1 Resisters 
            Register('IMAGE_H_SCALE', 0x00, fields=(
            	BitField('value', 0xFF),
            )),
            Register('IMAGE_V_SCALE', 0x01, fields=(
            	BitField('value', 0xFF),
            )),
             Register('IMAGE_H_START', 0x02, fields=(
            	BitField('value', 0xFF),
            )),
             Register('IMAGE_V_START', 0x03, fields=(
            	BitField('value', 0xFF),
            )),
            Register('IMAGE_TRANSLATION', 0x09, fields=(
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

