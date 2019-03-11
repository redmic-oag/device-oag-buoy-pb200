from pb200.nmea0183.wimda import WIMDA
from buoy.tests.item_db_to_send_thread import DBToSendThreadTest


class TestPB200DBToSendThread(DBToSendThreadTest):
    item_cls = WIMDA
    db_tablename = "pb200"
