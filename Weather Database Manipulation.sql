show databases;
drop database test;

show databases like "weather_database";

create database weather_database;
use weather_database;

drop database weather_database;
drop table weather_details;

SELECT EXISTS(SELECT * FROM weather_details WHERE date_calculated='2022-01-07 16:16:49');
SELECT EXISTS(SELECT * FROM weather_details WHERE date_calculated='2022-01-07 16:16:49' and city_name='conway');

insert into weather_details(date_calculated)
values('2022-01-07 15:46:33');

insert into weather_details(date_calculated, city_name)
values('2022-01-07 15:46:33', 'conway');

delete from weather_details
where date_calculated='2022-01-11 18:22:00';

delete from weather_details
where city_name='Little Rock';

delete from weather_details
where weather_main='Clouds';

select * from weather_details;

create table weather_details(
    clouds						int,
    humidity					int,
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
    city_name					varchar(50),
    date_calculated				datetime,			/* Make this the primary key */
    timezone					int,				/* From OWM site, shift in seconds from UTC. */
    
    latitude					float,
    longitude					float,
    sunrise     				int,	/* Convert from UNIX */
    sunset	     				int,	/* Convert from UNIX */
    country						varchar(50),
    main_pressure				int,
    grnd_level					int,
    sea_level					int
);

ALTER TABLE weather_details
ADD CONSTRAINT weather_details_pk PRIMARY KEY(date_calculated);