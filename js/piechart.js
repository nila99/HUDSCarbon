/*
 * StackedAreaChart - Object constructor function
 * @param _parentElement 	-- the HTML element in which to draw the visualization
 * @param _data						-- the data
 */




PieChart = function(_parentElement, _data, _eventHandler){
    this.parentElement = _parentElement;
    this.data = _data;
    this.eventHandler = _eventHandler;

    this.initVis();
}

PieChart.prototype.initVis = function() {
    var vis = this;


    vis.width = 360;
    vis.height = 360;
    vis.radius = Math.min(vis.width, vis.height) / 2;
    vis.donutWidth = 100;
    vis.color = d3.scaleLinear().domain([1,10])
    .range(["white", "blue"]);


    vis.svg = d3.select('#' + vis.parentElement)
		.append('svg')
    	.attr('width', vis.width)
    	.attr('height', vis.height)
    	.append('g')
    	.attr('transform', 'translate(' + (vis.width / 2) + ',' + (vis.height / 2) + ')');
	vis.arc = d3.arc()
    	.innerRadius(vis.radius - vis.donutWidth)
    	.outerRadius(vis.radius);
	vis.pie = d3.pie()
    	.value(function (d) {
        	return d.value;
    	})
    	.sort(null);
	vis.path = vis.svg.selectAll('path')
    	.data(vis.pie(vis.data))
    	.enter()
    	.append('path')
    	.attr('d', vis.arc)
    	.attr('fill', function (d, i) {
        	return vis.color(i);
    	})
    	.attr('transform', 'translate(0, 0)')







};



// Bring a D3 element to the front
d3.selection.prototype.moveToFront = function() {
    return this.each(function(){
        this.parentNode.appendChild(this);
    });
};

