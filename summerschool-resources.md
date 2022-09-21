---
layout:  single
title: Institute of Computing for Climate Science Summer School 2022 - Resources
---

<style>
.contents {
border: solid 1px;
border-color: rgb(140,140,140);
background: rgb(245,245,245);
padding:20px;
margin:20px;
}
div {
  font-size:12.5pt;
  text-align:justify;
}

</style>


{% include summerschool-head.html %}

<div class="contents">
<b>Contents of this page:</b>
<ul id="contents">
</ul>
</div>

## Using Git and GitHub effectively

* [Slides](summerschool-res/git-and-github.pdf)
* [Exercise](summerschool-res/git-exercise.pdf)

## Testing

* [Slides](https://github.com/Cambridge-ICCS/testing/raw/main/presentation/slides.pdf)
* [GitHub repository](https://github.com/Cambridge-ICCS/testing)

## CI and GitHub actions

* [Resources (incuding slides and exercises linked here)](https://github.com/raehik/ga-ci)

## Bridging Fortran and Python for ML

## Automating forward and inverse geoscientific simulation in Firedrake

## Training ML models

## Pairing and code review


 <script>
function convert(t) {
 return t.split(" ").map(function (x) { return x.toLowerCase(); }).join("-");
}

var contents = document.getElementById("contents");
var sections = document.getElementsByTagName("h2");
for(var i = 0; i < sections.length; i++) {
   let item = sections[i];
   let link = document.createElement("a");
   let li = document.createElement("li");
   link.href="#"+convert(item.innerHTML);
   link.innerHTML = item.innerHTML;
   li.appendChild(link);
   contents.appendChild(li);
}
</script>






