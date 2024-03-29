# Выведите 5 категорий товаров, продажи которых принесли наибольшую выручку. 
# Под выручкой понимается сумма произведений стоимости товара на количество проданных единиц.
# Результат должен содержать два столбца: 
#   название категории,
#   выручка от продажи товаров в данной категории.

select category, sum(price*sold_num) AS revenue
from store
group by category
order by revenue DESC
limit 5;



# Выведите в качестве результата одного запроса общее количество заказов,
# сумму стоимостей (бюджетов) всех проектов, средний срок исполнения заказа в днях.
# NB! Для вычисления длительности проекта удобно использовать встроенную функцию datediff().

select 
    count(project_name) as projects,
    sum(budget) as sum,
    avg(datediff(project_finish, project_start)) as time
from project where project_finish is not null;

