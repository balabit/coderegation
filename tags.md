---
layout: page
title: Tags
---

<div class='list-group'>
  {% assign tags_list = site.tags %}

  {% if tags_list.first[0] == null %}
    {% for tag in tags_list %}
      <a href="#{{ tag }}-ref" class='list-group-item'>{{ tag }}</a>
      <span class='badge'>({{ site.tags[tag].size }})</span>
    {% endfor %}
  {% else %}
    {% for tag in tags_list %}
      <a href="#{{ tag[0] }}-ref" class='list-group-item'>{{ tag[0] }}</a>
      <span class='badge'>({{ tag[1].size }})</span>
    {% endfor %}
  {% endif %}

  {% assign tags_list = nil %}
</div>


{% for tag in site.tags %}
  <h2 class='tag-header' id="{{ tag[0] }}-ref">{{ tag[0] }}</h2>
  <ul>
    {% assign pages_list = tag[1] %}

    {% for node in pages_list %}
      {% if node.title != null %}
        {% if group == null or group == node.group %}
          {% if page.url == node.url %}
          <li class="active"><a href="{{site.baseurl}}/{{node.url}}" class="active">{{node.title}}</a></li>
          {% else %}
          <li><a href="{{site.baseurl}}/{{node.url}}">{{node.title}}</a></li>
          {% endif %}
        {% endif %}
      {% endif %}
    {% endfor %}

    {% assign pages_list = nil %}
    {% assign group = nil %}
  </ul>
{% endfor %}
