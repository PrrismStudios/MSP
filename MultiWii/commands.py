class IDENT:
    id = 100
    direction = ">"
    datakey = ['VERSION','MULTITYPE','MSP_VERSION','capability']
    datatype = "3BI"
    def __init__(self, data):
        #if not len(datatype) == datakey:
        #    raise Exception("Length of data must match required data")
        self.data = data

class STATUS:
    id = 101
    direction = ">"
    datakey = ['cycleTime', 'i2c_errors_count', 'sensor', 'flag', 'global_conf.currentSet']
    datatype = "3HIB"
    def __init__(self, data):
        #if not len(datatype) == datakey:
        #    raise Exception("Length of data must match required data")
        self.data = data

class RAW_IMU:
    id = 102
    direction = ">"
    datakey = ['accx', 'accy', 'accz', 'gyrx', 'gyry', 'gyrz', 'magx', 'magy', 'magz']
    datatype = "9h"
    def __init__(self, data):
        """
            Required Data:
            accx: INT16, accy: INT16, accz: INT16
        """
        #if not len(datatype) == datakey:
        #    raise Exception("Length of data must match required data")
        self.data = data

    MSP_IDENT         = {"id": 100, "direction": ">", "data":['VERSION','MULTITYPE','MSP_VERSION','capability'], datatype="3BI"}
    MSP_STATUS        = {"id": 101, "direction": ">", "data":['cycleTime', 'i2c_errors_count', 'sensor', 'flag', 'global_conf.currentSet'], datatype="3HIB"}
    MSP_RAW_IMU       = {"id": 102, "direction": ">", "data":['accx', 'accy', 'accz', 'gyrx', 'gyry', 'gyrz', 'magx', 'magy', 'magz'], datatype="9H"}
    MSP_SERVO         = {"id": 103, "direction": ">", "data":['Servo'], datatype="8H"}
    MSP_MOTOR         = {"id": 104, "direction": ">", "data":['Motor'], datatype="8H"}
    MSP_SET_MOTOR     = {"id": 214, "direction": "<", "data":['Motor'], datatype="8H"}
    MSP_RC            = {"id": 105, "direction": ">", "data":['rcData[RC_CHANS]'], datatype="16H"}
    MSP_SET_RAW_RC    = {"id": 200, "direction": "<", "data":['rcData[RC_CHANS]'], datatype="16H"}
    MSP_RAW_GPS       = {"id": 106, "direction": ">", "data":['GPS_FIX', 'GPS_numSat', 'GPS_coord[LAT]', 'GPS_coord[LON]', 'GPS_altitude', 'GPS_speed', 'GPS_ground_course'], datatype="2B2I3H"}
    MSP_SET_RAW_GPS   = {"id": 201, "direction": "<", "data":['GPS_FIX', 'GPS_numSat', 'GPS_coord[LAT]', 'GPS_coord[LON]', 'GPS_altitude', 'GPS_speed', 'GPS_ground_course'], datatype="2B2I3H"}
    MSP_COMP_GPS      = {"id": 107, "direction": ">", "data":['GPS_distanceToHome', 'GPS_directionToHome', 'GPS_update'], datatype="2HB"}
    MSP_ATTITUDE      = {"id": 108, "direction": ">", "data":['angx', 'angy', 'heading'], datatype="3H"}
    MSP_ALTITUDE      = {"id": 109, "direction": ">", "data":['EstAlt', 'vario'], datatype="IH"}
    MSP_ANALOG        = {"id": 110, "direction": ">", "data":['vbat', 'intPowerMeterSum', 'rssi', 'amperage'], datatype="B3H"}
    MSP_RC_TUNING     = {"id": 111, "direction": ">", "data":['byteRC_RATE', 'byteRC_EXPO', 'byteRollPitchRate', 'byteYawRate', 'byteDynThrPID', 'byteDynThrPID', 'byteThrottle_EXPO'], datatype="7B"}
    MSP_SET_RC_TUNING = {"id": 204, "direction": "<", "data":['byteRC_RATE', 'byteRC_EXPO', 'byteRollPitchRate', 'byteYawRate', 'byteDynThrPID', 'byteDynThrPID', 'byteThrottle_EXPO'], datatype="7B"}
    MSP_PID           = {"id": 112, "direction": ">", "data":[]}
    MSP_SET_PID       = {"id": 202, "direction": "<", "data":[]}
    MSP_BOX           = {"id": 113, "direction": ">", "data":[]}
    MSO_SET_BOX       = {"id": 203, "direction": "<", "data":[]}
    MSP_MISC          = {"id": 114, "direction": ">", "data":[]}
    MSP_SET_MISC      = {"id": 207, "direction": "<", "data":[]}
    MSP_MOTOR_PINS    = {"id": 115, "direction": ">", "data":[]}
    MSP_BOXNAMES      = {"id": 116, "direction": ">", "data":[]}
    MSP_PIDNAMES      = {"id": 117, "direction": ">", "data":[]}
    MSP_WP            = {"id": 118, "direction": ">", "data":[]}
    MSP_SET_WP        = {"id": 209, "direction": "<", "data":[]}
    MSP_BOXIDS        = {"id": 119, "direction": ">", "data":[]}
    MSP_SERVO_CONF    = {"id": 120, "direction": ">", "data":[]}
    MSP_SET_SERVO_CONF= {"id": 212, "direction": "<", "data":[]}
    MSP_ACC_CALIBRATION={"id": 205, "direction": "<", "data":[]}
    MSP_MAG_CALIBRATION={"id": 206, "direction": "<", "data":[]}
    MSP_RESET_CONF    = {"id": 208, "direction": "<", "data":[]}
    MSP_SELECT_SETTING= {"id": 210, "direction": "<", "data":[]}
    MSP_SET_HEAD      = {"id": 211, "direction": "<", "data":[]}
    MSP_BIND          = {"id": 240, "direction": "<", "data":[]}
    MSP_EEPROM_WRITE  = {"id": 250, "direction": "<", "data":[]}