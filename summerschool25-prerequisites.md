---
layout:  single
title: Institute of Computing for Climate Science Summer School 2025
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

<h3><a href="summerschool25">← Back to Summer School 2025 page</a></h3><br />

# Pre-requisites list 


## RSE Skills (Monday)

* Have a working Python 3 installation on your system.
* Clone the workshop repository in advance of the session: [https://github.com/jatkinson1000/rse-skills-workshop](https://github.com/jatkinson1000/rse-skills-workshop)
* An expectation of basic programming skills, the ability to read and follow python code, and an enthusiasm to learn better practices - it is worth emphasising that many of the concepts will map across to other languages with pointers provided.

## Explainable data science with Fluid (Monday)

* Basic familiarity with functional programming and data types (lists, dictionaries, etc)

## Introduction to Git and GitHub for beginners (Monday)

* Install git on your computer, set up a Github account and the SSH key and MFA. You can follow the steps from here: [https://swcarpentry.github.io/git-novice/](https://swcarpentry.github.io/git-novice/) as well as [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
 - Detailed setup instructions to prepare before the course can be found [on this page in the course repository](https://github.com/Cambridge-ICCS/Summer-school-Intro-Git/blob/main/PREPARATION.md)
* It would be useful for participants to watch this video from a previous summer school before the course.

## Intermediate Git and GitHub (Monday)

* Have a working Python 3 installation on your system.
* Have Git on your system. Installed by default on Linux and most mac systems, see [https://github.com/git-guides/install-git](https://github.com/git-guides/install-git) for details.
* Basic programming skills, namely the ability to read Python code.
* Familiarity with basic git commands (namely: clone, add, commit, push, pull) is assumed, with a brief recap in the session.

## Introduction to High Performance Computing (Monday, Tuesday)

## AI for Software Engineering (Tuesday)

* Install [Cursor](https://www.cursor.com)

## Differentiable programming (Tuesday, Wednesday)

* Undergraduate level knowledge of linear algebra and calculus.
* Basic knowledge of C or Fortran.
* Either download and install the [Tapenade AD tool](https://tapenade.gitlabpages.inria.fr/tapenade/) or just check you can access the [web interface](http://tapenade.inria.fr:8080/tapenade/index.jsp). 

## Debugging (Tuesday)

* Unix command line
* Experience with a compiled language (C/C++/Fortran or Rust)
* No prior knowledge of debuggers is assumed
* (optional) Experience with MPI programs

## AI for Software Engineering (Tuesday)

- Install [Cursor](https://www.cursor.com)

## Practical Machine Learning with PyTorch (Wednesday, Thursday)

* The materials can be found along with a detailed description of prerequisites [here](https://github.com/Cambridge-ICCS/practical-ml-with-pytorch).
* Important: On the day there will be two options to explore the material. To avoid any setup complications, choose to either:
   - Clone and install the repo locally ahead of time.
   - Be ready with a Google account to use Google Colab.
* To get the most out of the session it would be helpful to review:
   - Python3 (numpy, pandas, matplotlib)
   - Maths (calculus, matrix algebra, regression)
   - Neural networks: See YouTube series by 3blue1brown, chapters 1-3.

## Observation System Simulation Experiences: how to use ML for optimal sampling strategy (Wednesday)

* Have a working Python 3 installation on their system
* Ideally download the data in advance of the session: [https://zenodo.org/records/12567970](https://zenodo.org/records/12567970).
* Ideally clone the repository in advance of the session: [https://github.com/lcimoli/OSSE_pCO2](https://github.com/lcimoli/OSSE_pCO2)

## Introduction to Julia (Wednesday)

* A Julia installation with Pluto.jl. Please following the setup instructions [on the material for this session](https://github.com/Cambridge-ICCS/Summer-School-Julia-Tutorial).
* Basic programming skills

## Testing and correctness (Thursday)

The concepts discussed in this course can be applied to almost any programming language, however we will use Python as a vehicle for specific examples and exercises.
Therefore having at least a basic knowledge of Python will be useful as well as a working Python 3 installation on your system. 
Follow the instructions on the [workshop material GitHub to get setup with the examples](https://github.com/Cambridge-ICCS/testing-workshop/blob/main/example/).

## FTorch (Thursday)

- A GitHub account.
- Some previous experience with PyTorch and machine learning is useful but not essential.
- Previous exposure to Fortran or a similar compiled language is useful but not essential.

## Random Forests and Decision Trees (Thursday)

Undergraduate level knowledge of linear algebra and calculus.
- Have a working Python 3 installation on their system.
- Download and install the scikit-learn library
  
Second session:
- First session strict prerequisite.
- Practical Machine Learning with PyTorch session
