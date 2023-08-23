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

-- Find interviews reports

SELECT name, transcript
    FROM interviews
    WHERE year = 2021 AND month = 7 AND day = 28;

-- Find bakery activities
SELECT activity, license_plate, hour, minute
    FROM bakery_security_logs
    WHERE month = 7 AND day = 28 AND hour = 10
    AND minute BETWEEN 5 AND 20;
+----------+---------------+------+--------+
| activity | license_plate | hour | minute |
+----------+---------------+------+--------+
| entrance | R3G7486       | 10   | 8      |
| entrance | 13FNH73       | 10   | 14     |
| exit     | 5P2BI95       | 10   | 16     |
| exit     | 94KL13X       | 10   | 18     |
| exit     | 6P58WS2       | 10   | 18     |
| exit     | 4328GD8       | 10   | 19     |
| exit     | G412CB7       | 10   | 20     |
+----------+---------------+------+--------+

