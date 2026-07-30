from config import ATR_MULTIPLIER


class RiskManager:

    @staticmethod
    def calculate_long(entry, atr):

        stop = round(entry - (atr * ATR_MULTIPLIER), 2)

        risk = entry - stop

        tp1 = round(entry + (risk * 2), 2)
        tp2 = round(entry + (risk * 3), 2)
        tp3 = round(entry + (risk * 4), 2)

        return {
            "entry": round(entry, 2),
            "stop": stop,
            "tp1": tp1,
            "tp2": tp2,
            "tp3": tp3
        }

    @staticmethod
    def calculate_short(entry, atr):

        stop = round(entry + (atr * ATR_MULTIPLIER), 2)

        risk = stop - entry

        tp1 = round(entry - (risk * 2), 2)
        tp2 = round(entry - (risk * 3), 2)
        tp3 = round(entry - (risk * 4), 2)

        return {
            "entry": round(entry, 2),
            "stop": stop,
            "tp1": tp1,
            "tp2": tp2,
            "tp3": tp3
        }
