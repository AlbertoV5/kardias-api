-- STARTING TABLES

DROP TABLE IF EXISTS clean;
CREATE TABLE clean
(
    patient_id INT NOT NULL,
    gender SMALLINT NOT NULL,
    state TEXT NOT NULL,
    municipality TEXT NOT NULL,
    altitude INT NOT NULL,
    age_days INT NOT NULL,
    weight_kg REAL NOT NULL,
    height_cm REAL NOT NULL,
    appearance TEXT NOT NULL,
    diagnosis_general TEXT NOT NULL,
    cx_previous INT NOT NULL,
    diagnosis_main TEXT NOT NULL,
    date_birth DATE NOT NULL,
    date_procedure DATE NOT NULL,
    surgical_procedure TEXT NOT NULL,
    rachs INT NOT NULL,
    stay_days INT NOT NULL,
    expired SMALLINT NOT NULL,
    CONSTRAINT clean_patient_id_pk PRIMARY KEY (patient_id)
) ;

-- PRIMARY TABLE

DROP TABLE IF EXISTS patient CASCADE;
CREATE TABLE patient 
(
    patient_id INT NOT NULL,
    gender SMALLINT NOT NULL,
    age_days INT NOT NULL,
    weight_kg REAL NOT NULL,
    height_cm REAL NOT NULL,
    cx_previous INT NOT NULL,
    date_birth DATE NOT NULL,
    date_procedure DATE NOT NULL,
    rachs INT NOT NULL,
    stay_days INT NOT NULL,
    expired SMALLINT NOT NULL,
    CONSTRAINT patient_patient_id_pk PRIMARY KEY (patient_id)
) ;

-- SECONDARY TABLES

DROP TABLE IF EXISTS origin CASCADE;
CREATE TABLE origin
(
    token VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    municipality VARCHAR(100) NOT NULL,
    altitude INT NOT NULL,
    CONSTRAINT origin_token_pk PRIMARY KEY (token)
) ;

DROP TABLE IF EXISTS appearance CASCADE;
CREATE TABLE appearance
(
    token VARCHAR(100) NOT NULL,
    appearance VARCHAR(100) NOT NULL,
    keywords VARCHAR(100) NOT NULL,
    CONSTRAINT appearance_appearance_token_pk PRIMARY KEY (token)
) ;

DROP TABLE IF EXISTS diagnosis_general CASCADE;
CREATE TABLE diagnosis_general 
(
    token VARCHAR(200) NOT NULL,
    diagnosis_general VARCHAR(400) NOT NULL,
    keywords VARCHAR(400) NOT NULL,
    CONSTRAINT diagnosis_general_token_pk PRIMARY KEY (token)
) ;

DROP TABLE IF EXISTS diagnosis_main CASCADE;
CREATE TABLE diagnosis_main 
(
    token VARCHAR(200) NOT NULL,
    diagnosis_main VARCHAR(400) NOT NULL,
    keywords VARCHAR(400) NOT NULL,
    CONSTRAINT diagnosis_main_token_pk PRIMARY KEY (token)
) ;

DROP TABLE IF EXISTS surgical_procedure CASCADE;
CREATE TABLE surgical_procedure 
(
    token VARCHAR(200) NOT NULL,
    surgical_procedure VARCHAR(400) NOT NULL,
    keywords VARCHAR(400) NOT NULL,
    CONSTRAINT surgical_procedure_token_pk PRIMARY KEY (token)
) ;

-- TERCIARY TABLES

DROP TABLE IF EXISTS patient_origin;
CREATE TABLE patient_origin
(
    patient_id INT NOT NULL,
    token VARCHAR(200) NOT NULL,
    CONSTRAINT patient_origin_patient_id_fk FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    CONSTRAINT patient_origin_token_fk FOREIGN KEY (token) REFERENCES origin(token),
    CONSTRAINT patient_origin_pk PRIMARY KEY (patient_id, token)
) ;

DROP TABLE IF EXISTS patient_appearance;
CREATE TABLE patient_appearance
(
    patient_id INT NOT NULL,
    token VARCHAR(200) NOT NULL,
    CONSTRAINT patient_appearance_patient_id_fk FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    CONSTRAINT patient_appearance_token_fk FOREIGN KEY (token) REFERENCES appearance(token),
    CONSTRAINT patient_appearance_pk PRIMARY KEY (patient_id, token)
) ;

DROP TABLE IF EXISTS patient_diagnosis_general;
CREATE TABLE patient_diagnosis_general 
(
    patient_id INT NOT NULL,
    token VARCHAR(200) NOT NULL,
    CONSTRAINT patient_diagnosis_general_patient_id_fk FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    CONSTRAINT patient_diagnosis_general_token_fk FOREIGN KEY (token) REFERENCES diagnosis_general(token),
    CONSTRAINT patient_diagnosis_general_pk PRIMARY KEY (patient_id, token)
) ;

DROP TABLE IF EXISTS patient_diagnosis_main;
CREATE TABLE patient_diagnosis_main 
(
    patient_id INT NOT NULL,
    token VARCHAR(200) NOT NULL,
    CONSTRAINT patient_diagnosis_main_patient_id_fk FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    CONSTRAINT patient_diagnosis_main_token_fk FOREIGN KEY (token) REFERENCES diagnosis_main(token),
    CONSTRAINT patient_diagnosis_main_pk PRIMARY KEY (patient_id, token)
) ;

DROP TABLE IF EXISTS patient_surgical_procedure;
CREATE TABLE patient_surgical_procedure 
(
    patient_id INT NOT NULL,
    token VARCHAR(200) NOT NULL,
    CONSTRAINT patient_procedures_patient_id_fk FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    CONSTRAINT patient_procedures_token_fk FOREIGN KEY (token) REFERENCES surgical_procedure(token),
    CONSTRAINT patient_procedures_pk PRIMARY KEY (patient_id, token)
) ;
