// --> CREATE SVG DRAWING AREA

var margin = {top: 30, right: 20, bottom: 150, left: 150};

var width = 900 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom;

var svg_ohio_graph = d3.select("#ohiograph").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .attr("class", "svg_class")
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Time parser format
var parseDate = d3.time.format("%Y-%m-%d").parse;

//Scale functions
var x = d3.time.scale()
    .range([0, width]);

var y = d3.scale.linear()
    .range([height, 0]);

// Color scale
var color = d3.scale.category10();

//Axes
var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
    .ticks(12)
    .tickFormat(d3.time.format('%d %b'));

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

// Line
var line = d3.svg.line()
    .interpolate("basis")
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.mentions); });

// Load the data
d3.csv("data/ohiomentions2.csv", function(data) {
    data.forEach(function(d) {
        d.date = parseDate(d.date);
        d.mentions = +d.mentions;
    });

    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.mentions; })]);

    // Nest the entries by symbol
    var dataNest = d3.nest()
        .key(function(d) {return d.candidate;})
        .entries(data);

    console.log(dataNest);

    // add legend spacing
    var legendSpace = width/dataNest.length;

    // Loop through each symbol / key
    dataNest.forEach(function(d, i) {

        svg_ohio_graph.append("path")
            .attr("class", "line")
            .style("stroke", function() {
                return d.color = color(d.key);
            })
            // add id for each line
            .attr("id", 'tag'+ d.key.replace(/\s+/g, ''))
            .attr("d", line(d.values));

        // add the legend
        svg_ohio_graph.append("text")
            .attr("x", (legendSpace/2) + i*legendSpace)
            .attr("y", height + (margin.bottom/2) + 30)
            .attr("class", "legend")
            .style("fill", function() {
                return d.color = color(d.key);
            })
            // add interactivity
            .on("click", function() {
                // Determine if current line is visible
                var active = d.active ? false : true;
                var newOpacity = active ? 0 : 1;
                // Hide or show depending on ID
                d3.select('#tag' + d.key.replace(/\s+/g, ''))
                    .transition(500)
                    .duration(500)
                    .style("opacity", newOpacity);
                // update whether the elt is active or not
                d.active = active;
            })
            .text(d.key);

    });

    // Add the X Axis
    svg_ohio_graph.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);
        //.selectAll("text")
        //.attr("y", 0)
        //.attr("x", 9)
        //.attr("dy", ".35em")
        //.attr("transform", "rotate(90)")
        //.style("text-anchor", "start");

    // Add the Y Axis
    svg_ohio_graph.append("g")
        .attr("class", "y axis")
        .call(yAxis);

    // create x label for time axis
    svg_ohio_graph.append("text")
        .attr("x", (width/2))
        .attr("y", height + 60)
        .attr("class", "x-axis-label")
        .text("Time");

    // create y label for mentions axis
    svg_ohio_graph.append("text")
        .attr("x", -350)
        .attr("y", -60)
        .text("Number of mentions on Twitter, per day")
        .attr("class", "y-axis-label")
        .attr("transform", "rotate(-90)")
        .attr("fill", "black");

});