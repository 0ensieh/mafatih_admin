/* Pie Chart*/
var datapie = {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    datasets: [{
        data: [20, 20, 30, 5, 25],
        backgroundColor: ['#6c5ffc', '#05c3fb', '#09ad95', '#1170e4', '#e82646']
    }]
};
var optionpie = {
    maintainAspectRatio: false,
    responsive: true,
    legend: {
        display: true,
    },
    animation: {
        animateScale: true,
        animateRotate: true
    }
};

var ctx7 = document.getElementById('chartPie');
var myPieChart7 = new Chart(ctx7, {
    type: 'pie',
    data: datapie,
    options: optionpie
});