import unittest

from pb200.pb200 import PB200Daemon
from buoy.tests.base_device_tests import BaseDeviceTest


class TestDevicePB200(BaseDeviceTest):
    device_class = PB200Daemon
    DEVICE_NAME = 'PB200'
    config_buoy_file = "tests/support/config/pb200.yaml"
    __test__ = True


if __name__ == '__main__':
    unittest.main()
