---
layout:  single
title: Institute of Computing for Climate Science Summer School 2024 - Programme
---

<style>
span.other, span.research, span.sci, span.social, span.workshop, span.hack, span.disc {
  border-radius: 4px;
  /* border-style: outset; */
  padding: 3pt;
}
span.other {
  background: rgb(237, 241, 255);
}
span.research {
  background: rgb(250, 238, 210);
}
span.sci,span.research {
  background: rgb(255, 227, 243);
}
span.social {
  background: rgb(255, 251, 204);
}
span.workshop {
  background: rgb(217, 255, 204);
}
span.disc {
  background: rgb(242, 224, 255);
}
span.hack {
  background: rgb(230, 242, 232);
}
.showButton {
    font-size: smaller;
    font-decoration: underline;
    color: #cf5d4e;
    display: block-level;
    clear: left;
    cursor: pointer;
    border: outset;
    padding: 2px;
}
.abstract {
    margin: 10px;
    padding: 10px;
    text-align: justify;
    width: 50vw;
    background: #eee;
    position: relative;
    top: 10px;
    left: 10px;
}
.opt {
	color: gray;
	font-style: italic;
	}
	div {
  font-size:12.5pt;
  text-align:justify;
  }
  .chairs {
  display:none;
  color: purple;
  font-weight: bold;
}
</style>

<style>
div {
  font-size:12.5pt;
  text-align:justify;
}
</style>

During the week, you can [book in a session with one of the RSE team](https://docs.google.com/spreadsheets/d/1iINWYEOdEytngnanVqyq2gAi8DJq4kMusvY6_BI3N0A/edit?usp=sharing) for advice, or to discuss ongoing projects.

## Wednesday 10th July, Centre for Mathematical Sciences

|  Start | End  | Track 1  | Track 2 |
| ------ | ----- | ------- | ------- |
| 14:00  | 15:00 | <span class="workshop" id="workshop-1">Introduction to Git and GitHub</span> | <span class="workshop" id="workshop-2">Intermediate Git and GitHub</span> |
| 15:00  | 15:30 | Coffee & Tea |
| 15:30  | 17:00 | <span class="workshop" name="workshop-3">Scientific Visualisation</span> |

Aromi Pizza and beer from 17:30; board games + Lego

## Thursday 11th July, Centre for Mathematical Sciences

|  Start | End  | Track 1   | Track 2 |
| ------ | ----- | ------- |
| 08:30  | 09:00 | Coffee, tea, and fruit |
| 09:00  | 10:30 | <span class="workshop" name="workshop-4">Introduction to climate and weather modelling</span> | <span class="workshop" name="workshop-5">Explainable data science with the Fluid language</span> |
| 10:30  | 11:00 | Break - tea, coffee, pastries |
| 11:00  | 12:00 | <span class="workshop" name="workshop-4">Introduction to climate and weather modelling</span> | <span class="workshop" name="workshop-6">What can abstract mathematics tell us about programming climate models?</span> |
| 12:00  | 13:30 | Lunch - Church College |
| 13:30  | 15:00 | <span class="workshop" name="workhop-7">OpenMP for GPUs</span> | Research Sofware Engineering with Python |
| 15:00  | 15:30 | Break - tea, coffee |
| 15:30  | 17:00 | <span class="workshop" name="workshop-7">OpenMP for GPUS (lab)</span> | Typing Python with mypy |

Pre-dinner drinks reception and dinner at Madingley Hall.
Transposrt from CMS will depart at 17:15.

## Friday 12th July, CMS

|  Start | End  | Track 1   | Track 2 |
| ------ | ----- | ------- |
| 08:30  | 09:00 | Coffee, tea, and fruit |
| 09:00  | 10:30 | <span class="workshop" name="workshop-8">Introduction to Neural Networks with PyTorch</span> | <span class="workshop" name="workshop-9">Coupling PyTorch with Fortran via FTorch</spa>
| 10:30  | 11:00 | Break - tea, coffee, pastries |
| 11:00  | 12:00 | Introduction to Neural Networks with PyTorch | Code clinic |
| 12:00  | 13:30 | Lunch - Church College |
| 13:30  | 15:00 | Profiling and performacne | Introduction to Comptuational Science in Julia |
| 15:00  | 15:30 | Break - tea, coffee |
| 15:30  | 16:00 | Proifiling and performance testing (lab) | Introduction to Comptuational Science in Jula (lab) |
| 16:00 | 17:00 | <b>Closing Keynote</b> - Evelina Gabasova


Cambridge Wine Merchants and cheese and wine tasting session - 15 min short intro to wines and then wines and nibbles

<div id="abstract-workshop-1">
<p>
This session is aimed to help participants taking their first steps with version control using Git and Github. We will learn the basic principles of Git, how we can upload our code (or other data) to a remote repository, collaborate on it with colleagues, receive their changes, go back to previous versions, etc.
</p>
<p>No more emailing files forth and back, no more "version5.78_final_final_use-this-one"!
</p>
<p>
This is a hands-on session with live-coding and exercises.
</p>
<p>
We will use the Unix shell in this course. Previous experience with using the shell would be helpful, but we will help you out if you haven"t used it before.
</p>
</div>

<div id="abstract-workshop-2">
<p>
This session is intended for participants who want to expand their understanding of Git and GitHub. Building on the basic principles of Git (e.g., the commit, pull, and push commands), we will explore the concept of branching, when to use it, and useful tools for interrogating and manipulating branches. We will also learn about the core concepts of GitHub, how they interact, and how they can be used to build effective software development workflows.
</p><p>
This is a hands-on session with live-coding and exercises.
</p><p>
We will use the Unix shell in this course.
</p>
</div>

<div id="abstract-workshop-3">
In this session we will look at viewing scientific data using python tools. We will cover how to open and access large datasets and prepare them for plotting - e.g. with xarray and (geo)pandas. We will look at libraries that are useful for plotting geospatial data such as cartopy, regionmask, cmocean. As well as technical skills we will discuss considerations for presenting data such as use of scales, colourmaps, and labelling. Finally we will look at examples of structuring matplotlib code for streamlining presentation and enabling easy re-use.
</div>

<div id="abstract-workshop-4">
This session will include a general lecture to explain what the current approach to weather and climate modelling is, and how it links to supercomputing. This will be followed by a short practical session using a pre-built model, with some tasks via a Jupyter Notebook.
</div>

<div id="abstract-workshop-5">
Charts and other visual summaries, curated by journalists and scientists from real-world data and simulations, are how we understand our changing world and the anthopogenic sources of that change. But interpreting these visual outputs is a challenge, even for experts with access to the source code and data. Fluid (f.luid.org) is a new “transparent” programming language, being developed at the Institute of Computing for Climate Science in Cambridge, that can be used to create charts and figures that are linked to data so a user can interactively discover what visual elements actually represent. This is an opportunity to learn about and experiment with a new programming language designed to make climate science more open, intelligible and accessible.
</div>

<div id="abstract-workshop-6">
Category theory is a subfield of mathematics that seeks to expose common underlying structure in other areas of mathematics. It has since also became a foundational technique for understanding logic and programming, with its use both in semantics of formal languages and as a tool for structuring programs. Many concepts in computer programming can be explained from a category theoretic perspective, yielding new insights about how to reason about programs and generalise their definitions. In this session, I will give an overview of a few key ideas that have applications to numerical programming tasks familiar in earth systems modelling. This will provide some fresh perspectives about how to structure and reason about programs both for correctness and efficiency.
</div>


<div id="abstract-workshop-7">
<p>
To make the best use of today"s massively parallel and heterogeneous (both CPU and GPU) computing resources we need to use several programming models. OpenMP is an open specification for a directive based programming model that can take advantage of all the cores on a processor and offload computations to GPUs making only minimal changes to the C, C++ or Fortran source code.
</p>
<p>
This session will serve as an introduction to the OpenMP programming model for GPU acceleration. You will learn how to introduce the directives into your code, and put this into practice using OpenMP to speed up example programs.
</p>
</div>

<div id="abstract-workshop-8">
<p>
This session aims to teach the key theoretical concepts behind machine learning, and offers hands-on training in applying machine learning techniques using PyTorch, along with guidance on structuring resilient and sustainable machine learning code.
</p>
<p>
We will cover both regression and classification, learning about key concepts and applying them in parallel exercises. Once complete participants will have a good framework for building, training, and running neural nets that could be adapted for their own applications.
</p>
<p>
We will demonstrate the application of machine learning with examples from the geoscience domain.
</p>
<p>
<b>Required Pre-Reading</b>: To make the most of the session we expect participants to arrive with a (minimal) base-level understanding of machine learning concepts. In addition to this we will also assume knowledge of some basic mathematics and python abilities.
</p>
</div>

<div id="abstract-workshop-9">
A key focus of many scientific computing domains at present is how to use machine learning to enhance and accelerate traditional simulations. Climate science is no exception, with this topic being part of all VESRI projects. To achieve coupling between ML and numerical models presents a number of technical and scientific challenges, however.

[FTorch](https://github.com/Cambridge-ICCS/FTorch) is a library developed by ICCS to couple PyTorch-based machine learning models to Fortran code with the aim of reducing the burden on scientific researchers. It has already been used in DataWave and M2LInES projects and further afield. In this workshop we will introduce FTorch and review its capabilities before taking participants through the process of coupling a PyTorch model into a Fortran code bin a practical demonstration.

There may also be time for questions/discussion from those seeking to use FTorch in their work, and the developers will be available for code-clinics and discussions throughout the week.

Further information can be found in [this video](https://www.youtube.com/watch?v=-NJGuV6Rz6U) or [this video](https://www.youtube.com/watch?v=Ei6H_BoQ7g4&list=PL27mQJy8eDHmibt_aL3M68x-4gnXpxvZP&index=33).
</div>


<script>
// Helper to add a HTML after another
function insertAfter(newNode, existingNode) {
  existingNode.parentNode.insertBefore(newNode, existingNode.nextSibling);
}
// adds abstract button (and its action) to every workshop tag
function addAbstractClicker() {
  var workshopTitles = document.getElementsByClassName("workshop");
  for (let i = 0; i < workshopTitles.length; i++) {
    let workshop = workshopTitles[i];
    // make a label to have a clicker abstract hing
    let label = document.createElement("span");
    label.innerHTML = "abstract"
    label.className = "showButton";
    label.style.borderStyle = "outset";
    insertAfter(label, workshop);
    label.addEventListener("click",
      function () {
          if (label.style.borderStyle == "outset") {
              label.style.borderStyle = "inset";
              // create abstract box
              let abstractInfo = document.getElementById("abstract-"+workshop.id).innerHTML;
              let abstract = document.createElement("p");
              abstract.id = "info-abstract-"+workshop.id
              abstract.className = "abstract";
              abstract.innerHTML = abstractInfo;
              // add to the page
              insertAfter(abstract, label);
          } else {
            label.style.borderStyle = "outset";
            // remove the abstract
            let abstract = document.getElementById("info-abstract-"+workshop.id);
            console.log(abstract);
            label.parentElement.removeChild(abstract);
          }
        });
  }
}
addAbstractClicker();
</script>
