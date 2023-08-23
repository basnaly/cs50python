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

-- Ruth    Sometime within ten minutes of the theft, I saw the thief
--         get into a car in the bakery parking lot and drive away.
--         If you have security footage from the bakery parking lot,
--         you might want to look for cars that left the parking lot
--         in that time frame.

-- Eugene  I don't know the thief's name, but it was someone I recognized.
--         Earlier this morning, before I arrived at Emma's bakery, I was
--         walking by the ATM on Leggett Street and saw the thief there
--         withdrawing some money.

-- Raymond As the thief was leaving the bakery, they called someone who
--         talked to them for less than a minute. In the call, I heard the
--         thief say that they were planning to take the earliest flight out
--         of Fiftyville tomorrow. The thief then asked the person on the
--         other end of the phone to purchase the flight ticket.

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

SELECT atm_transactions.account_number, bank_accounts.person_id, people.name, people.license_plate
    FROM atm_transactions, bank_accounts
    JOIN people
    ON atm_transactions.account_number = bank_accounts.account_number
    AND bank_accounts.person_id = people.id
    WHERE month = 7 AND day = 28 AND atm_location = 'Leggett Street'
    AND transaction_type = 'withdraw';
