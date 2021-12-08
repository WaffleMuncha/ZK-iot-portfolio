var pieChartCanvas2 = document.getElementById('Device-Load');
var pieData = {
    labels:['CPU Use','Unused'],
    datasets:
    [{
        data: [0, 100],
        borderWidth: 1,
        borderAlign: 'outer',
        backgroundColor: [
            'rgba(251, 86, 7, 1)',
            'rgba(255, 0, 110, 1)',],
        borderColor:[
            'rgba(255, 190, 11, 1)',
            'rgba(131, 56, 236, 1)',],
    }]
};

var pieOptions = {};

var myPieChart = new Chart(pieChartCanvas2, {
    type: 'pie',
    data: pieData,
    option: pieOptions,
});
var counter = 0;
var pieUpdate = function () {

   let url = "http://127.0.0.1:5000/api/cpu-load"
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
           var newIdle = 100 - newCPU
           myPieChart.data.datasets[0].data = [newCPU, newIdle]
           myPieChart.update()

       }
       counter = counter + 1
    }

setInterval(pieUpdate, 2000)