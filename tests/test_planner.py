from datetime import date

from planner import completion_rate, days_left, is_urgent, sort_by_due


# This test is already written for you. Read it, then run pytest.
def test_days_left_counts_days_until_due():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 22)
    # Act
    result = days_left(due, today)
    # Assert
    assert result == 4


# Now write the tests below. Use the same three steps: Arrange, Act, Assert.
from datetime import date
# import your functions here, e.g.:
# from tasks import is_urgent, days_left, sort_by_due, completion_rate


# TODO 1: days_left is negative when the task is overdue.
def test_days_left_is_negative_when_overdue():
    today = date(2026, 10, 19)
    due = date(2026, 10, 16)          # 3 days in the past
    assert days_left(due, today) == -3


# TODO 2: is_urgent is True when the task is due tomorrow.
def test_is_urgent_when_due_tomorrow():
    today = date(2026, 10, 19)
    due = date(2026, 10, 20)          # 1 day left
    assert is_urgent(due, today) is True


# TODO 3: is_urgent is True when the task is due in exactly 2 days (the limit).
def test_is_urgent_when_due_exactly_2_days():
    today = date(2026, 10, 19)
    due = date(2026, 10, 21)          # exactly 2 days left
    assert is_urgent(due, today) is True


# TODO 4: is_urgent is False when the task is overdue.
def test_is_urgent_is_false_when_overdue():
    today = date(2026, 10, 19)
    due = date(2026, 10, 18)          # 1 day ago
    assert is_urgent(due, today) is False


# TODO 5: sort_by_due puts the soonest task first.
def test_sort_by_due_puts_soonest_first():
    tasks = [
        {"title": "B", "due": date(2026, 10, 25)},
        {"title": "A", "due": date(2026, 10, 20)},
    ]
    assert [t["title"] for t in sort_by_due(tasks)] == ["A", "B"]


# TODO 6: completion_rate returns 0.0 when there are no tasks.
def test_completion_rate_with_no_tasks():
    assert completion_rate(0, 0) == 0.0


# TODO 7: completion_rate(1, 3) returns 33.3.
def test_completion_rate_rounds_to_one_decimal():
    assert completion_rate(1, 3) == 33.3

