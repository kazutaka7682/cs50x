-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT description FROM crime_scene_reports WHERE year = 2020 AND month = 7 AND day = 28 AND street = 'Chamberlin Street';
-- 10:15(a.m.)にてChambalin streetのcourthouseにて盗難（アヒルが盗まれる）あり, その際3人の証人にインタビューした(crime_scene_reports)

SELECT transcript FROM interviews WHERE year = 2020 AND month = 7 AND day = 28;
--(Barbara)Fifer Streetにて泥棒がATMでお金を下ろすのを見た(interviews)　泥棒の名前は知らんけど認識はしてた
--(Ruth)10:15から10分以内に裁判所の駐車場から車を盗んで逃走するのを見た(interviews) 探すならその時間帯の逃走車を追うと良いかもね
--(Eugene)泥棒が裁判所を出ようとしたとき, 電話を行った.明日fiftyvilleを出る一番早い便に乗るつもりだと言い, 泥棒は電話の相手に航空券を購入するように頼んだ(interviews)

SELECT license_plate FROM courthouse_security_logs WHERE year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute = 24;
--10:12~10:25までの裁判所警備記録からライセンスプレートを取得, 9個

SELECT name FROM people WHERE license_plate = '0NTHK55';
--前セクションで求めたライセンスに基づいて氏名を把握, 9人

SELECT full_name, abbreviation FROM airports WHERE city LIKE '%fiftyville%';
--fiftyville cityに存在する空港名とその略称を把握

SELECT hour FROM flights WHERE year = 2020 AND month = 7 AND day = 29;
--7月29日にCSF(fiftyville airport)に朝一番で出発する時間を検索

SELECT abbreviation, full_name, city FROM airports WHERE id =
(SELECT destination_airport_idFROM flights WHERE year = 2020 AND month = 7 AND day = 29 AND hour = 8);
--出発時間から算出した朝一番にfiftyvilleを出発する行き先

SELECT passport_number FROM passengers WHERE flight_id
= (SELECT destination_airport_id FROM flights WHERE year = 2020 AND month = 7 AND day = 29 AND hour = 8 AND minute = 20);
--朝一番発の飛行機の乗客パスポート番号の発行

SELECT name, phone_number FROM people WHERE passport_number IN
(SELECT passport_number FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE year = 2020 AND month = 7 AND day = 29 AND hour = 8));
--朝一番に乗る乗客のパスポート番号からその名前を検索

SELECT duration, receiver, caller FROM phone_calls
WHERE year = 2020 AND month = 7 AND day = 28 AND duration <= 60
AND (caller =
(SELECT phone_number FROM people WHERE passport_number IN
(SELECT passport_number FROM passengers WHERE flight_id =
(SELECT id FROM flights WHERE year = 2020 AND month = 7 AND day = 29 AND hour = 8))));
--7月28日の盗難直後に1分以内の会話をした電話を検索し, その発信者と受信者の電話番号を把握

SELECT name FROM people WHERE phone_number = '(826) 555-1652';
--発信者と受信者の氏名を捕捉




--別バージョン


SELECT name
FROM people
JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
WHERE year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute<= 25 AND activity = 'exit';
--裁判所の記録から怪しい時間内に駐車場からでたものを容疑者候補として算出

SELECT name
FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE year = 2020 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Fifer Street';
--早朝に銀行でお金をおろしたと思われる人物の算出

--容疑者候補:Ernest, Danielle, Elizabeth, Russell

SELECT name
FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
WHERE flight_id = (
SELECT id
FROM flights
WHERE year = 2020 AND month = 7 AND day = 29
ORDER BY hour, minute
LIMIT 1);
--7月29日の早朝フライトから乗客の氏名を算出