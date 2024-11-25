import enum


class TaskType(enum.StrEnum):
    RECEIVE_CONFIGURATION = "RxConfiguration"
    UPLOAD_CONFIGURATION = "TxConfiguration"
