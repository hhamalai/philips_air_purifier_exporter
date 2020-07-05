from textwrap import dedent
from philips_air_purifier.status import is_manual_mode, is_on, fan_speed_to_int


def to_metrics(status):
    return dedent(
        f"""
        air_quality {status["iaql"]}
        is_manual {1 if is_manual_mode(status) else 0}
        is_on {1 if is_on(status) else 0}
        temp {status["temp"]}
        pm25 {status["pm25"]}
        is_purifying {1 if "P" in status["func"] else 0}
        is_humidifying {1 if "H" in status["func"] else 0}
        humidity {status["rh"]}
        target_humidity {status["rhset"]}
        speed {fan_speed_to_int(status)}
        water_level {status["wl"]}
    """
    ).lstrip()
