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
}
.abstract {
    margin: 10px;
    padding: 10px;
    text-align: justify;
    width: 50vw;
    background: #eee;
    pointer: cursor;
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

[Location of MR2 is in the 'core' part of the Centre for Mathematical Sciences, downstairs](http://www.cms.cam.ac.uk/meeting-rooms)

|  Start | End  | Track 1  | Track 2 |
| ------ | ----- | ------- | ------- |
| 14:00  | 15:00 | Introduction to Git and GitHub | Intermediate Git and GitHub |
| 15:00  | 15:30 | <span class='social'>Coffee & Tea</span> |
| 15:30  | 17:00 | <td colspan=2> Scientific Visualisation </td> |

Aromi Pizza and beer from 17:30; board games + Lego

## Thursday 11th July, Centre for Mathematical Sciences

|  Start | End  | Track 1   | Track 2 |
| ------ | ----- | ------- |
| 08:30  | 09:00 | span class='social'>Coffee, tea, and fruit</span> |
| 09:00  | 10:30 | Introduction to climate and weather modelling | Explainable data science with the Fluid language |
| 10:30  | 11:00 | <span class='social'>Break - tea, coffee, pastries</span> |
| 11:00  | 12:00 | Intorduction to climate and weather modelling | What can abstract mathematics tell us about programming climate models? |
| 12:00  | 13:30 | <span class='social'>Lunch - Church College</span> |
| 13:30  | 15:00 | OpenMP for GPUs | Research Sofware Engineering with Python |
| 15:00  | 15:30 | <span class='social'>Break - tea, coffee</span> |
| 15:30  | 17:00 | OpenMP for GPUS (lab) | Typing Python with mypy |

Pre-dinner drinks reception and dinner at Madingley Hall.
Transposrt from CMS will depart at 17:15.

## Friday 12th July, CMS

|  Start | End  | Track 1   | Track 2 |
| ------ | ----- | ------- |
| 08:30  | 09:00 | <span class='social'>Coffee, tea, and fruit</span> |
| 09:00  | 10:30 | Introduction to Neural Networks with PyTorch | Coupling PyTorch with Fortran via FTorch
| 10:30  | 11:00 | <span class='social'>Break - tea, coffee, pastries</span> |
| 11:00  | 12:00 | Introduction to Neural Networks with PyTorch | Code clinic |
| 12:00  | 13:30 | <span class='social'>Lunch - Church College</span> |
| 13:30  | 15:00 | Profiling and performacne | Introduction to Comptuational Science in Julia |
| 15:00  | 15:30 | <span class='social'>Break - tea, coffee</span> |
| 15:30  | 16:00 | Proifiling and performance testing (lab) | Introduction to Comptuational Science in Jula (lab) |
| 16:00 | 17:00 | <b>Closing Keynote</b> - Evelina Gabasova


Cambridge Wine Merchants and cheese and wine tasting session - 15 min short intro to wines and then wines and nibbles

<script>
      //
	function insertAfter(newNode, existingNode) {
    existingNode.parentNode.insertBefore(newNode, existingNode.nextSibling);
}
      var abstracts = document.getElementsByClassName("abstract");
      for (let i=0; i<abstracts.length; i++){
	  let p = document.createElement("p");
	  p.innerHTML = abstracts[i].innerHTML;
	  insertAfter(p,abstracts[i]);
	  abstracts[i].style.display = "none";
	  p.style.display = "none";
	  let showButton = document.createElement("span");
	  showButton.innerHTML = "(abstract)";
	  showButton.addEventListener("click", function() {
	      if (p.style.display == "none") {
		  showButton.innerHTML = "(hide)";
		  p.style.display = "";
	      } else {
 		  showButton.innerHTML = "(abstract)";
		  p.style.display = "none";
              }
	  });
	  showButton.className = "showButton";
	  abstracts[i].parentNode.insertBefore(showButton, abstracts[i]);
      }

function getQueryVariable(variable)
{
  var query = window.location.search.substring(1);
  var vars = query.split("&");
  for (var i=0;i<vars.length;i++)
  {
    var pair = vars[i].split("=");
    if (pair[0] == variable)
    {
      return pair[1];
    }
  }
  return -1; //not found
  }

function showSessionChairs() {
var chairs = document.getElementsByClassName("chairs");
for (let i = 0; i < chairs.length; i++){
   chairs[i].innerHTML = "Chair: " + chairs[i].innerHTML;
	chairs[i].style.display = "block";
	}
	}


if (getQueryVariable("chairs") == "true"){
showSessionChairs();
}
</script>

<a onClick="showSessionChairs();">Show session chairs</a>
