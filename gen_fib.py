def cached_nth_fib(wrapper):
    """Cached the previous run output of the nth_fib for better improvement."""
    cached = {}

    def inner(n: int) -> int:
        if n not in cached:
            cached[n] = wrapper(n)
        return cached[n]

    return inner


@cached_nth_fib
def nth_fib(n: int) -> int:
    """Return the nth fibonacci number."""
    if n in (1, 2):
        return n - 1  # 1st: 0, 2nd: 1

    return nth_fib(n - 1) + nth_fib(n - 2)
