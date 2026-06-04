def evaluate(result):
    if result["success"]:
        return 100, "OK"
    return 50, result["error"]


def is_good_enough(score):
    return score >= 85
