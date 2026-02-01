def expected_attacks_until_proc(c, tol=1e-12, max_k=20000):
    if c >= 1.0:
        return 1.0
    e = 0.0
    surv = 1.0
    k = 1
    while surv > tol and k < max_k:
        p_k = min(c * k, 1.0)
        contrib = surv * p_k
        e += k * contrib
        surv *= max(0.0, 1.0 - p_k)
        k += 1
    return e


def compute_c(nominal_p, tol=1e-6, max_iter=200):
    target = 1.0 / nominal_p
    low = 1e-8
    high = min(1.0, target * 0.3)
    for i in range(max_iter):
        mid = (low + high) / 2
        exp_n = expected_attacks_until_proc(mid)
        if exp_n < target:
            high = mid
        else:
            low = mid
        if high - low < tol:
            break
    c = (low + high) / 2
    assert abs(expected_attacks_until_proc(c) - target) < 0.01, "No convergence"
    return c
