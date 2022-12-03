-- User data
DROP TABLE IF EXISTS _user_tier CASCADE;
CREATE TABLE _user_tier
(
    id SMALLINT,
    name VARCHAR(24) NOT NULL UNIQUE,
    CONSTRAINT _user_tier_id_pk PRIMARY KEY (id)
) ;

INSERT INTO _user_tier (id, name)
VALUES  (1, 'visitor'), 
        (2, 'employee'), 
        (3, 'developer'), 
        (4, 'admin'),
        (5, 'root') ;

DROP TABLE IF EXISTS _user CASCADE;
CREATE TABLE _user
(
    id SERIAL,
    username VARCHAR(32) NOT NULL UNIQUE, 
    key VARCHAR(128) NOT NULL,
    tier SMALLINT NOT NULL,
    CONSTRAINT _user_id_pk PRIMARY KEY (id),
    CONSTRAINT _user_tier_id_fk FOREIGN KEY (tier) REFERENCES _user_tier(id)
) ;