function makeplot() {
Plotly.d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/candlestick_dataset_2007_2009.csv", function(data){ processData(data) } );
};

function processData(allRows) {

console.log(allRows);
var data_open = [], data_close = [], data_high = [], data_low = [], dates = [];
for (var i=0; i<allRows.length; i++) {
 row = allRows[i];
data_close.push(parseFloat(row['close']));
data_high.push(parseFloat(row['high']));
data_low.push(parseFloat(row['low']));
data_open.push(parseFloat(row['open']));
}
makePlotly( data_open, data_close, data_high, data_low );
}


function makePlotly( data_open, data_close, data_high, data_low ){
var data_dates = getAllDays('2008-10-01', '2008-11-01');

var fig = PlotlyFinance.createCandlestick({
open: data_open,
high: data_high,
low: data_low,
close: data_close,
dates: data_dates
});
Plotly.newPlot('myDiv', fig.data, fig.layout);
};

// Utility Function to generate all days
function getAllDays(start, end) {
 var s = new Date(start);
 var e = new Date(end);
 var a = [];

 while(s < e) {
     a.push(s);
     s = new Date(s.setDate(
         s.getDate() + 1
     ))
 }

 return a;
};

makeplot();
