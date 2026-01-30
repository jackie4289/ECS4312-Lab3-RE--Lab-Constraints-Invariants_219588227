# Contains requirement-driven tests for the dispensing subsystem.
# TODO: create at least 3 test cases

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from dispense import DispenseEvent


def test_negative_dose_rejected():
    """
    Test that attempting to create a DispenseEvent with dose_mg < 0 is rejected.
    Requirement: Constraint - dose_mg must be positive
    """
    try:
        DispenseEvent(patient_id="P001", medication="Aspirin", dose_mg=-5, quantity=1)
        assert False, "Expected ValueError for negative dose"
    except ValueError as e:
        assert "dose_mg must be positive" in str(e)
        print("Test passed: Negative dose rejected")


def test_zero_dose_rejected():
    """
    Test that attempting to create a DispenseEvent with dose_mg = 0 is rejected.
    Requirement: Constraint - dose_mg must be positive
    """
    try:
        DispenseEvent(patient_id="P001", medication="Aspirin", dose_mg=0, quantity=1)
        assert False, "Expected ValueError for zero dose"
    except ValueError as e:
        assert "dose_mg must be positive" in str(e)
        print("Test passed: Zero dose rejected")


def test_valid_dose_accepted():
    """
    Test that creating a DispenseEvent with a positive dose_mg is accepted.
    """
    try:
        event = DispenseEvent(patient_id="P001", medication="Aspirin", dose_mg=500, quantity=1)
        assert event.dose_mg == 500
        print("Test passed: Valid dose accepted")
    except ValueError as e:
        assert False, f"Unexpected error for valid dose: {e}"


def test_duplicate_medication_same_day_rejected():
    """
    Test that the invariant rejects duplicate medication dispensing for the same patient on the same day.
    Requirement: Invariant - A patient may not receive the same medication more than once per day
    """
    # Create first event
    event1 = DispenseEvent(patient_id="P001", medication="Aspirin", dose_mg=500, quantity=1)
    
    # Try to create a second event for the same patient, same medication on the same day
    event2 = DispenseEvent(patient_id="P001", medication="Aspirin", dose_mg=500, quantity=2)
    
    # Check that the invariant is violated
    result = DispenseEvent.invariant_holds([event1], event2)
    assert result is False, "Expected invariant to reject duplicate medication on same day"
    print("Test passed: Duplicate medication on same day rejected")


def test_different_medication_same_day_allowed():
    """
    Test that the invariant allows different medications for the same patient on the same day.
    """
    # Create first event
    event1 = DispenseEvent(patient_id="P001", medication="Aspirin", dose_mg=500, quantity=1)
    
    # Create a second event for the same patient but different medication
    event2 = DispenseEvent(patient_id="P001", medication="Ibuprofen", dose_mg=400, quantity=1)
    
    # Check that the invariant allows this
    result = DispenseEvent.invariant_holds([event1], event2)
    assert result is True, "Expected invariant to allow different medications"
    print("Test passed: Different medication on same day allowed")


def test_same_medication_different_patient_allowed():
    """
    Test that the invariant allows the same medication for different patients on the same day.
    """
    # Create first event
    event1 = DispenseEvent(patient_id="P001", medication="Aspirin", dose_mg=500, quantity=1)
    
    # Create a second event for a different patient with the same medication
    event2 = DispenseEvent(patient_id="P002", medication="Aspirin", dose_mg=500, quantity=1)
    
    # Check that the invariant allows this
    result = DispenseEvent.invariant_holds([event1], event2)
    assert result is True, "Expected invariant to allow same medication for different patients"
    print("Test passed: Same medication for different patient allowed")


def test_negative_quantity_rejected():
    """
    Test that attempting to create a DispenseEvent with quantity ≤ 0 is rejected.
    Requirement: Constraint - quantity must be a positive integer
    """
    try:
        DispenseEvent(patient_id="P001", medication="Aspirin", dose_mg=500, quantity=-1)
        assert False, "Expected ValueError for negative quantity"
    except ValueError as e:
        assert "quantity must be a positive integer" in str(e)
        print("Test passed: Negative quantity rejected")


if __name__ == "__main__":
    test_negative_dose_rejected()
    test_zero_dose_rejected()
    test_valid_dose_accepted()
    test_duplicate_medication_same_day_rejected()
    test_different_medication_same_day_allowed()
    test_same_medication_different_patient_allowed()
    test_negative_quantity_rejected()
    print("\nAll tests passed!")