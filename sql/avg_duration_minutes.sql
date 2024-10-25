select avg(
    cast(
        replace(duration,' min','') as int)
    ) as avg_duration_min
from moviesandtv
where duration like '%min'
