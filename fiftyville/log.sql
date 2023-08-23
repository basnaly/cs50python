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

SELECT atm_transactions.account_number, bank_accounts.person_id, people.name, people.license_plate, people.phone_number, people.passport_number
    FROM atm_transactions, bank_accounts
    JOIN people
    ON atm_transactions.account_number = bank_accounts.account_number
    AND bank_accounts.person_id = people.id
    WHERE atm_transactions.month = 7 AND atm_transactions.day = 28
    AND atm_transactions.atm_location = 'Leggett Street'
    AND atm_transactions.transaction_type = 'withdraw';

+----------------+-----------+---------+---------------+----------------+-----------------+
| account_number | person_id |  name   | license_plate |  phone_number  | passport_number |
+----------------+-----------+---------+---------------+----------------+-----------------+
| 49610011       | 686048    | Bruce   | 94KL13X       | (367) 555-5533 | 5773159633      |
| 26013199       | 514354    | Diana   | 322W7JE       | (770) 555-1861 | 3592750733      |
| 16153065       | 458378    | Brooke  | QX4YZN3       | (122) 555-4581 | 4408372428      |
| 28296815       | 395717    | Kenny   | 30G67EN       | (826) 555-1652 | 9878712108      |
| 25506511       | 396669    | Iman    | L93JTIZ       | (829) 555-5269 | 7049073643      |
| 28500762       | 467400    | Luca    | 4328GD8       | (389) 555-5198 | 8496433585      |
| 76054385       | 449774    | Taylor  | 1106N58       | (286) 555-6063 | 1988161715      |
| 81061156       | 438727    | Benista | 8X428L0       | (338) 555-6650 | 9586786673      |
+----------------+-----------+---------+---------------+----------------+-----------------+

SELECT caller, receiver, duration
    FROM phone_calls
    WHERE month = 7 AND day = 28 AND duration < 60;

+----------------+----------------+----------+
|     caller     |    receiver    | duration |
+----------------+----------------+----------+
| (130) 555-0289 | (996) 555-8899 | 51       |
| (499) 555-9472 | (892) 555-8872 | 36       |
| (367) 555-5533 | (375) 555-8161 | 45       |
| (499) 555-9472 | (717) 555-1342 | 50       |
| (286) 555-6063 | (676) 555-6554 | 43       |
| (770) 555-1861 | (725) 555-3243 | 49       |
| (031) 555-6622 | (910) 555-3251 | 38       |
| (826) 555-1652 | (066) 555-9701 | 55       |
| (338) 555-6650 | (704) 555-2131 | 54       |
+----------------+----------------+----------+

SELECT airports.city, airport.full_name, passengers.passport_number
    FROM airports, flights
    JOIN passengers
    ON airports.id = flights.origin_airport_id
    AND flights.id = passengers.flight_id
    WHERE month = 7 AND day = 28;