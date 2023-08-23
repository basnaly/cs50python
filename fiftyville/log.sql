-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find crime scene description
SELECT description
    FROM crime_scene_reports
    WHERE month = 7 AND day = 28
    AND street = 'Humphrey Street';

-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present
-- at the time – each of their interview transcripts mentions the bakery. |
-- | Littering took place at 16:36. No known witnesses.

-- Find bakery activities
SELECT activity, license_plate
    FROM bakery_security_logs
    WHERE month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 5 AND 15
    AND minute BETWEEN 15 AND 20 AND activity = 'entrance';

+----------+---------------+
| activity | license_plate |
+----------+---------------+
| exit     | G412CB7       |
+----------+---------------+

SELECT activity, license_plate
    FROM bakery_security_logs
    WHERE month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 0 AND 20;

+----------+---------------+
| activity | license_plate |
+----------+---------------+
| entrance | R3G7486       |
| entrance | 13FNH73       |
| exit     | 5P2BI95       |
| exit     | 94KL13X       |
| exit     | 6P58WS2       |
| exit     | 4328GD8       |
| exit     | G412CB7       |
+----------+---------------+