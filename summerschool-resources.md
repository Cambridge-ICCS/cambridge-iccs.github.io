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

* [Resources (examples)](https://github.com/raehik/ga-ci)
* [Slides](https://docs.google.com/presentation/d/15V34-oJ1OuG3vjskW2kc_e9rcwHN_Vxe4lPLIUxBAhs/edit?usp=sharing)
* [Exercises](https://docs.google.com/document/d/1rgUY_mDGunFDOCsPZ3atch3px44moxjZV9rxDJOUjgQ/edit?usp=sharing)

## Bridging Fortran and Python for ML

* [Guide and examples of how to interface Python and TensorFlow or PyTorch](https://github.com/Cambridge-ICCS/fortran-ml-bridge)
* [Slides](https://docs.google.com/presentation/d/16m_rW9Q9uL7sT8vOKTt4DUO6BuyxtBocudzFBlZwNiM/edit?usp=sharing)

## Automating forward and inverse geoscientific simulation in Firedrake

* [Notebooks on Google Colab](https://colab.research.google.com/github/firedrakeproject/ICCS-Cam)

## Training ML models

* [Resources](https://github.com/handley-lab/2022-cambridge-iccs)

## Pairing and code review

* [https://codereviewchecklist.com/](https://codereviewchecklist.com/)
* [Pair programming slides](summerschool-res/pair-programming-and-code-review.pdf)

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






