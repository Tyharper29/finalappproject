CREATE DATABASE appdev;
Use appdev;
CREATE TABLE honorsurvey_responses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    race TEXT,
    gender VARCHAR(10),
    pregnant VARCHAR(10),
    druguse VARCHAR(10),
    bariaticsurgery VARCHAR(10),
    type2diabetic VARCHAR(10),
    HowLongType2Diabetic VARCHAR(10),
    a1c TEXT,
    pastmonthlostcontrol VARCHAR(10),
    numberoftimeslostcontrol VARCHAR(20),
    compelledtoconsumefood VARCHAR(10),
    unabletostopeating VARCHAR(10),
    lostcontrolbeforet2d VARCHAR(10),
    lostcontrolworse VARCHAR(10),
    soughttreatment VARCHAR(10),
    treatmentaccess TEXT,
    engageintreatment VARCHAR(15),
    mobiletechnology VARCHAR(10),
    tech_apps TEXT,
    tech_benefits TEXT,
    heardaboutstudy TEXT
);
SELECT * FROM honorsurvey_responses;
show tables;






