function f1(){

    'use strict';

    Chart.defaults.global.defaultFontColor = '#75787c';

   var chartOptions = {
        scale: {
            gridLines: {
                color: '#3f4145'
            },
            ticks: {
                beginAtZero: true,
                min: 0,
                max: 100,
                stepSize: 20
            },
            pointLabels: {
                fontSize: 12
            }
        },
        legend: {
            position: 'left'
        }
    };
    var data_chart = jQuery.parseJSON(document.getElementById("data_chart_123").textContent);
    var data_cname1 = document.getElementById("data_cname1").textContent;
    var data_cname2 = document.getElementById("data_cname2").textContent;
    var data_cname3 = document.getElementById("data_cname3").textContent;
    var data_champion1000 = jQuery.parseJSON(document.getElementById("data_champion01").textContent);
    var data_champion2000 = jQuery.parseJSON(document.getElementById("data_champion02").textContent);
    var data_champion3000 = jQuery.parseJSON(document.getElementById("data_champion03").textContent);
    var RADARCHARTEXMPLE1  = $('#radarChartCustom1');
    var radarChartExample1 = new Chart(RADARCHARTEXMPLE1, {
        type: 'radar',
        options: chartOptions,
        data: {
            labels: ["击杀", "输出", "坦度", "助攻", "治疗", "生存"],
            datasets: [
                {
                    label: "个人能力",
                    backgroundColor: "rgba(113, 39, 172, 0.4)",
                    borderWidth: 2,
                    borderColor: "#7127AC",
                    pointBackgroundColor: "#7127AC",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "#7127AC",
                    data: data_chart
                },
            ]
        }
    });

    var radarChartExample1 = {
        responsive: true
    };

    var RADARCHARTEXMPLE2  = $('#radarChartCustom2');
    var radarChartExample2 = new Chart(RADARCHARTEXMPLE2, {
        type: 'radar',
        options: chartOptions,
        data: {
            labels: ["击杀", "输出", "坦度", "助攻", "治疗", "生存"],
            datasets: [
                {
                    label: "个人能力",
                    backgroundColor: "rgba(113, 39, 172, 0.4)",
                    borderWidth: 2,
                    borderColor: "#7127AC",
                    pointBackgroundColor: "#7127AC",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "#7127AC",
                    data: data_chart
                },
                {
                    label: data_cname1,
                    backgroundColor: "rgba(207, 83, 249, 0.4)",
                    borderWidth: 2,
                    borderColor: "#CF53F9",
                    pointBackgroundColor: "#CF53F9",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "#CF53F9",
                    data: data_champion1000
                },

            ]
        }
    });
    var radarChartExample2 = {
        responsive: true
    };

    var RADARCHARTEXMPLE3  = $('#radarChartCustom3');
    var radarChartExample3 = new Chart(RADARCHARTEXMPLE3, {
        type: 'radar',
        options: chartOptions,
        data: {
            labels: ["击杀", "输出", "坦度", "助攻", "治疗", "生存"],
            datasets: [
                {
                    label: "个人能力",
                    backgroundColor: "rgba(113, 39, 172, 0.4)",
                    borderWidth: 2,
                    borderColor: "#7127AC",
                    pointBackgroundColor: "#7127AC",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "#7127AC",
                    data: data_chart
                },
// Light pink, gray blue, yellow green, white, fuchsia, silver gray, black
                {
                    label: data_cname2,
                    backgroundColor: "rgba(86,40,171,0.4)",
                    borderWidth: 2,
                    borderColor: "#5628ab",
                    pointBackgroundColor: "#5628ab",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "#5628ab",
                    data: data_champion2000
                },

            ]
        }
    });
    var radarChartExample3 = {
        responsive: true
    };

    var RADARCHARTEXMPLE4  = $('#radarChartCustom4');
    var radarChartExample4 = new Chart(RADARCHARTEXMPLE4, {
        type: 'radar',
        options: chartOptions,
        data: {
            labels: ["击杀", "输出", "坦度", "助攻", "治疗", "生存"],
            datasets: [
                {
                    label: "个人能力",
                    backgroundColor: "rgba(113, 39, 172, 0.4)",
                    borderWidth: 2,
                    borderColor: "#7127AC",
                    pointBackgroundColor: "#7127AC",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "#7127AC",
                    data: data_chart
                },

                {
                    label: data_cname3,
                    backgroundColor: "rgba(62,39,171,0.4)",
                    borderWidth: 2,
                    borderColor: "#3e27ab",
                    pointBackgroundColor: "#3e27ab",
                    pointBorderColor: "#fff",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "#3e27ab",
                    data:data_champion3000
                },
            ]
        }
    });
    var radarChartExample4 = {
        responsive: true
    };


}