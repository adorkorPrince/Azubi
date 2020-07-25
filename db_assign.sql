-- 1
SELECT COUNT(u_id)
FROM users

-- 2
SELECT count(u_id) FROM transfer
WHERE send_amount_currency = 'CFA' 

-- 3
SELECT COUNT (DISTINCT u_id)
FROM transfer
WHERE send_amount_currency = 'CFA' 

-- 4
SELECT COUNT(atx_id)
FROM agent_transactions
WHERE when_created BETWEEN '31/12/2017' AND '01/01/2019'

--5
WITH agent_withdrawers AS
(SELECT COUNT (agent_id))
AS net_withdrawers
FROM agent_transactions
HAVING COUNT(amount)
IN (SELECT COUNT(amount)) FROM agent_transactions WHERE amount > 1
AND amount != 0 HAVING COUNT(amount) > (SELECT COUNT)
FROM agent_transactions WHERE amount < 1 AND amount != 0)))
SELECT net_withdrawers
FROM agent_withdrawers;


-- 6

SELECT count(atx.amount) as Volume Summary, ag.city
FROM agent_transactions AS atx INNER JOIN agents AS ag
ON atx.atx_id = ag.agent_id
WHERE atx.when_created BETWEEN NOW()::DATE-EXTRACT(DOW FROM NOW())::INTEGER-7
AND NOW()::DATE-EXTRACT(DOW FROM NOW())::INTEGER
GROUP BY ag.city

-- 7

SELECT count(atx.atx_id) AS volume, ag.city, ag.country
FROM agent_transactions AS atx INNER JOIN agents AS ag
ON atx.atx_id = ag.agent_id
WHERE atx.when_created BETWEEN NOW()::DATE-EXTRACT(DOW FROM NOW())::INTEGER-7
AND NOW()::DATE-EXTRACT(DOW FROM NOW())::INTEGER
GROUP BY ag.country


-- 8

SELECT transfers.kind AS Kind, wallets.ledger_location AS Country, 
SUM (transfers.send_amount_scalar) AS Volume FROM transfers 
INNER JOIN wallets ON transfers.source_wallet_id = wallets.wallet_id 
WHERE (transfers.when_created > (NOW() - INTERVAL '1 week')) 
GROUP BY wallets.ledger_location, transfers.kind; 

--9

SELECT COUNT(transfers.source_wallet_id) 
AS Unique_Senders, 
COUNT (transfer_id) 
AS Transaction_Count, transfers.kind 
AS Transfer_Kind, wallets.ledger_location 
AS Country, 
SUM (transfers.send_amount_scalar) 
AS Volume 
FROM transfers 
INNER JOIN wallets 
ON transfers.source_wallet_id = wallets.wallet_id 
WHERE (transfers.when_created > (NOW() - INTERVAL '1 week')) 
GROUP BY wallets.ledger_location, transfers.kind; 


--#10 

SELECT source_wallet_id, send_amount_scalar 
FROM transfers WHERE send_amount_currency = 'CFA' 
AND (send_amount_scalar>10000000) 
AND (transfers.when_created > (NOW() - INTERVAL '1 month'));












