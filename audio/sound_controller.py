class SoundController:
    def __init__(self):
        self.master_volume = 1.0
        self.sfx_volume = 0.8
        self.muted = False

    def set_volume(self, volume):
        self.master_volume = max(0.0, min(1.0, volume))

    def is_playable(self):
        return not self.muted and self.master_volume > 0