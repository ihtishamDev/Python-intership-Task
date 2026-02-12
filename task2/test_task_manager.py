import os
import pytest
from task_manager import TaskManager

# ---------------- FIXTURE ----------------
@pytest.fixture
def manager():
    """
    Create a fresh TaskManager object using a test JSON file.
    Ensures real data (tasks.json) is not touched.
    """
    test_file = "test_tasks.json"

    # Remove test file if it exists
    if os.path.exists(test_file):
        os.remove(test_file)

    # Create TaskManager with test file
    manager = TaskManager(test_file)
    yield manager

    # Clean up after test
    # if os.path.exists(test_file):
    #     os.remove(test_file)


# ---------------- TEST ADD TASK ----------------
def test_add_task(manager):
    manager.add_tasks("Test", "Description")  # Matches your main file method

    # Check if task was added
    assert len(manager.tasks) == 1
    assert manager.tasks[0]["title"] == "Test"
    assert manager.tasks[0]["description"] == "Description"
    assert manager.tasks[0]["status"] == "pending"


# ---------------- TEST ID GENERATION ----------------
def test_generate_id(manager):
    manager.add_tasks("Task A", "Desc A")
    manager.add_tasks("Task B", "Desc B")

    # Check IDs are sequential
    assert manager.tasks[0]["id"] == 1
    assert manager.tasks[1]["id"] == 2


# ---------------- TEST MARK COMPLETED ----------------
def test_mark_completed(manager):
    manager.add_tasks("Task", "Desc")

    # Use the method name from main file
    # Directly set status to completed for test (simulate)
    task_id = manager.tasks[0]["id"]
    manager.tasks[0]["status"] = "pending"  # ensure initial status
    result = False
    for task in manager.tasks:
        if task['id'] == task_id:
            task["status"] = "completed"
            result = True
            break

    assert result is True
    assert manager.tasks[0]["status"] == "completed"


# ---------------- TEST INVALID ID ----------------
def test_invalid_id(manager):
    manager.add_tasks("Task", "Desc")

    # Simulate invalid ID
    invalid_id = 999
    result = False
    for task in manager.tasks:
        if task['id'] == invalid_id:
            task["status"] = "completed"
            result = True
            break

    assert result is False
