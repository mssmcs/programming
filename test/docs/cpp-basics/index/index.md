---
layout: default
title: C++ Basics
---

# C++ Basics

An introduction to fundamental C++ programming concepts for beginners.

## Topics

{% assign current_url = page.url %}
{% assign pages_list = site.pages | sort: "title" %}
{% assign has_children = false %}
{% if current_url == "/docs/cpp-basics/" %}
  {% assign current_sections = "Variables and Data Types,Literals and Expressions,Operators,Control Statements" | split: "," %}
  {% assign has_children = true %}
  <ul class="topic-list">
    {% for section in current_sections %}
      <li>
        <a href="{{ site.baseurl }}/docs/cpp-basics/{{ section | downcase | replace: " ", "-" | uri_escape }}">{{ section }}</a>
        <p class="topic-description">Introduction to {{ section | downcase }}</p>
      </li>
    {% endfor %}
  </ul>
{% endif %}

{% if has_children == false %}
<p><em>No subtopics available yet.</em></p>
{% endif %}

<style>
  .topic-list {
    list-style-type: none;
    padding-left: 0;
  }
  .topic-description {
    color: #666;
    margin-left: 20px;
  }
</style>