var margin = {top: 20, right: 80, bottom: 30, left: 50},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var parseDate = d3.time.format("%Y-%m-%d").parse;

var x = d3.time.scale()
    .range([0, width]);

var y = d3.scale.linear()
    .range([height, 0]);

var color = d3.scale.category10();

var xAxis = d3.svg.axis()
    .scale(x)
    .ticks(10)
    .tickFormat(d3.time.format("%d %b"))
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

var svg_multi = d3.select("#state").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var select_state = "California";
var select_party = "Republicans";
var Florida_data, NewYork_data, Ohio_data, Wisconsin_data, Nevada_data, California_data;

queue()
    .defer(d3.csv, "data/Florida_Results.csv")
    .defer(d3.csv, "data/NewYork_Results.csv")
    .defer(d3.csv, "data/Ohio_Results.csv")
    .defer(d3.csv, "data/Wisconsin_Results.csv")
    .defer(d3.csv, "data/Nevada_Results.csv")
    .defer(d3.csv, "data/California_Results.csv")
    .await(function(error, Florida, NewYork, Ohio, Wisconsin, Nevada, California) {

        var data_array = [Florida, NewYork, Ohio, Wisconsin, Nevada, California];
        // parse dates
        function changeDates(item) {
            item.forEach(function(d) {
                d.Date = parseDate(d.Date);
            });
        }

        data_array.forEach(changeDates);

        // create the axes
        svg_multi.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis);

        svg_multi.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text("Percentage of political tweets");

        Florida_data = Florida;
        NewYork_data = NewYork;
        Ohio_data = Ohio;
        Wisconsin_data = Wisconsin;
        Nevada_data = Nevada;
        California_data = California;

        // Update visualization when ready
        updateVisualization("Republicans");
    });

var data;

function updateVisualization(party) {
    console.log(party);
    // Get the user-selected state
    select_state = d3.select("#select-box").property("value");
    console.log(select_state);
    // Get appropriate dataset for that state
    switch (select_state) {
        case "Florida":
            data = Florida_data;
            break;
        case "NewYork":
            data = NewYork_data;
            break;
        case "Ohio":
            data = Ohio_data;
            break;
        case "Wisconsin":
            data = Wisconsin_data;
            break;
        case "Nevada":
            data = Nevada_data;
            break;
        case "California":
            data = California_data;
            break;
    }

    // Get the user-selected party
    // select_party = d3.select('input[name="party"]:checked').node().value;
    select_party = party;

    color.domain(d3.keys(data[0]).filter(function(key) {
        if (select_party == "Republicans") {
            return ((key !== "Date") && (key !== "Sanders") && (key !== "Clinton"));
        } else {
            return ((key !== "Date") && (key !== "Cruz") && (key !== "Rubio") && (key !== "Trump") && (key !== "Kasich"));
        }
    }));
    console.log(data);

    data = data.sort(function (a,b) {return d3.ascending(a.Date, b.Date); });

    var people = color.domain().map(function(name) {
        return {
            name: name,
            values: data.map(function(d) {
                return {Date: d.Date, candidate: +d[name]};
            })
        };
    });

    console.log(people);

    // update domains for axes
    x.domain(d3.extent(data, function(d) { return d.Date; }));

    //for use in mentions by absolute numbers
    //y.domain([
    //    d3.min(people, function(c) { return d3.min(c.values, function(v) { return v.candidate; }); }),
    //    d3.max(people, function(c) { return d3.max(c.values, function(v) { return v.candidate; }); })
    //]);

    y.domain([0, 100]);

    // draw axes anew
    svg_multi.select(".y")
        .call(yAxis);
    svg_multi.select(".x")
        .transition()
        .duration(1000)
        .call(xAxis);

    var line = d3.svg.line()
        .interpolate("basis")
        .x(function(d) { return x(d.Date); })
        .y(function(d) { return y(d.candidate); });

    var person = svg_multi.selectAll(".candidate")
        .data(people, function(d) {
            return d.name;
        });

    var personGroups = person.enter()
        .append("g")
        .attr("class", "candidate");

    //person
    //    .enter().append("g")
    //    .attr("class", "candidate");

    personGroups.append("path")
        .attr("class", "line")
        //.attr("d", function(d) { return line(d.values); })
        .style("stroke", function(d) { return color(d.name); });

    personGroups.append("text")
        .attr("x", 3)
        .attr("dy", ".35em");

    var personUpdate = d3.transition(person);

    personUpdate.select("path")
        .transition()
        .duration(1000)
        .attr("d", function(d) {
            return line(d.values);
        });

    person.select("text")
        .datum(function(d) { return {name: d.name, value: d.values[d.values.length - 1]}; })
        .attr("transform", function(d) { return "translate(" + x(d.value.Date) + "," + y(d.value.candidate) + ")"; })
        .text(function(d) { return d.name; });

    person.exit().remove();

}