About
=====

A simple and efficient paginator.

Jinja2
------

Jinja2 is supported via Coffin.

::
	{% with paginate(request, my_queryset) as results %}
	  {{ results.paging }}
	  {% for result in results.objects %}
	    {{ result }}
	  {% endfor %}
	  {{ results.paging }}
	{% endwith %}

Django
------

::
	{% load paging %}
	{% paginate my_queryset from request as results %}
	{{ results.paging }}
	{% for result in results.objects %}
	  {{ result }}
	{% endfor %}
	{{ results.paging }}
