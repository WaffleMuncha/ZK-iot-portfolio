var ctx = document.getElementById('Temperature-Bar')
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Temperature'],
        datasets: [{
            label: 'Celsius',
            data: [12],
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