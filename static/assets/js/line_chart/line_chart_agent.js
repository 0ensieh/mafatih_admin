let ctx = document.getElementById("chartLine").getContext("2d");
let myChart = new Chart(ctx, {
  type: "line",
  data: {
    // labels: ["Sun", "Mon", "Tus", "Wed", "Thu", "Fri", "Sat"],
    labels: label,
    datasets: [
     {
      label: "avg 1 min",
      // data: [250, 420, 210, 420, 210, 320, 350],
      data: avg_1min,
      backgroundColor: "transparent",
      borderColor: "rgba(50,251,5,0.66)",
      borderWidth: 2,
      pointBackgroundColor: "#ffffff",
      pointRadius: 4
    },
    {
      label: "avg 5 min",
      data: avg_5min,
      backgroundColor: "transparent",
      borderColor: "rgba(5,195,251,0.63)",
      borderWidth: 2,
      pointBackgroundColor: "#ffffff",
      pointRadius: 4
    },
    {
      label: "avg 15 min",
      data: avg_15min,
      backgroundColor: "transparent",
      borderColor: "rgba(251,5,5,0.71)",
      borderWidth: 2,
      pointBackgroundColor: "#ffffff",
      pointRadius: 4
    },]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    scales: {
      xAxes: [{
        ticks: {
          fontColor: "#9ba6b5"
        },
        display: true,
        gridLines: {
          color: "rgba(119, 119, 142, 0.2)"
        }
      }],
      yAxes: [{
        ticks: {
          fontColor: "#9ba6b5"
        },
        display: true,
        gridLines: {
          color: "rgba(119, 119, 142, 0.2)"
        },
        scaleLabel: {
          display: false,
          labelString: "Thousands",
          fontColor: "rgba(119, 119, 142, 0.2)"
        }
      }]
    },
    legend: {
      labels: {
        fontColor: "#9ba6b5"
      }
    },
//    annotation: {
//      annotations: [{
//        type: 'line',
//        mode: 'horizontal',
//        scaleID: 'y-axis-0',
//        value: 1.2,
//        borderColor: 'red',
//        borderWidth: 2,
//        label: {
//          enabled: true,
//          content: 'Horizontal Line'
//        }
//      }]
//    }
  }
});