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
a.workhop:hover {
  text-decoration: underline;
}
.workshop {
  font-weight:700;
  color: #1d3ddf;
  cursor: pointer;
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
    color: #eee;
    background: #5d4cfe;
    display: block-level;
    clear: left;
    cursor: pointer;
    border: outset;
    padding: 2px;
}
.showButton:active {
    border: inset;
}
.showButton:hover {
    border: outset;
    background: #8d8cff
}.abstract {
    margin: 10px;
    padding: 10px;
    text-align: justify;
    width: 50vw;
    top: 25vh;
    left: 25vw;
    background: #eee;
    position: fixed;
    z-index: 10;
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
#abstracts div {
	display: none;
}
body {
  z-index: 0;
}
#layer {
  background: rgba(0,0,0,0.5);
  z-index: 2;
  display: none;
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  height: 100vh;
  width: 100vw;
}
td:nth-child(3), td:nth-child(4) {
  padding-left: 2em;
  padding-right: 2em;
}
</style>

<style>
div {
  font-size:12.5pt;
  text-align:justify;
}
</style>

<div id="layer"></div>

During the week, you can [book in a session with one of the RSE team](https://docs.google.com/spreadsheets/d/1iINWYEOdEytngnanVqyq2gAi8DJq4kMusvY6_BI3N0A/edit?usp=sharing) for advice, or to discuss ongoing projects.

<b class="workshop" onMouseOver="highlightTitles('rgb(250, 242, 92)')" onMouseOut="highlightTitles('rgb(255,255,255)')">Click a title to see its abstract</b>

## Wednesday 10th July, Centre for Mathematical Sciences

|  Start | End  | Track 1  | Track 2 |
| ------ | ----- | ------- | ------- |
| 14:00  | 14:15 | Introduction - Please be seated by 2pm |
| 14:15  | 15:45 | <a class="workshop" name="workshop-1">Introduction to Git and GitHub</a> | <a class="workshop" name="workshop-2">Intermediate Git and GitHub</a> |
| 15:45  | 16:15 | Coffee & Tea |
| 16:15  | 17:45 | <a class="workshop" name="workshop-3">Scientific Visualisation</a> | Code clinic

Aromi Pizza and beer from 17:45; board games + Lego

## Thursday 11th July, Centre for Mathematical Sciences

|  Start | End  | Track 1   | Track 2 |
| ------ | ----- | ------- |
| 08:15  | 09:00 | Continental breakfast at the CMS |
| 09:00  | 10:30 | <a class="workshop" name="workshop-10">Introduction to Neural Networks with PyTorch</a> | <a class="workshop" name="workshop-11">Coupling PyTorch with Fortran via FTorch</a>
| 10:30  | 11:00 | Break - tea, coffee, pastries |
| 11:00  | 12:00 | <a class="workshop" name="workshop-10">Introduction to Neural Networks with PyTorch</a> | Code clinic |
| 12:00  | 13:30 | Lunch - Church College |
| 13:30  | 15:00 | <a class="workshop" name="workshop-7">OpenMP for GPUs</a> | <a class="workshop" name="workshop-8">Research Sofware Engineering with Python</a> |
| 15:00  | 15:30 | Break - tea, coffee |
| 15:30  | 17:00 | <a class="workshop" name="workshop-7">OpenMP for GPUs (lab)</a> | <a class="workshop" name="workshop-9">Typing Python with mypy</a> |

Pre-dinner drinks reception and dinner at Madingley Hall.
Transposrt from CMS will depart at 17:15.

## Friday 12th July, CMS

|  Start | End  | Track 1   | Track 2 |
| ------ | ----- | ------- |
| 08:15  | 09:00 | Continental breakfast at the CMS |
| 09:00  | 10:30 | <a class="workshop" name="workshop-4">Introduction to climate and weather modelling</a> | <a class="workshop" name="workshop-5">Explainable data science with the Fluid language</a> |
| 10:30  | 11:00 | Break - tea, coffee, pastries |
| 11:00  | 12:00 | <a class="workshop" name="workshop-4">Introduction to climate and weather modelling</a> | <a class="workshop" name="workshop-6">What can abstract mathematics tell us about programming climate models?</a> |
| 12:00  | 13:30 | Lunch - Church College |
| 13:30  | 15:00 | <a class="workshop" name="workshop-12">Profiling and performance testing</a> | <a class="workshop" name="workshop-13">Introduction to Comptuational Science in Julia</a> |
| 15:00  | 15:30 | Break - tea, coffee |
| 15:30  | 16:00 | <a class="workshop" name="workshop-12">Profiling and performance testing (lab)</a>  | <a class="workshop" name="workshop-13">Introduction to Comptuational Science in Jula (lab)</a> |
| 16:00 | 17:00 | <b>Closing Keynote</b> - Evelina Gabasova


Cambridge Wine Merchants and cheese and wine tasting session - 15 min short intro to wines and then wines and nibbles

<section id="abstracts">
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
<p>
In this session we will look at viewing scientific data using python tools. We will cover how to open and access large datasets and prepare them for plotting - e.g. with xarray and (geo)pandas. We will look at libraries that are useful for plotting geospatial data such as cartopy, regionmask, cmocean. As well as technical skills we will discuss considerations for presenting data such as use of scales, colourmaps, and labelling. Finally we will look at examples of structuring matplotlib code for streamlining presentation and enabling easy re-use.
</p>
</div>

<div id="abstract-workshop-4">
<p>
This session will include a general lecture to explain what the current approach to weather and climate modelling is, and how it links to supercomputing. This will be followed by a short practical session using a pre-built model, with some tasks via a Jupyter Notebook.
	
<ol>
  <li>Fundamentals of dynamics and physics for the atmosphere and ocean</li>
  <li>Numerical methods used in weather and climate prediction</li>
  <li>The supercomputing challenges in weather and climate simulation</li>
  <li>Aspects of Machine Learning
    <ul><li>ML emulators</li>
      <li>Improvement of parameterizations</li>
      <li>Uncertainty quantification</li>
      <li>ML techniques for operational weather forcast</li>
      </ul></li>
    </ol>

The practical session will be based on _Observation System Simulation Experience for ocean surface pCO2 over the Atlantic Ocean_.

Sparse data coverage and the lack of observations covering the full seasonal cycle challenge mapping methods and result in noisy reconstructions of surface ocean pCO2 and disagreements between different models. We explored design options for a future augmented Atlantic-scale observing system that would optimally combine data streams from various platforms and contribute to reduce the bias in reconstructed surface ocean pCO2 fields and sea–air CO2 fluxes. 
</p>
</div>

<div id="abstract-workshop-5">
<p>
Charts and other visual summaries, curated by journalists and scientists from real-world data and simulations, are how we understand our changing world and the anthopogenic sources of that change. But interpreting these visual outputs is a challenge, even for experts with access to the source code and data. Fluid (f.luid.org) is a new “transparent” programming language, being developed at the Institute of Computing for Climate Science in Cambridge, that can be used to create charts and figures that are linked to data so a user can interactively discover what visual elements actually represent. This is an opportunity to learn about and experiment with a new programming language designed to make climate science more open, intelligible and accessible.
</p>
</div>

<div id="abstract-workshop-6">
<p>
Category theory is a subfield of mathematics that seeks to expose common underlying structure in other areas of mathematics. It has since also became a foundational technique for understanding logic and programming, with its use both in semantics of formal languages and as a tool for structuring programs. Many concepts in computer programming can be explained from a category theoretic perspective, yielding new insights about how to reason about programs and generalise their definitions. In this session, I will give an overview of a few key ideas that have applications to numerical programming tasks familiar in earth systems modelling. This will provide some fresh perspectives about how to structure and reason about programs both for correctness and efficiency.
</p>
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
Python is the tool of choice for many applications in research, from data processing and analysis to producing plots and figures for publications.
</p><p>
However, much of this code is written to a base standard to achieve a single goal. Further, it is often written in a fluid style as interesting science appears. Whilst this is fast in the short-term, it does not lend well to re-usability by others (or even the future author!) or to well-written and structured code.
</p><p>
In this session we will explore a number of tools and techniques that can be easily applied to improve your code's quality, readability, reduce bugs, and facilitate re-use.
</p>
</div>

<div id="abstract-workshop-9">
<p>
Many compiled languages include a 'type checker' as part of their compilation process which applies automated checks to source code to rule out potential runtime errors due to mismatches in the format of data ('type errors'). The Python language does not include such a check: its types are 'dynamic', with type errors occurring only if encountered at runtime. Python however supports type annotations (since Python 3.0) which allows a programmer to insert optional type information into code which external tools can then use to type check a program. This session will teach how to use Python types alongside the mypy tool for ruling out program bugs and better documenting source code. We will also talk about some fundamental concepts in typing and program verification.
</p>
</div>


<div id="abstract-workshop-10">
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

<div id="abstract-workshop-11">
<p>
A key focus of many scientific computing domains at present is how to use machine learning to enhance and accelerate traditional simulations. Climate science is no exception, with this topic being part of all VESRI projects. To achieve coupling between ML and numerical models presents a number of technical and scientific challenges, however.

[FTorch](https://github.com/Cambridge-ICCS/FTorch) is a library developed by ICCS to couple PyTorch-based machine learning models to Fortran code with the aim of reducing the burden on scientific researchers. It has already been used in DataWave and M2LInES projects and further afield. In this workshop we will introduce FTorch and review its capabilities before taking participants through the process of coupling a PyTorch model into a Fortran code bin a practical demonstration.

There may also be time for questions/discussion from those seeking to use FTorch in their work, and the developers will be available for code-clinics and discussions throughout the week.

Further information can be found in [this video](https://www.youtube.com/watch?v=-NJGuV6Rz6U) or [this video](https://www.youtube.com/watch?v=Ei6H_BoQ7g4&list=PL27mQJy8eDHmibt_aL3M68x-4gnXpxvZP&index=33).
</p></div>

<div id="abstract-workshop-12">
<p>
Have you ever found yourself in a position where your code feels slow but you can't quite put your finger on it.

* is it the new system your running on?
* the new dependencies installed by your system admin?
* or that new awesome feature you pushed to main branch last week without tests 😳 ?

Climate software is necessarily complex, often containing thousands of source files and millions of lines of code. These projects are often developed collaboratively by a large number of scientists over a significant number of years. It is no longer possible to know every line of code, every function and every source file. We can no longer "just guess" where performance is being lost. This is where profiling comes in. In this tutorial we will cover the basics of profiling -- what it is, what its used for and how to understand the output. These basics will be reinforced with demonstrations of two high performance profilers: score-p and TAU.
</p>
</div>

<div id="abstract-workshop-13">
<p>
This introductory tutorial provides a comprehensive overview of the core features and capabilities of the Julia programming language, designed for participants with a foundational understanding of programming concepts.
We begin with an introduction to Julia and the interactive Pluto Notebook environment, followed by an exploration of functions, primary and composite data types, and generic programming through multiple dispatch.
The second half of the tutorial delves into applications of Julia in scientific computing and machine learning. We will provide a hands-on lab that uses Julia to build a dynamical system using time-stepping methods and physics-informed neural networks.
</p>
</div>
</section>

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
    workshop.addEventListener("click",
      function () {
          let abstract = document.getElementById("info-abstract-"+workshop.getAttribute("name"));
          let layer = document.getElementById("layer");
          if (abstract) {
              // null
          } else {
              //label.style.borderStyle = "inset";
              // create abstract box
              let abstractInfo = document.getElementById("abstract-"+workshop.getAttribute("name")).innerHTML;
              let abstract = document.createElement("p");
              abstract.id = "info-abstract-"+workshop.getAttribute("name");
              abstract.className = "abstract";
              abstract.innerHTML = "<b>" + workshop.innerHTML + "</b><br />" + abstractInfo;
              layer.style.display = "block";
              // add to the page
              insertAfter(abstract, workshop);
              // close
              let label = document.createElement("span");
              label.innerHTML = "Close"
              label.className = "showButton";
              label.style.borderStyle = "outset";
              abstract.appendChild(label);
              label.addEventListener("click",
                function() {
                  abstract.parentElement.removeChild(abstract);
                  layer.style.display = "none";
                })
          }
        });
  }
}
addAbstractClicker();

function highlightTitles(color) {
  var workshopTitles = document.getElementsByClassName("workshop");
  for (let i = 0; i < workshopTitles.length; i++) {
     let workshop = workshopTitles[i];
     workshop.style.background = color;
  }
}
</script>
