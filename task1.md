Task 1: Requirements Elicitation
Elicitation Questions for the Medication Dispensing System

1. Should the system check for drug interactions when a patient is prescribed multiple medications simultaneously or within a short timeframe?

2. Patient Prescription Verification. Should the system verify that a patient has a valid, active prescription from a licensed healthcare provider before dispensing any medication?

3: Medication Inventory Management. Should the system track and enforce medication inventory levels, including minimum thresholds and automatic reordering alerts?

4: Age-Appropriate and Weight-Based Dosing. Should the system validate that prescribed doses are appropriate for the patient's age, weight, and medical conditions?

5: Time Granularity for "Per Day" Restrictions. What constitutes a "day" in the context of the "once per day" constraint—a calendar day (00:00-23:59) or a 24-hour rolling window from the first dispensing?

6: Maximum Cumulative Dose Over Time. Is there a maximum cumulative dose limit over longer periods (e.g., weekly, monthly) in addition to daily limits?

7: Medication Substitution and Generic Equivalents. Should the system allow generic substitutions or therapeutic equivalents to be dispensed in place of brand-name medications?

8: Dispense Event Audit and Modification. Once a medication dispensing event is recorded, can it be modified or deleted, and if so, under what conditions (e.g., pharmacist override, time window)?

9: Concurrent Dispensing and Race Conditions. How should the system handle concurrent requests to dispense the same medication to the same patient on the same day (e.g., from multiple pharmacists)?

10: Patient Allergies and Contraindications. Should the system maintain a patient allergy profile and automatically reject dispensing of medications the patient is allergic to?
