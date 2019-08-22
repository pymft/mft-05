
[tutorials point](https://www.tutorialspoint.com/sqlite/)

[editor](https://sqliteonline.com/)


[chinook sqlite template db](http://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip)


```sql
SELECT tracks.name , 
       milliseconds / 60000,
       artists.name, 
       albums.title, 
       genres.name
       
from 
     tracks 
JOIN albums  ON  tracks.albumid = albums.albumid 
JOIN artists ON  artists.artistid = albums.artistid
JOIN genres  ON  genres.genreid = tracks.genreid 


WHERE artists.name LIKE "Led%"

ORDER BY tracks.name DESC
--LIMIT 50

```