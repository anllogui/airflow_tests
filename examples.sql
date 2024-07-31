create table num_films_by_actor as
with film_counts as (
select actor_id, count(*) as films from film_actor 
group by actor_id
)
select a.actor_id, a.first_name, a.last_name, f.films
from actor a, film_counts f
where a.actor_id = f.actor_id