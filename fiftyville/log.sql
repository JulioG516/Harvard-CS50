-- Keep a log of any SQL queries you execute as you solve the mystery.


-- Here i tried to pick the description and the street from the crime scene report to know more about
 SELECT street, description
 FROM crime_scene_reports
 WHERE year = 2021 AND day = 28 AND month = "7";

-- Humphrey Street | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
-- With That information i used a query to get the interview transcript and name of people who was interviewed

SELECT name, transcript
FROM interviews
WHERE year = 2021 AND day = 28 AND month = 7;

-- For the time i know all 3 people on interview mention bakery i will store all that information
-- | Ruth| Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
--| Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
--| Eugene  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

-- Now i know i need to seek out for bakery security logs, the call made by the thief, their withdraw and flight
-- First i will get the name, hour, minute from query from bakery security logs like Ruth said

SELECT name,  bakery_security_logs.hour, bakery_security_logs.minute
FROM people
JOIN bakery_security_logs ON  people.license_plate = bakery_security_logs.license_plate
WHERE bakery_security_logs.year = 2021 AND bakery_security_logs.day = 28 AND bakery_security_logs.month = 7 AND
bakery_security_logs.hour = 10 AND bakery_security_logs.minute >= 15 AND bakery_security_logs.minute <= 25
AND bakery_security_logs.ACTIVITY = "exit";

-- List of possible suspects and how many times they appeared, Counting with the above query and so on
-- Vanessa 1, Bruce 4 X, Barry 1, Luca 2, Sofia 2, Iman 1, Diana 3, Kelsey 2

-- Raymond say the suspect calls someone and ask to buy a ticket out of Fiftyville
-- I tracked all phone calls looking for an call from one of the suspects and a duration less then a minute

SELECT name, phone_calls.duration
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.caller
WHERE year = 2021 AND day = 28 AND month = 7 AND phone_calls.duration <= 60 ORDER BY duration ASC;

-- tracking the receiver call
SELECT name, phone_calls.duration
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.receiver
WHERE year = 2021 AND day = 28 AND month = 7 AND phone_calls.duration <= 60 ORDER BY duration ASC;

-- So in our accumplice we have Larry , Jacqueline, James, Robin, Philip, Melissa, Jack, Anna and Doris as suspects
-- Dismissing Luca because he appeared in our suspect list

-- Knowing more about the Fiftyville airport

SELECT abbreviation, full_name, city, id
FROM airports
WHERE city = "Fiftyville";

--Looking for the  earliest flight out of Fiftyville and to day 29 as Raymond say

SELECT flights.id, city, full_name , flights.hour, flights.minute
FROM airports
JOIN flights
ON airports.id = flights.destination_airport_id
WHERE flights.origin_airport_id = 8
AND flights.year = 2021
AND flights.day = 29
and flights.month = 7 ORDER BY hour;

-- the most early flight is to New York City in LaGuardia Airport with ID 36

-- Checking all pasenger in that Flight id and enumerating it on our list
SELECT name, passengers.passport_number, passengers.seat, passengers.flight_id
FROM people
JOIN passengers
ON people.passport_number = passengers.passport_number
JOIN flights
ON passengers.flight_id = flights.id
WHERE year = 2021 AND day = 29 and month = 7 AND passengers.flight_id = 36;

-- By the Time bruce appeared here three times

-- Checking the withdraw that Eugene sayed on Leggett Street

SELECT account_number
FROM atm_transactions
WHERE year = 2021 AND day = 28 AND month = "7" AND transaction_type = "withdraw" AND atm_location = "Leggett Street";

-- Finding the owner from each account
SELECT name
FROM people
JOIN bank_accounts
ON people.id = bank_accounts.person_id
JOIN atm_transactions
ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = 2021 AND day = 28 AND month = "7" AND transaction_type = "withdraw" AND atm_location = "Leggett Street";

-- Bruce appeared four times in our queries, so he MUST gonna be our suspect
-- We just need to seek out the accumplice by looking for their calls in on previously query

-- Here we found Bruce with a call that last 45 seconds
SELECT name, phone_calls.duration
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.caller
WHERE year = 2021 AND day = 28 AND month = "7" AND phone_calls.duration <= 60 ORDER BY duration ASC;

-- and here we found Robin with a call that last 45 seconds too, meaning they're speaking, so Robin it was Bruce accumplice
SELECT name, phone_calls.duration
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.receiver
WHERE year = 2021 AND day = 28 AND month = "7" AND phone_calls.duration <= 60 ORDER BY duration ASC;

