# -*- coding: utf-8 -*-

from buoy.base.data.item import BaseItem


class WIMDA(BaseItem):
    def __init__(self, **kwargs):
        self.press_inch = kwargs.pop('press_inch', None)
        self.press_mbar = kwargs.pop('press_mbar', None)
        self.air_temp = kwargs.pop('air_temp', None)
        self.water_temp = kwargs.pop('water_temp', None)
        self.rel_humidity = kwargs.pop('rel_humidity', None)
        self.abs_humidity = kwargs.pop('abs_humidity', None)
        self.dew_point = kwargs.pop('dew_point', None)
        self.wind_dir_true = kwargs.pop('wind_dir_true', None)
        self.wind_dir_magnetic = kwargs.pop('wind_dir_magnetic', None)
        self.wind_knots = kwargs.pop('wind_knots', None)
        self.wind_meters = kwargs.pop('wind_meters', None)
        super(WIMDA, self).__init__(**kwargs)

    @staticmethod
    def from_nmea(in_datetime, wimda):
        if hasattr(wimda, "b_pressure_bar"):
            wimda.b_pressure_bar *= 1000

        return WIMDA(
            date=in_datetime,
            press_inch=wimda.b_pressure_inch,
            press_mbar=wimda.b_pressure_bar,
            air_temp=wimda.air_temp,
            water_temp=wimda.water_temp,
            rel_humidity=wimda.rel_humidity,
            abs_humidity=wimda.abs_humidity,
            dew_point=wimda.dew_point,
            wind_dir_true=wimda.direction_true,
            wind_dir_magnetic=wimda.direction_magnetic,
            wind_knots=wimda.wind_speed_knots,
            wind_meters=wimda.wind_speed_meters)

    @property
    def press_inch(self):
        """
        :return: Barometric pressure, inches of mercury
        :rtype: Decimal
        """
        return self._press_inch

    @press_inch.setter
    def press_inch(self, value):
        self._press_inch = self._convert_string_to_decimal(value)

    @property
    def press_mbar(self):
        """
        :return: Barometric pressure, bars
        :rtype: Decimal
        """
        return self._press_mbar

    @press_mbar.setter
    def press_mbar(self, value):
        self._press_mbar = self._convert_string_to_decimal(value)

    @property
    def air_temp(self):
        """
        :return: Barometric pressure, bars
        :rtype: Decimal
        """
        return self._air_temp

    @air_temp.setter
    def air_temp(self, value):
        self._air_temp = self._convert_string_to_decimal(value)

    @property
    def water_temp(self):
        """
        :return: Water temperature, degrees Celsius
        :rtype: Decimal
        """
        return self._water_temp

    @water_temp.setter
    def water_temp(self, value):
        self._water_temp = self._convert_string_to_decimal(value)

    @property
    def rel_humidity(self):
        """
        :return: Relative humidity, percent
        :rtype: Decimal
        """
        return self._rel_humidity

    @rel_humidity.setter
    def rel_humidity(self, value):
        self._rel_humidity = self._convert_string_to_decimal(value)

    @property
    def abs_humidity(self):
        """
        :return: Absolute humidity, percent
        :rtype: Decimal
        """
        return self._abs_humidity

    @abs_humidity.setter
    def abs_humidity(self, value):
        self._abs_humidity = self._convert_string_to_decimal(value)

    @property
    def dew_point(self):
        """
        :return: Dew point, degrees C
        :rtype: Decimal
        """
        return self._dew_point

    @dew_point.setter
    def dew_point(self, value):
        self._dew_point = self._convert_string_to_decimal(value)

    @property
    def wind_dir_true(self):
        """
        :return: Wind direction true
        :rtype: Decimal
        """
        return self._wind_dir_true

    @wind_dir_true.setter
    def wind_dir_true(self, value):
        self._wind_dir_true = self._convert_string_to_decimal(value)

    @property
    def wind_dir_magnetic(self):
        """
        :return: Wind direction magnetic
        :rtype: Decimal
        """
        return self._wind_dir_magnetic

    @wind_dir_magnetic.setter
    def wind_dir_magnetic(self, value):
        self._wind_dir_magnetic = self._convert_string_to_decimal(value)

    @property
    def wind_knots(self):
        """
        :return: Wind speed knots
        :rtype: Decimal
        """
        return self._wind_knots

    @wind_knots.setter
    def wind_knots(self, value):
        self._wind_knots = self._convert_string_to_decimal(value)

    @property
    def wind_meters(self):
        """
        :return: Wind speed meters/second
        :rtype: Decimal
        """
        return self._wind_meters

    @wind_meters.setter
    def wind_meters(self, value):
        self._wind_meters = self._convert_string_to_decimal(value)

    def __str__(self):
        return ("Uuid: {uuid}\n"
                "Date: {date}\n"
                "Barometric pressure: {press_inch} in - {press_mbar} mbar\n"
                "Air temperature: {air_temp} ºC\n"
                "Water temperature: {water_temp} ºC\n"
                "Relative humidity: {rel_humidity} %\n"
                "Absolute humidity: {abs_humidity} %\n"
                "Dew point: {dew_point} C\n"
                "Wind direction true: {wind_dir_true} º\n"
                "Wind direction magnetic: {wind_dir_magnetic} º\n"
                "Wind speed: {wind_knots} knots - {wind_meters} m/s").format(**dict(self))
