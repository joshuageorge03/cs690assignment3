"""Write exactly three pytest tests in this file.

TODO 1: Add one test derived from acceptance criterion AC-1.
TODO 2: Add one test derived from acceptance criterion AC-2.
TODO 3: Add one test derived from acceptance criterion AC-3.

Use only the public functions in ``reference``: reservation_disposition and
can_offer_to_waitlist. Do not edit the reference module. Call them with named
arguments, as in tests/test_reference_smoke.py.

Name each test so the acceptance criterion it checks is visible from the test
name or an adjacent comment, for example: def test_ac1_<what_it_checks>().

Put any policy value, such as the grace period, in a named constant marked as
a configured value, as in the at-risk example from the Week 5 lecture.
"""

from reference import can_offer_to_waitlist, reservation_disposition

GRACE_MINUTES = 10  # configured value


def test_ac1_reservation_becomes_releasable_at_grace_period():
    result = reservation_disposition(
        minutes_after_start=GRACE_MINUTES,
        grace_minutes=GRACE_MINUTES,
        checked_in=False,
    )

    assert result == "releasable"


def test_ac2_checked_in_reservation_remains_active_after_grace_period():
    result = reservation_disposition(
        minutes_after_start=GRACE_MINUTES + 5,
        grace_minutes=GRACE_MINUTES,
        checked_in=True,
    )

    assert result == "active"


def test_ac3_waitlist_cannot_receive_unprepared_kit():
    result = can_offer_to_waitlist(
        disposition="releasable",
        preparation_complete=False,
    )

    assert result is False