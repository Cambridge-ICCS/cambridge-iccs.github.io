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
    width: 60vw;
    top: 20vh;
    max-height: 60vh;
    left: 25vw;
    background: #eee;
    position: fixed;
    z-index: 10;
    overflow: scroll;

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
.pre-reqs {
  background: #e1e5e0;
}
</style>

<style>
div {
  font-size:12.5pt;
  text-align:justify;
}
</style>

<div id="layer"></div>

# Other information

* [Logistics and Accommodation](https://cambridge-iccs.github.io/summerschool24-logistics)

# Schedule

During the week, you can [book in a session with one of the RSE team](https://docs.google.com/spreadsheets/d/1iINWYEOdEytngnanVqyq2gAi8DJq4kMusvY6_BI3N0A/edit?usp=sharing) for advice, or to discuss ongoing projects.

<b class="workshop" onMouseOver="highlightTitles('rgb(250, 242, 92)')" onMouseOut="highlightTitles('rgb(255,255,255)')">Click a title to see its abstract
and <u>suggested pre-requisites</u> for each session.</b>

## Wednesday 10th July, Centre for Mathematical Sciences

|  Start | End  | Track 1  | Track 2 |
| ------ | ----- | ------- | ------- |
| 14:00  | 14:15 | Introduction - Please be seated by 2pm sharp |
| 14:15  | 15:45 | <a class="workshop" name="workshop-1">Introduction to Git and GitHub</a> | <a class="workshop" name="workshop-2">Intermediate Git and GitHub</a> |
| 15:45  | 16:15 | Coffee & Tea |
| 16:15  | 17:45 | <a class="workshop" name="workshop-3">Scientific Visualisation</a> | Code clinic

Aromi Pizza and beer from 17:45; board games + Lego

## Thursday 11th July, Centre for Mathematical Sciences

Optional running excursion in the morning:

* 07:00-07:30 - scenic 4k led by Jack Atkinson
* 07:00-07:30 - scenic but longer and slightly faster 5k led by Dominic Orchard

Both starting and leaving from the [Faulkes Gatehouse](https://www.google.com/maps/place/52%C2%B012'35.6%22N+0%C2%B006'11.7%22E/@52.2100265,0.1027237,19z/data=!4m12!1m7!3m6!1s0x47d870b5d418f2d9:0xbadd58d1d3b75cfa!2sDepartment+of+Applied+Mathematics+and+Theoretical+Physics,+University+of+Cambridge!8m2!3d52.2103076!4d0.1010554!16s%2Fg%2F11b5zwtgs1!3m3!8m2!3d52.209875!4d0.103257?entry=ttu) at the CMS.

|  Start | End  | Track 1   | Track 2 |
| ------ | ----- | ------- |
| 08:15  | 09:00 | Continental breakfast at the CMS |
| 09:00  | 10:30 | <a class="workshop" name="workshop-10">Introduction to Neural Networks with PyTorch</a> | <a class="workshop" name="workshop-11">Coupling PyTorch with Fortran via FTorch</a>
| 10:30  | 11:00 | Break - tea, coffee, pastries |
| 11:00  | 12:00 | <a class="workshop" name="workshop-10">Introduction to Neural Networks with PyTorch</a> | Code clinic |
| 12:00  | 13:30 | Lunch - Churchill College |
| 13:30  | 15:00 | <a class="workshop" name="workshop-7">OpenMP for GPUs</a> | <a class="workshop" name="workshop-8">Research Sofware Engineering with Python</a> |
| 15:00  | 15:30 | Break - tea, coffee |
| 15:30  | 17:00 | <a class="workshop" name="workshop-7">OpenMP for GPUs (lab)</a> | <a class="workshop" name="workshop-9">Typing Python with mypy</a> |

Dinner at [Madingley Hall](https://maps.app.goo.gl/TQS7L9brtSCKwHAaA), Madingley, Cambridge CB23 8AQ.
Transport from CMS will depart at 17:15.

## Friday 12th July, CMS

|  Start | End  | Track 1   | Track 2 |
| ------ | ----- | ------- |
| 08:15  | 09:00 | Continental breakfast at the CMS |
| 09:00  | 10:30 | <a class="workshop" name="workshop-4">Introduction to climate and weather modelling</a> | <a class="workshop" name="workshop-5">Explainable data science with the Fluid language</a> |
| 10:30  | 11:00 | Break - tea, coffee, pastries |
| 11:00  | 12:00 | <a class="workshop" name="workshop-4">Introduction to climate and weather modelling</a> | <a class="workshop" name="workshop-6">What can abstract mathematics tell us about programming climate models?</a> |
| 12:00  | 13:30 | Lunch - Churchill College |
| 13:30  | 15:30 | <a class="workshop" name="workshop-12">Profiling and performance testing</a> | <a class="workshop" name="workshop-13">Introduction to Computational Science in Julia</a> |
| 15:30  | 16:00 | Break - tea, coffee |
| 16:00 | 17:00 | <b>Closing Keynote</b> - Dr Evelina Gabasova - <a class="workshop" name="workshop-14">Transformational power of openness: open source in research and beyond</a>


Cambridge Wine Merchants and cheese and wine tasting session - 15 min short intro to wines and then wines and nibbles

* [Full Program](https://iccs.cam.ac.uk/files/2024_iccs_summer_school_program.pdf)

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
<p class="pre-reqs">
<b>Pre-requisites:</b> Install git on your computer, set up a Github account and the SSH key and MFA.<br />
You can follow the steps from here: <a href="https://swcarpentry.github.io/git-novice/">https://swcarpentry.github.io/git-novice/</a> as well as <a href="https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account">https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account</a>.
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
<p class="pre-reqs">
<b>Pre-requisites:</b> Attendees will need to have Git installed on their computers, have GitHub accounts, and have SSH keys and MFA set up.<br /><br />
We are assuming that attendees are familiar with Git commands `git add`, `git commit`, `git pull`, `git push`, and `git log`, and the GitHub concepts of Issues and Pull Requests.
<br /><br />
The repository used for the exercises will include some simple Python code but understanding Python is not a requirement. However, attendees will need to have working Python 3 installations on their computers.
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

<p class='pre-reqs'>
<b>Pre-requisites:</b>
The data required for the practical session is here:
<p>
Denvil-Sommer, A. (2024). Dataset for OSSE exercise at ICCS Summer School 2024 Cambridge [Data set]. Zenodo. <a href="https://doi.org/10.5281/zenodo.12567970">https://doi.org/10.5281/zenodo.12567970</a>
</p>
You may wish to look at the article:
<p>
Denvil-Sommer, A., Gehlen, M., and Vrac, M.: Observation system simulation experiments in the Atlantic Ocean for enhanced surface ocean pCO2 reconstructions, Ocean Sci., 17, 1011–1030, <a href="https://doi.org/10.5194/os-17-1011-2021">https://doi.org/10.5194/os-17-1011-2021</a>, 2021.
</p>
Students will need following libraries installed on their laptops:<ul>
<li>numpy</li>
<li>pandas</li>
<li>matplotlib.pyplot</li>
<li>cartopy</li>
<li>torch</li>
<li>sklearn</li>
</ul>
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
To make the best use of today's massively parallel and heterogeneous (both CPU and GPU) computing resources we need to use several programming models. OpenMP is an open specification for a directive based programming model that can take advantage of all the cores on a processor and offload computations to GPUs making only minimal changes to the C, C++ or Fortran source code.
</p>
<p>
This session will serve as an introduction to the OpenMP programming model for GPU acceleration. You will learn how to introduce the directives into your code, and put this into practice using OpenMP to speed up example programs.
</p>
<p class="pre-reqs">
<b>Pre-requisites:</b>
<ul>
<li>As we will be running the practical exercises on the Cambridge HPC system, basic linux shell knowledge is expected.</li>

<li>Expect basis programming skills and the ability to read C or Fortran-style code, and the ability to compile and run code on systems using Makefiles.</li>

<li>Some familiarity with GPU programming is beneficial but not essential</li>
</ul>
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
<p class="pre-reqs">
<b>Pre-requisites:</b>
For the RSE Skills we require participants to:
<ul>
<li>Have a working Python 3 installation on their system.</li>
<li>Ideally clone the workshop repository in advance of the session: <a href="https://github.com/Cambridge-ICCS/rse-skills-python">https://github.com/Cambridge-ICCS/rse-skills-python</a></li>
<li>
We expect basic programming skills, the ability to read and follow python code, and an enthusiasm to learn better practice - it is worth emphasising that many of the concepts will map across to other languages besides python.
</li>
</ul>
</p>
</div>

<div id="abstract-workshop-9">
<p>
Many compiled languages include a 'type checker' as part of their compilation process which applies automated checks to source code to rule out potential runtime errors due to mismatches in the format of data ('type errors'). The Python language does not include such a check: its types are 'dynamic', with type errors occurring only if encountered at runtime. Python however supports type annotations (since Python 3.0) which allows a programmer to insert optional type information into code which external tools can then use to type check a program. This session will teach how to use Python types alongside the mypy tool for ruling out program bugs and better documenting source code. We will also talk about some fundamental concepts in typing and program verification.
<p class='pre-reqs'>
<b>Pre-requisites</b><br/>
Python 3 and <a href="https://mypy.readthedocs.io/en/stable/getting_started.html#installing-and-running-mypy">mypy</a> should be installed before the session.
</p>
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
<p class='pre-reqs'>
<b>Pre-requisites</b>:
Participants will have the choice of executing the material on Colab or locally on their own system. The latter will require familiarity with virtual environments and code deployment.<br /><br />

<i><u>Mathematics and Machine Learning</u></i>
We will not focus on the mathematics of ML too heavily but we expect some familiarty with calculus (differentiating a function), matrix algebra (matrix multiplication and representing data as a matrix) and the concept of regression (fitting a function to data)<br /><br />

<i><u>Neural Networks</u></i><br />
High level concepts can be obtained by watching the the [video series by 3Blue1Brown](https://www.3blue1brown.com/topics/neural-networks), at least chapters 1-3.<br /><br />

<i><u>Python</u></i>
The course will be taught in python using pyTorch. Whilst no prior knowledge of pyTorch is expected we assume users are familiar with the basics of Python3 which includes:

- Basic mathematical operations
- Writing and using functions
The concept of <a href="https://eli5.gg/Object-oriented%20programming">object orientation</a>
i.e. that an object, e.g. a dataset, can have associated functions/methods associated with it.

Basic use of the following libraries:
- <a href="https://numpy.org/">numpy</a> for mathematical and array operations
- <a href="https://matplotlib.org">matplotlib</a> for ploting and visualisation
- <a href="https://pandas.pydata.org/docs/getting_started/index.html">pandas</a> for storing and accessing tabular data
- Familiarity with the <a href="https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/index.html">concept of a jupyter notebook</a>.
</p>
</div>

<div id="abstract-workshop-11">
<p>
A key focus of many scientific computing domains at present is how to use machine learning to enhance and accelerate traditional simulations. Climate science is no exception, with this topic being part of all VESRI projects. To achieve coupling between ML and numerical models presents a number of technical and scientific challenges, however.

<a href="https://github.com/Cambridge-ICCS/FTorch">FTorch</a> is a library developed by ICCS to couple PyTorch-based machine learning models to Fortran code with the aim of reducing the burden on scientific researchers. It has already been used in DataWave and M2LInES projects and further afield. In this workshop we will introduce FTorch and review its capabilities before taking participants through the process of coupling a PyTorch model into a Fortran code bin a practical demonstration.

There may also be time for questions/discussion from those seeking to use FTorch in their work, and the developers will be available for code-clinics and discussions throughout the week.

Further information can be found in <a href="https://www.youtube.com/watch?v=-NJGuV6Rz6U">this video</a> or <a href="https://www.youtube.com/watch?v=Ei6H_BoQ7g4&list=PL27mQJy8eDHmibt_aL3M68x-4gnXpxvZP&index=33">this video</a>.
</p>
<p class="pre-reqs">
<b>Pre-requisites:</b>

<ul>
<li> A python installation. Preferably with pytorch pip installed in advance</li>
<li> Compilers (the gnu suite would be ideal)
 <ul>
  <li>A Fortran Compiler</li>
  <li>A C compiler</li>
  <li>A C++ compiler</li>
  </ul>
  </li>
<li>Internet access</li>
<li>Windows users are encouraged to use Windows Subsystem for Linux, or review the Windows guidance on the FTorch documentation in advance.</li>
</ul>
</p>
</div>

<div id="abstract-workshop-12">
<p>
Have you ever found yourself in a position where your code feels slow but you can't quite put your finger on it.

<ul>
<li>is it the new system your running on?</li>
<li>the new dependencies installed by your system admin?</li>
<li>or that new awesome feature you pushed to main branch last week without tests 😳 ?</li>
</ul>

Climate software is necessarily complex, often containing thousands of source files and millions of lines of code. These projects are often developed collaboratively by a large number of scientists over a significant number of years. It is no longer possible to know every line of code, every function and every source file. We can no longer "just guess" where performance is being lost. This is where profiling comes in. In this tutorial we will cover the basics of profiling -- what it is, what its used for and how to understand the output. These basics will be reinforced with demonstrations of two high performance profilers: score-p and TAU.
<p class="pre-reqs">
<b>Pre-requisites:</b>

<ul>
<li>Bring a code that you would like to profile (we can provide example code but it's always better to use your own)</li>

<li>No need to install any profilers or tools prior to the workshop</li>

<li>Access to a Unix machine would be ideal (if using Windows, please install Windows Subsystem for Linux WSL)</li>

<li>Optional - score-p/cube, valgrind, clang/gnu compiler, tau profiler, python</li>
</ul>

</p>
</p>

</div>

<div id="abstract-workshop-13">
<p>
This introductory tutorial provides a comprehensive overview of the core features and capabilities of the Julia programming language, designed for participants with a foundational understanding of programming concepts.
We begin with an introduction to Julia and the interactive Pluto Notebook environment, followed by an exploration of functions, primary and composite data types, generic programming through multiple dispatch, and more.
Afterwards, the tutorial provides several study cases to delve into applications of Julia in scientific computing and machine learning. The last part will be a hands-on lab to build an Earth energy balance model and train a neural network to solve its differential equation.
</p>
<p class="pre-reqs">
<b>Pre-requisites:</b>

<ul>
<li> Basic experience in programming </li>
<li> A Julia installation with Pluto.jl. <b>Please following the <a href="https://github.com/Cambridge-ICCS/Summer-school-Julia-tutorial">setup instructios on the material for this session</a></b></li>
<li>Some knowledge in calculus and linear algebra would be desirable</li>
</ul>
</p>
</div>

<div id="abstract-workshop-14">
Building software tools has become a fundamental aspect of many areas of current research, from environmental modelling to digital humanities. Evelina will talk about how the potential of these tools can be amplified through the principles of open source and open science. Looking at successful and not so successful examples, we will explore the current landscape of open source in academia and research in general: from building collaborative communities to the current struggles to define what open source even means in the world of large language models. On top of that, we will cover some of the best practices for creating robust, reusable and openly accessible tools to maximise the impact of our research work.
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
