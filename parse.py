#!/usr/bin/env python
from pg_chameleon import sql_token

statement=""" 

-- drop table
DROP TABLE `test`;
-- create table
CREATE   TABLE `test` (
  store_id TINYINT UNSIGNED NULL AUTO_INCREMENT,
  manager_staff_id TINYINT UNSIGNED NOT NULL,
  address_id SMALLINT UNSIGNED NOT NULL,
  `address_txt` varchar (30) NOT NULL default 'default_t;ext',
  `address_dp` double precision (30,2) NOT NULL,
  `test_enum` enum ('a','b'),
  size ENUM('x-small', 'small', 'medium', 'large', 'x-large'),
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (store_id),
  UNIQUE KEY idx_unique_manager (manager_staff_id),
  KEY idx_fk_address_id2 (address_id),
  index
  idx_fk_address_id (address_id,store_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


ALTER TABLE test
ADD COLUMN `count` SMALLINT(6) NOT NULL AFTER `lastname`,
ADD COLUMN `log` VARCHAR(12) NOT NULL AFTER `count`,
ADD COLUMN new_enum ENUM('asd','r') UNSIGNED NOT NULL AFTER `status`,
ADD COLUMN status INT(10) UNSIGNED NOT NULL AFTER `log`;


ALTER TABLE `test`
DROP COLUMN `count` SMALLINT(6) NOT NULL AFTER `lastname`,
ADD COLUMN newstatus INT(10) UNSIGNED NOT NULL AFTER `log`;


				"""

token_sql=sql_token()
token_sql.parse_sql(statement)
#for token in token_sql.tokenised:
#	try:
#		print token["columns"]
#	except:
#		pass
#print parsesql.query_list
