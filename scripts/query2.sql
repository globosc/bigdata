select Actor2Geo_FullName, count(*) from exports1 where DATEADDED like '20201006%' group by Actor2Geo_FullName order by 2 desc limit 10;
