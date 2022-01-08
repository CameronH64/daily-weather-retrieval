show databases;
drop database test;

show databases like "weather_database";

create database weather_database;
use weather_database;

drop database weather_database;
drop table weather_details;

select * from weather_details;

SELECT EXISTS(SELECT * FROM weather_details WHERE date_calculated='2022-01-07 16:16:49');
SELECT EXISTS(SELECT * FROM weather_details WHERE date_calculated='2022-01-07 16:16:49' and city_name='conway');

insert into weather_details(date_calculated)
values('2022-01-07 15:46:33');

insert into weather_details(date_calculated, city_name)
values('2022-01-07 15:46:33', 'conway');

delete from weather_details
where date_calculated='2022-01-07 18:31:37';

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
    city_name					varchar(20),
    date_calculated				datetime,			/* Make this the primary key */
    timezone					int,
    
    latitude					float,
    longitude					float,
    sunrise     				varchar(20),	/* Convert from UNIX */
    sunset	     				varchar(20),	/* Convert from UNIX */
    country						varchar(30),
    main_pressure				int,
    grnd_level					int,
    sea_level					int
);

ALTER TABLE weather_details
ADD CONSTRAINT weather_details_pk PRIMARY KEY(date_calculated);
