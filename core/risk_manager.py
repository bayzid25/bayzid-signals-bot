from config import (
    ATR_MULTIPLIER,
    RISK_REWARD_1,
    RISK_REWARD_2,
    RISK_REWARD_3
)


class RiskManager:

    @staticmethod
    def calculate_long(entry, atr):

        stop = round(
            entry - (atr * ATR_MULTIPLIER),
            2
        )

        risk = entry - stop

        tp1 = round(
            entry + (risk * RISK_REWARD_1),
            2
        )

        tp2 = round(
            entry + (risk * RISK_REWARD_2),
            2
        )

        tp3 = round(
            entry + (risk * RISK_REWARD_3),
            2
        )

        return {
            "entry": round(entry, 2),
            "stop": stop,
            "tp1": tp1,
            "tp2": tp2,
            "tp3": tp3
        }

    @staticmethod
    def calculate_short(entry, atr):

        stop = round(
            entry + (atr * ATR_MULTIPLIER),
            2
        )

        risk = stop - entry

        tp1 = round(
            entry - (risk * RISK_REWARD_1),
            2
        )

        tp2 = round(
            entry - (risk * RISK_REWARD_2),
            2
        )

        tp3 = round(
            entry - (risk * RISK_REWARD_3),
            2
        )

        return {
            "entry": round(entry, 2),
            "stop": stop,
            "tp1": tp1,
            "tp2": tp2,
            "tp3": tp3
        }
