show databases;

show databases like "weather_database";

create database weather_database;
use weather_database;

drop database weather_database;
drop table weather_details;

select * from weather_details;

create table weather_details(
    clouds						varchar(20),
    humidity					varchar(20),
    temp_min					float,
    temp_max					float,
    main_temp					float,
    feels_like					float,
    wind_gust					float,
    wind_speed					float,
    wind_deg					int,
    rain_1h						float,
    rain_3h						float,
    snow_1h						float,
    snow_3h						float,
    
    weather_description			varchar(20),
    weather_icon				varchar(5),
    weather_main				varchar(20),
    
    city_ID						varchar(20),
    city_Name					varchar(20),
    date_calculated				date,			/* Make this the primary key */
    timezone					int,
    
    latitude					float,
    longitude					float,
    sunrise     				varchar(20),	/* Can be unix OR UTC? */
    sunset	     				varchar(20),
    country						varchar(30),
    main_pressure				int,
    grnd_level					int,
    sea_level					int
);

ALTER TABLE weather_details
ADD CONSTRAINT weather_details_pk PRIMARY KEY(date_calculated);
