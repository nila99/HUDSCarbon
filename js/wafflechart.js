/*
 * StackedAreaChart - Object constructor function
 * @param _parentElement    -- the HTML element in which to draw the visualization
 * @param _data                     -- the data
 */


WaffleChart = function(_parentElement, _data, _eventHandler){
    this.parentElement = _parentElement;
    this.data = _data;
    this.eventHandler = _eventHandler;

    this.initVis();
}

WaffleChart.prototype.initVis = function() {
    var vis = this;


    vis.total = 0;
    vis.width;
    vis.height;
    vis.widthSquares = 20;
    vis.heightSquares = 20;
    vis.squareSize = 25;
    vis.squareValue = 0;
    vis.gap = 1;
    vis.color =d3.scaleLinear().domain([1,10])
    .range(["white", "blue"]);



    vis.total = d3.sum(vis.data, function(d) { return d.value; });
    //value of a square
    vis.squareValue = vis.total / (vis.widthSquares*vis.heightSquares);

    vis.data.forEach(function(d, i) 
    {
      d.value = +d.value;
      d.units = Math.floor(d.value/vis.squareValue);
      vis.data = vis.data.concat(
        Array(d.units+1).join(1).split('').map(function()
          {
            return {  squareValue: vis.squareValue,                      
                      units: d.units,
                      value: d.value,
                      groupIndex: i};
          })
        );
       });



    console.log(vis.data);

    vis.width = (vis.squareSize*vis.widthSquares) + vis.widthSquares*vis.gap + 25;
    vis.height = (vis.squareSize*vis.heightSquares) + vis.heightSquares*vis.gap + 25;

    vis.waffle = d3.select('#' + vis.parentElement)
      .append("svg")
      .attr("width", vis.width)
      .attr("height", vis.height)
      .append("g")
      .selectAll("div")
      .data(vis.data)
      .enter()
      .append("rect")
      .attr("width", vis.squareSize)
      .attr("height", vis.squareSize)
      .attr("fill", function(d)
      {
        return vis.color(d.groupIndex);
      })
      .attr("x", function(d, i)
        {
          //group n squares for column
          vis.col = Math.floor(i/vis.heightSquares);
          return (vis.col*vis.squareSize) + (vis.col*vis.gap);
        })
      .attr("y", function(d, i)
      {
        vis.row = i%vis.heightSquares;
        return (vis.heightSquares*vis.squareSize) - ((vis.row*vis.squareSize) + (vis.row*vis.gap))
      })




};



// Bring a D3 element to the front
d3.selection.prototype.moveToFront = function() {
    return this.each(function(){
        this.parentNode.appendChild(this);
    });
};

