from dino_runner.utils.constants import METALCACTUS, METALCACTUS_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class MetalCactus(PowerUp):
    def __init__(self):
        self.image = METALCACTUS
        self.type = METALCACTUS_TYPE
        super().__init__(self.image, self.type)
