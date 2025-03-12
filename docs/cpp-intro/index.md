---
layout: default
title: Home
---

# Computer Science Courses

Welcome to the course materials for CS classes.

## Available Resources

{% assign top_sections = site.pages | sort: "url" %}
<ul class="section-list">
{% for node in top_sections %}
  {% assign node_url_parts = node.url | split: '/' %}
  {% assign node_url_parts_size = node_url_parts | size %}
  {% assign filename = node_url_parts | last %}
  
  {% if node_url_parts_size == 3 and filename == '' and node.title and node.url != '/' %}
    <li>
      <a href="{{ site.baseurl }}{{ node.url }}">{{ node.title }}</a>
      
      <!-- Find subsections for this section -->
      <ul>
      {% for subnode in top_sections %}
        {% assign subnode_url_parts = subnode.url | split: '/' %}
        {% if subnode_url_parts.size == 4 and subnode.url contains node.url and subnode.url != node.url and subnode.title %}
          <li><a href="{{ site.baseurl }}{{ subnode.url }}">{{ subnode.title }}</a></li>
        {% endif %}
      {% endfor %}
      </ul>
    </li>
  {% endif %}
{% endfor %}
</ul>

<style>
  .section-list {
    list-style-type: none;
    padding-left: 0;
  }
  
  .section-list > li {
    margin-bottom: 1.5em;
  }
  
  .section-list > li > a {
    font-weight: bold;
    font-size: 1.1em;
  }
  
  .section-list ul {
    margin-top: 0.5em;
    padding-left: 1.5em;
  }
</style>