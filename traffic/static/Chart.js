// Create a new Chart.js line chart
var ctx = document.getElementById('chartContainer').getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'Vehicle Count',
            data: vehicleCounts,
            fill: True,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});
