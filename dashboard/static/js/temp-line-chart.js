var lineChartCanvas = document.getElementById('temp-historic');

var labels = []
var data = {
  labels: labels,
  datasets: [{
    label: 'Temperature Historic Chart',
    data: [0],
    fill: false,
    borderColor: 'rgb(75, 192, 192)',
    tension: 0.1
  }]
};

var options = {
  legend: {display: false},
  title: {
    display: true,
    text: 'temp'
  },
  scales: {
    xAxes: [{
      scaleLabel: {
        display: true,
        labelString: 'Time'
      }
    }],
    yAxes: [{
      scaleLabel: {
        display: true,
        labelString: 'Temp Celsius',
      },
      ticks: {
        beginAtZero: true,
        suggestedMin: 0,
        suggestedMax: 100,
      },
    }],
  },
}



var lineChart = new Chart(lineChartCanvas, {
  type: 'line',
  data: data,
  options: options
  });

var counter = 0;
var pieUpdate = function () {
  var now = new Date();
  var time = now.getHours() + ":" + now.getMinutes() + ":" + now.getSeconds();

  lineChart.data.labels.unshift(time)

   let url = "http://127.0.0.1:5000/api/current-temp"
   let method = "GET"
   let typeOfResponse = "json"

   let xhr = new XMLHttpRequest()
   xhr.open(method, url)
   xhr.responseType = typeOfResponse
   xhr.send()

   xhr.onload = function ()
       {
           let responseObj = xhr.response
           var newCPU = parseFloat(responseObj)
           if (newCPU > 100){
               newCPU = 100
           }
           else {
               if (newCPU < 0) {
                   newCPU = 0
                   }
               }


           lineChart.data.datasets[0].data.unshift(newCPU);
           if (counter > 20) {
             lineChart.data.labels.pop()
             lineChart.data.datasets[0].data.pop()
           }
           lineChart.update();

       }
       counter = counter + 1
    }

setInterval(pieUpdate, 2000)