---
layout:  blank
title: ICCS Summer School 2023 - Resources and pre-reading
---

<style>
.contents {
border: solid 1px;
border-color: rgb(140,140,140);
background: rgb(245,245,245);
padding:20px;
margin:20px;
margin-right: calv(35vw - 20px);
}
div {
  font-size:12.5pt;
  text-align:justify;
}

</style>


<div class="contents">
<b>Contents of this page:</b>
<ul id="contents">
</ul>
</div>

## [Programme](https://iccs.cam.ac.uk/system/files/iccs_summer_school_2023_programme.pdf)

## [Handbook](https://iccs.cam.ac.uk/system/files/participant_handbook_online_version_05-07-2023.pdf)

## ICCS RSE Open Office Hours

Through the summer school, attendees can [book a session](https://docs.google.com/spreadsheets/d/1WKZxp3nqpXrIRMRkfFzc71sos-UD-Uy1zeab0c1p7Xc/edit?usp=sharing) with one of the ICCS RSEs
for advice or to discuss ongoing projects.

## Using GitHub effectively for collaborative development

#### Pre-reading

[Using Git and GitHub effectively](https://www.youtube.com/watch?v=ZrwzK4CnJ3Q)

This covers the theory behind using Git as presented at the ICCS
summer school last year. The session this year will greatly expand on
the last few minutes of that presentation.

## Introduction to GPU Programming

Prerequisite for hands-on lab: Basic understanding of the C programming
language.

## Introduction to Machine Learning with Pytorch

#### Pre-reading

To make the most of the session we expect participants to arrive with a
(minimal) base-level understanding of machine learning concepts. In
addition to this we will also assume knowledge of some basic mathematics
and python abilities.

[Details of these can be found on the workshop GitHub repository, along
with resources.](https://github.com/Cambridge-ICCS/ml-training-material)

## Hackathon

#### Pre-reading

Watch this [introduction
video](https://www.youtube.com/watch?v=RAKttoCPXws) to find out more!
If you would like to suggest a project idea, please use the [team
hackathon ideas/pitches form](https://docs.google.com/forms/d/e/1FAIpQLSe-OU8L8i6UXvFmfFXVCzFa71meOMYG-OuM_EwQgGVL0WELGQ/viewform?usp=sf_link) to propose your project idea.

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
