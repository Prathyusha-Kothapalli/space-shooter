class BossEnrageSystem:
    @staticmethod
    def is_enraged(current_hp, max_hp):
        return (current_hp / max_hp) <= 0.3

    @staticmethod
    def get_attack_multiplier(current_hp, max_hp):
        if BossEnrageSystem.is_enraged(current_hp, max_hp):
            return 1.75
        return 1.0