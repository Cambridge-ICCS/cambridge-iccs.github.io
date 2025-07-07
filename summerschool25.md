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

<h3><a href="summerschool25-programme.htm">Full programme</a></h3>

<h3><a href="https://cambridge-iccs.github.io/summerschool25-prerequisites">Collected list of pre-requisities</a></h3>

<br />

During the week, you can <a href="https://docs.google.com/spreadsheets/d/1v8y2GodI9JZoHrFRpLW2tD135MurDBMIcr-ArBFIT3A/edit">book in a session</a> with one of the RSE team for advice, or to discuss ongoing projects.

## List of Topics in brief

* **Version control (Git and GitHub)** – both introductory and intermediate sessions
* **RSE Skills** – how to apply research software engineering principles to write higher-quality code, reduce bugs, and facilitate re-use
* **Debugging** – leveraging debugging tools for effectively understanding program behaviour and diagnosing problems
* **AI for Software Engineering** – leveraging generative AI tools effectively for software engineering
* **Differentiable programming** – foundations of working with automatic differentiation and deploying in code
* **Introduction to High Performance Computing** – hardware, performance limits, programming models, profiling, debugging
* **Practical Machine Learning with PyTorch** – understanding the structure of a PyTorch model, ML pipeline for classification/regression
* **Observation System Simulation Experiences** – using ML for optimal sampling strategy
* **Introduction to Julia** – a brief introduction to the Julia language for computational science
* **Explainable data science with Fluid** – building transparent, interactive data science visualisations using the Fluid language
* **FTorch** – coupling ML and numerical models in Fortran with FTorch
* **Testing and correctness** – deploying unit tests, regression tests, property-based tests
* **Random Forests and Decision Trees** – how and when to use these ensemble methods

### Hackathon

As in previous years, we will be running a hackathon at the summer school on the Friday. The idea of a hackathon is to spend focussed time working on a mini-project for a day in a small group (e.g., 3-6 people). Projects are proposed by participants and can be based on something you are currently working on, or an idea that could be reasonably tackled in a day (at least to make some progress). This is a fantastic opportunity to learn from each other ‘by doing’, forge new connections, and even make progress on a project. As part of the registration, you will be asked for your GitHub login. We will add everyone to [the Summer School hackathon repository](https://github.com/Cambridge-ICCS/hackathon-2025) in which people can propose topics ahead of time by posting an issue, enabling discussion and forming groups by responding to the issue. We will have a short session to discuss the summer school arrangements, but our hope is that there will be a sufficient number of projects submitted ahead of time to enable groups to be formed by the Friday. We will send out a reminder to submit project ideas ahead of the summer school.

### Code of Conduct

The open exchange of ideas and the freedom of thought and expression are central to the aims and goals of the
summer school; these require an environment that recognizes the inherent worth of every person and group, that
fosters dignity, understanding, and mutual respect, and that embraces diversity. We are dedicated to providing a
safe, hospitable, productive, and harassment-free and discrimination-free environment for everyone attending,
regardless of ethnicity, religion, disability, physical appearance, gender, or sexual orientation. In particular, we
expect all the participants to use welcoming and inclusive language, to be respectful of differing viewpoints and
experiences, to gracefully accept constructive criticism, to focus on what is best for the community, and to show
empathy towards other community members. We expect everyone to communicate openly with respect and
consideration for others, treating each other as equals. It is important to remember that a community where people
feel uncomfortable or threatened is neither healthy nor productive.

There is no tolerance for unwelcome, hostile, or disruptive behaviour or speech that intimidates, creates discomfort,
or interferes with a person’s participation or opportunity for participation at the event. Participants asked to stop
any harassing behaviour are expected to comply immediately. Participants violating these standards may be
expelled from this and future events.

If you witness or are subject to unacceptable behaviour, please talk to one of the ICCS leadership: [Dominic Orchard](mailto:dao29@cam.ac.uk)
or [Marla Fuchs](mailto:mf372@cam.ac.uk).

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
