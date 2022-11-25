from dino_runner.utils.constants import SONIC, SONIC_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Sonic(PowerUp):
    def __init__(self):
        self.image = SONIC
        self.type = SONIC_TYPE
        super().__init__(self.image, self.type)
