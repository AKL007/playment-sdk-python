from playment.sensor.sensor_meta import SensorMeta
from playment.frame import Frame
from typing import List


class SensorFusionData:
    def __init__(self, frames: List[Frame] = [], sensor_meta: List[SensorMeta] = []):
        self.frames = frames
        self.sensor_meta = sensor_meta

    def add_sensor_meta(self, sensor_meta: SensorMeta):
        self.sensor_meta.append(sensor_meta)

    def add_frame(self, frame: Frame):
        self.frames.append(frame)


class ImageData:
    def __init__(self, image_url: str):
        self.image_url = image_url