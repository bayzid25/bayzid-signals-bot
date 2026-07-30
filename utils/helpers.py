from datetime import datetime

_last_signals = {}


def current_time():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")


def can_send_signal(symbol, side, cooldown_minutes=120):

    key = f"{symbol}_{side}"
    now = datetime.utcnow()

    if key not in _last_signals:
        _last_signals[key] = now
        return True

    elapsed = (now - _last_signals[key]).total_seconds()

    if elapsed >= cooldown_minutes * 60:
        _last_signals[key] = now
        return True

    return False
