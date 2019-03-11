import unittest
from datetime import datetime, timezone
from buoy.tests.item_save_thread import ItemSaveThreadTest
from pb200.nmea0183.wimda import WIMDA


def get_item():
    data = {
        'date': datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
        'air_temp': '26.8',
        'press_inch': '30.3273',
        'pres_mbar': '1.027',
        'water_temp': '20.1',
        'rel_humidity': '12.3',
        'abs_humidity': '21.0',
        'dew_point': '2.3',
        'wind_dir_true': '2.0',
        'wind_dir_magnetic': '128.7',
        'wind_knots': '134.6',
        'wind_meters': '0.3'
    }
    return WIMDA(**data)


class TestPB200ItemSaveThread(ItemSaveThreadTest):
    __test__ = True


if __name__ == '__main__':
    unittest.main()
