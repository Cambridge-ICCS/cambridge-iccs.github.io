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

Requisites: some familiarity with Git. 

[Last years' training](https://www.youtube.com/watch?v=ZrwzK4CnJ3Q)
covers the theory behind using Git as presented at the ICCS
summer school last year. The session this year will greatly expand on
the last few minutes of that presentation.

#### Resources

* [Example repository](https://github.com/Cambridge-ICCS/ss23-git)
* [Worksheet](https://docs.google.com/document/d/1gB2h9SNn5ZnAlvUE7mfG1lUDUUQmFyPYHiTyxIFJsKM/)
* There was a mention of [choosealicense.com](https://choosealicense.com/) for information on software licenses.

## Panel on the importance of software engineering goodpractices in climate science

A few resources that were mentioned during the panel:

* Regarding promoting diversity:
     * [Understanding Equity, Diversity and Inclusion Challenges Within the Research Software Community, Chue Hong, N.P., Cohen, J., Jay, C. (2021)](https://link.springer.com/chapter/10.1007/978-3-030-77980-1_30)
     * [N8CIR Recruitment Diversity Checklist](https://n8cir.org.uk/news/diversity-checklist/)

* Regarding reviewing of code in peer review context:
     * [ACM Artifact Review and Badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current)

## Introduction to GPU Programming

Prerequisite for hands-on lab: Basic understanding of the C programming
language.
 * Some knowledge of C programming

#### Resources

* [Slides - Architectures Overview](https://drive.google.com/open?id=1-LoFELBaGN3bdgl8iids6EjicgEv841M&usp=drive_fs)
* [Slides - Introduction to CUDA](https://drive.google.com/open?id=1-lRkvx8XpASl1pVN5MvXxFYN1g_blOYi&usp=drive_fs)
* [Slides - Optimisation](https://drive.google.com/open?id=101ZF26FNlt6IxoKAqKIfgVr9D6Xvq4LR&usp=drive_fs)
* [InstanceHub.com](https://www.instancehub.com/)
* [CUDA Hello World](https://www.instancehub.com/labs/1/)
* [CUDA Lab One](https://www.instancehub.com/labs/2/)
* [CUDA Lab Two](https://www.instancehub.com/labs/3/)

## Introduction to Machine Learning with Pytorch

#### Pre-reading

To make the most of the session we expect participants to arrive with a
(minimal) base-level understanding of machine learning concepts.
In addition to this we will also assume knowledge of some basic mathematics
and python abilities.

Details of these can be
[found on the workshop GitHub repository](https://github.com/Cambridge-ICCS/ml-training-material).

#### Slides

The slides for the course can be found at the following locations:

- [Teaching](https://cambridge-iccs.github.io/slides/ml-training/slides.html)
<!-- - [Applications](https://cambridge-iccs.github.io/slides/ml-training/applications.html) -->

#### Teaching material

The teaching material (including exercises as jupyter notebooks) can be
[found on the workshop GitHub repository](https://github.com/Cambridge-ICCS/ml-training-material)
alongside installation instructions.

## Probabilistic Machine Learning - From Bayesian Linear Regression to Gaussian Processes

Colab notebooks:
* [intro_to_gps.ipynb](https://githubtocolab.com/Cambridge-ICCS/GPJax/blob/sumschool-setup/docs/examples/intro_to_gps.ipynb)
* [regression.ipynb](https://githubtocolab.com/Cambridge-ICCS/GPJax/blob/sumschool-setup/docs/examples/regression.ipynb)
* [intro_to_kernels.ipynb](https://githubtocolab.com/Cambridge-ICCS/GPJax/blob/sumschool-setup/docs/examples/intro_to_kernels.ipynb)
* [spatial.ipynb](https://githubtocolab.com/Cambridge-ICCS/GPJax/blob/sumschool-setup/docs/examples/spatial.ipynb)

Or setup locally:

```
# local instructions
git clone https://github.com/JaxGaussianProcesses/GPJax
cd GPJax
python -m venv venv
source venv/bin/activate
pip install poetry jupyterlab
poetry install --with docs
jupytext --to notebook docs/examples/*.py
cd docs/examples
jupyter notebook
```

## Hackathon

#### Pre-reading

Watch this [introduction
video](https://www.youtube.com/watch?v=RAKttoCPXws) to find out more!
If you would like to suggest a project idea, please use the [team
hackathon ideas/pitches form](https://docs.google.com/forms/d/e/1FAIpQLSe-OU8L8i6UXvFmfFXVCzFa71meOMYG-OuM_EwQgGVL0WELGQ/viewform?usp=sf_link) to propose your project idea.

#### [Hackathon sign-up](https://docs.google.com/spreadsheets/d/1--2aT8WMuOQUqtDiMkpp3aPoIFGD96hQ19VNNeFlL-g/edit#gid=0)

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
