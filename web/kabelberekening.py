RHO_COPPER = 1.724e-8

STANDARD_SIZES = [
    1.5,
    2.5,
    4,
    6,
    10,
    16,
    25,
    35,
    50,
    70,
    95,
    120,
    150,
    185,
    240]


def calculate_cross_section_mm2(
        current_a,
        length_m,
        V_nominal=230,
        allowed_vdrop_pct=3.0):
    if current_a <= 0 or length_m <= 0:
        raise ValueError("current en length moeten > 0 zijn")
    deltaV = V_nominal * (allowed_vdrop_pct / 100.0)
    A_m2 = (RHO_COPPER * current_a * length_m) / deltaV
    A_mm2 = A_m2 * 1e6
    if A_mm2 < 1.5:
        A_mm2 = 1.5
    return A_mm2


def pick_standard_size(required_mm2):
    for s in STANDARD_SIZES:
        if s >= required_mm2:
            return s
    return STANDARD_SIZES[-1]
