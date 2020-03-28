let totalCEdata = []
let totalLUdata = []
let totalCOCdata = []

queue()
    .defer(d3.csv,"data/totalCE.csv")
    .defer(d3.csv,"data/totalLU.csv")
    .defer(d3.csv,"data/totalCOC.csv")
    .await(analyze);



function analyze(error, totalCE, totalLU, totalCOC) {
  if(error) { console.log(error); }
  totalCEdata = totalCE;
  totalLUdata = totalLU
  totalCOCdata = totalCOC
  createVis();
}

function createVis() {
    var vis = this;
    vis.pie = new WaffleChart("waffle-chart", totalLUdata);
    vis.pie = new PieChart("time-pie-chart", totalCEdata);
    vis.pie = new PieChart("time-pie-chart2", totalCOCdata);
 
}