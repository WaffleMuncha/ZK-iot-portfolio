var ctx = document.getElementById('Humidity-Bar')
var humChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Humidity'],
        datasets: [{
            data: [0],
            label: '%',
            backgroundColor: [
                'rgba(255, 190, 11, 1)',
                'rgba(58, 134, 255, 1)',

            ],
            borderColor: [
                'rgba(251, 86, 7, 1)',
                'rgba(255, 0, 110, 1)',

            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
var chartUpdate = function () {
    let url = "http://127.0.0.1:5000/api/current-humidity"
    let method = "GET"
    let typeOfResponse = "json"

    let xhr = new XMLHttpRequest()
    xhr.open(method, url)
    xhr.responseType = typeOfResponse
    xhr.send()

    xhr.onload = function () {
        let responseObj = xhr.response
        var newCPU = parseFloat(responseObj)
        if (newCPU > 100) {
            newCPU = 100
        } else {
            if (newCPU < 0) {
                newCPU = 0
            }
        }
        var newIdle = 100 - newCPU
        humChart.data.datasets[0].data = [newCPU]
        humChart.update()
    }
};
chartUpdate();