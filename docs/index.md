---
layout: default
title: Docs
---

# Docs

Documentation and resources for docs.

## Topics

{% assign current_url = page.url %}
{% assign pages_list = site.pages | sort: "title" %}
{% assign has_children = false %}

<ul class="topic-list">
{% for node in pages_list %}
  {% assign node_url_parts = node.url | split: '/' %}
  {% assign node_url_parts_size = node_url_parts | size %}
  {% assign node_parent_path = node.url | split: '/' | pop | join: '/' | append: '/' %}
  
  {% if node_parent_path == current_url and node.url != current_url and node.title %}
    {% assign has_children = true %}
    <li>
      <a href="{{ site.baseurl }}{{ node.url }}">{{ node.title }}</a>
      {% if node.description %}
      <p class="topic-description">{{ node.description }}</p>
      {% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>

{% if has_children == false %}
<p><em>No subtopics available yet.</em></p>
{% endif %}

<style>
  .topic-list {
    list-style-type: none;
    padding-left: 0;
  }
  
  .topic-list > li {
    margin-bottom: 1.2em;
  }
  
  .topic-list > li > a {
    font-weight: bold;
    font-size: 1.1em;
    color: #0366d6;
    text-decoration: none;
  }
  
  .topic-list > li > a:hover {
    text-decoration: underline;
  }
  
  .topic-description {
    margin-top: 0.3em;
    margin-bottom: 0;
    color: #555;
  }
</style>

{% include subtopics.html %}