Пицца из нашего меню:

{% for entry in catalog -%}
*{{ entry.title }} #{{loop.index}}*
{{ entry.description }}
        '30 см (450гр)'{{ entry.size }} см ({{ entry.weight }}гр) - *{{ choice.price }} руб.*

{% endfor %}
