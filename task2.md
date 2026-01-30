Task 2: Requirement Classification
Classification of Elicitation Questions

1. Should the system check for drug interactions when a patient is prescribed multiple medications simultaneously or within a short timeframe? ,FR
-- This describes a capability or service the system should provide—checking drug interactions when dispensing, therefore it is a functional requirement. 

2. Patient Prescription Verification. Should the system verify that a patient has a valid, active prescription from a licensed healthcare provider before dispensing any medication? ,C
-- This is a validation rule that must be checked before a dispense event is created, therefore it is a constraint.

3: Medication Inventory Management. Should the system track and enforce medication inventory levels, including minimum thresholds and automatic reordering alerts? ,FR
-- This is a feature which where the system tracks and enforces inventory levels, therefore it is a Funcional Requirement. 

4: Age-Appropriate and Weight-Based Dosing. Should the system validate that prescribed doses are appropriate for the patient's age, weight, and medical conditions? ,C
-- This is a validation rule applied when creating a dispense event, therefore it is a constraint.

5: Time Granularity for "Per Day" Restrictions. What constitutes a "day" in the context of the "once per day" constraint—a calendar day (00:00-23:59) or a 24-hour rolling window from the first dispensing? ,I
-- This defines a system-wide rule about how the "once per day" invariant is interpreted, therefore it is an invariant.

6: Maximum Cumulative Dose Over Time. Is there a maximum cumulative dose limit over longer periods (e.g., weekly, monthly) in addition to daily limits? ,I
-- This is a system-wide rule that must hold across multiple dispense events. It requires tracking and aggregating doses for a patient over a time period (week/month) and ensuring the total never exceeds a limit. This is an invariant because it describes a persistent constraint.

7: Medication Substitution and Generic Equivalents. Should the system allow generic substitutions or therapeutic equivalents to be dispensed in place of brand-name medications? ,FR
-- This describes a system capability—the ability to recognize and allow generic substitutions or therapeutic equivalents, therefore it is a functional requirement. 

8: Dispense Event Audit and Modification. Once a medication dispensing event is recorded, can it be modified or deleted, and if so, under what conditions (e.g., pharmacist override, time window)? ,FR
-- This addresses data lifecycle management and auditability—whether dispense events can be modified, deleted, or only appended to, therefore it is a functional requirement. 

9: Concurrent Dispensing and Race Conditions. How should the system handle concurrent requests to dispense the same medication to the same patient on the same day (e.g., from multiple pharmacists)? ,C
-- This describes a validation rule that must be enforced when processing concurrent requests, therefore it is a constraint.

10: Patient Allergies and Contraindications. Should the system maintain a patient allergy profile and automatically reject dispensing of medications the patient is allergic to? ,C
-- This is a validation rule checked before dispensing, therefore it is a constraint.