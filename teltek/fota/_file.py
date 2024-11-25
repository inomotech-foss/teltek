import enum


class FileType(enum.StrEnum):
    FIRMWARE = "firmware"
    CONFIGURATION = "configuration"
    CERTIFICATE = "certificate"
    BLUE_NRG = "blue_nrg"
    BLE_FW = "ble_fw"
