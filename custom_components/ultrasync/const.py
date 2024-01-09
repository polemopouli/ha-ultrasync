"""Constants the Interlogix/Hills ComNav UltraSync Hub."""

DOMAIN = "ultrasync"

# Scan Time (in millseconds)
DEFAULT_SCAN_INTERVAL = 1000

DEFAULT_NAME = "UltraSync"

# Services
SERVICE_AWAY = "away"
SERVICE_STAY = "stay"
SERVICE_DISARM = "disarm"
SERVICE_BYPASS = "bypass"
SERVICE_UNBYPASS = "unbypass"
SERVICE_SWITCH = "switch"

# Index used for managing loaded sensors
SENSORS = "sensors"

DATA_COORDINATOR = "coordinator"
DATA_UNDO_UPDATE_LISTENER = "undo_update_listener"
SENSOR_UPDATE_LISTENER = "ultrasync_update_sensors"
