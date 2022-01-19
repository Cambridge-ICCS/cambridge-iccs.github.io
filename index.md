---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: single
header:
  overlay_image: /assets/images/mock.png
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))

sidebar:

---
<style>
.page__title {
  margin-left: 1.25em;
  margin-top: 0.25em;
  margin-bottom: 1em;
}
#masthead-title {
  display: none; // hide the site title on the home page as the splash has the title
}
</style>

<div class='left'>
<p style='text-align:justify'>
Computational modelling is key to modern climate science. But models are becoming
increasingly complex as we seek to understand our physical world in more depth
and model it at higher fidelity. The <strong>Institute of Computing
for Climate Science</strong> studies and supports the role of software engineering, computer science, artificial
intelligence, and data science within climate science.
</p>

<div class='right'>
<h3 class="archive__subtitle">{{
site.data.ui-text[site.locale].recent_posts | default: "Recent News Posts" }}</h3>

{% if paginator %}
  {% assign posts = paginator.posts %}
{% else %}
  {% assign posts = site.posts %}
{% endif %}
</div>
