# -*- coding: utf-8 -*-

import logging.config

from datetime import datetime, timezone

import pynmea2

from buoy.base.device.device import Device
from buoy.base.device.threads.reader import DeviceReader
from buoy.base.service.daemon import Daemon
from buoy.base.utils.argsparse import parse_args
from buoy.base.utils.config import *
from buoy.base.database import DeviceDB
from pb200.nmea0183.wimda import WIMDA


logger = logging.getLogger(__name__)

DEVICE_NAME = "pb200"
DAEMON_NAME = "pb200"


class PB200Reader(DeviceReader):
    def __init__(self, **kwargs):
        super(PB200Reader, self).__init__(**kwargs)

    def parser(self, data):
        try:
            item = pynmea2.parse(data)
            if item.sentence_type == 'MDA':
                return WIMDA.from_nmea(datetime.now(tz=timezone.utc), item)
        except pynmea2.nmea.ParseError as e:
            logger.debug(e)


class PB200(Device):
    def __init__(self, *args, **kwargs):
        device_name = kwargs.pop('device_name', 'PB200')
        super(PB200, self).__init__(self, device_name=device_name, cls_reader=PB200Reader, *args, **kwargs)


class PB200Daemon(PB200, Daemon):
    def __init__(self, name, **kwargs):
        db_conf = kwargs.pop('database')
        service_conf = kwargs.pop('service')
        db = DeviceDB(db_config=db_conf, db_tablename=name, cls_item=WIMDA)

        Daemon.__init__(self, daemon_name=DAEMON_NAME, daemon_config=service_conf)
        PB200.__init__(self, db=db, **kwargs)

    def before_stop(self):
        self.disconnect()


def run(config_buoy: str, config_log_file: str):
    logging.config.dictConfig(load_config_logger(path_config=config_log_file))
    buoy_config = load_config(path_config=config_buoy)

    daemon = PB200Daemon(name=DEVICE_NAME, **buoy_config)
    daemon.start()


def main():
    args = parse_args(path_config='/etc/buoy/pb200')
    run(config_buoy=args.config_file, config_log_file=args.config_log_file)


if __name__ == "__main__":
    main()
