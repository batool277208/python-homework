def is_locked(failed, max_tries=3):
    """Return True if the account is locked."""
    return failed >= max_tries


def tries_left(failed, max_tries=3):
    """Return how many tries are left, or 0 if locked."""
    if is_locked(failed, max_tries):
        return 0
    return max_tries - failed


def status(failed):
    """Return 'locked' or 'active (N tries left)'."""
    left = tries_left(failed)
    if left == 0:
        return "locked"
    return f"active ({left} tries left)"


print(is_locked(2))
print(is_locked(3))
print(is_locked(3, 5))
print(tries_left(1))
print(tries_left(7))
print(status(1))
print(status(4))