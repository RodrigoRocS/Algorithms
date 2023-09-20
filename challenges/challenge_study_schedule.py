def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if target_time is None:
        return None

    if any(
        not all(isinstance(value, int) for value in period)
        for period in permanence_period
    ):
        return None

    count = sum(
        1 for x in permanence_period if x[0] <= target_time <= x[1]
    )

    return count
    raise NotImplementedError
