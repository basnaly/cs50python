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

-- Find interviews reports on this day
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

-- According to Ruth, the thief left the bakery on car, find bakery parking lot activities
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

-- According to Eugene thief there was withdrawing some money on the ATM on Leggett Street. Find who withdrew.
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

-- According to Raymond
SELECT caller, receiver, duration, people.name
    FROM phone_calls
    JOIN people
    ON phone_calls.receiver = people.phone_number
    WHERE month = 7 AND day = 28 AND duration < 60;

+----------------+----------------+----------+------------+
|     caller     |    receiver    | duration |    name    |
+----------------+----------------+----------+------------+
| (130) 555-0289 | (996) 555-8899 | 51       | Jack       |
| (499) 555-9472 | (892) 555-8872 | 36       | Larry      |
| (367) 555-5533 | (375) 555-8161 | 45       | Robin      |
| (499) 555-9472 | (717) 555-1342 | 50       | Melissa    |
| (286) 555-6063 | (676) 555-6554 | 43       | James      |
| (770) 555-1861 | (725) 555-3243 | 49       | Philip     |
| (031) 555-6622 | (910) 555-3251 | 38       | Jacqueline |
| (826) 555-1652 | (066) 555-9701 | 55       | Doris      |
| (338) 555-6650 | (704) 555-2131 | 54       | Anna       |
+----------------+----------------+----------+------------+

SELECT airports.city, passengers.passport_number, flights.destination_airport_id
    FROM airports, flights
    JOIN passengers
    ON airports.id = flights.origin_airport_id
    AND flights.id = passengers.flight_id
    WHERE flights.month = 7 AND flights.day = 29 AND airports.city = 'Fiftyville';

+------------+-----------------+------------------------+
|    city    | passport_number | destination_airport_id |
+------------+-----------------+------------------------+
| Fiftyville | 2835165196      | 6                      |
| Fiftyville | 6131360461      | 6                      |
| Fiftyville | 3231999695      | 6                      |
| Fiftyville | 3592750733      | 6                      |
| Fiftyville | 2626335085      | 6                      |
| Fiftyville | 6117294637      | 6                      |
| Fiftyville | 2996517496      | 6                      |
| Fiftyville | 3915621712      | 6                      |
| Fiftyville | 4149859587      | 11                     |
| Fiftyville | 9183348466      | 11                     |
| Fiftyville | 7378796210      | 11                     |
| Fiftyville | 7874488539      | 11                     |
| Fiftyville | 4195341387      | 11                     |
| Fiftyville | 6263461050      | 11                     |
| Fiftyville | 3231999695      | 11                     |
| Fiftyville | 7951366683      | 11                     |
| Fiftyville | 7214083635      | 4                      |
| Fiftyville | 1695452385      | 4                      |
| Fiftyville | 5773159633      | 4                      |
| Fiftyville | 1540955065      | 4                      |
| Fiftyville | 8294398571      | 4                      |
| Fiftyville | 1988161715      | 4                      |
| Fiftyville | 9878712108      | 4                      |
| Fiftyville | 8496433585      | 4                      |
| Fiftyville | 7597790505      | 1                      |
| Fiftyville | 6128131458      | 1                      |
| Fiftyville | 6264773605      | 1                      |
| Fiftyville | 3642612721      | 1                      |
| Fiftyville | 4356447308      | 1                      |
| Fiftyville | 7441135547      | 1                      |
| Fiftyville | 7894166154      | 9                      |
| Fiftyville | 6034823042      | 9                      |
| Fiftyville | 4408372428      | 9                      |
| Fiftyville | 2312901747      | 9                      |
| Fiftyville | 1151340634      | 9                      |
| Fiftyville | 8174538026      | 9                      |
| Fiftyville | 1050247273      | 9                      |
| Fiftyville | 7834357192      | 9                      |
+------------+-----------------+------------------------+