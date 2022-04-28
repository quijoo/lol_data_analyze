 $(document).ready(function () {
    // ------------------------------------------------------- //
    // Pie Chart Custom 1
    // ------------------------------------------------------ //
    var Tname0 = document.getElementById("Tname0").textContent;
    var Tname1 = document.getElementById("Tname1").textContent;
    var Tname2 = document.getElementById("Tname2").textContent;
    var Tname3 = document.getElementById("Tname3").textContent;

    var PIECHARTEXMPLE    = $('#pieChartCustom1');
    var pieChartExample = new Chart(PIECHARTEXMPLE, {
        type: 'pie',
        options: {
            legend: {
                display: true,
                position: "left"
            }
        },
        data: {
            labels: [
                Tname0,
                Tname1,
                Tname2,
                Tname3
            ],
            datasets: [
                {
                    data: [8.88, 8.87, 9.57, 2.06],
                    borderWidth: 0,
                    backgroundColor: [
                        '#723ac3',
                        "#864DD9",
                        "#9762e6",
                        "#a678eb"
                    ],
                    hoverBackgroundColor: [
                        '#723ac3',
                        "#864DD9",
                        "#9762e6",
                        "#a678eb"
                    ]
                }]
            }
    });

    var pieChartExample = {
        responsive: true
    };

        // ------------------------------------------------------- //
    // Pie Chart Custom 2
    // ------------------------------------------------------ //
    var PIECHARTEXMPLE    = $('#pieChartCustom2');
    var pieChartExample = new Chart(PIECHARTEXMPLE, {
        type: 'pie',
        options: {
            legend: {
                display: true,
                position: "left"
            }
        },
        data: {
            labels: [
                "LeeSin",
                "Graves",
                "Nidalee",
                "Ekko"
            ],
            datasets: [
                {
                    data: [16.39, 5.14, 18.01, 5.62],
                    borderWidth: 0,
                    backgroundColor: [
                        '#723ac3',
                        "#864DD9",
                        "#9762e6",
                        "#a678eb"
                    ],
                    hoverBackgroundColor: [
                        '#723ac3',
                        "#864DD9",
                        "#9762e6",
                        "#a678eb"
                    ]
                }]
            }
    });

    var pieChartExample = {
        responsive: true
    };

    // ------------------------------------------------------- //
    // Pie Chart Custom 3
    // ------------------------------------------------------ //
    var PIECHARTEXMPLE    = $('#pieChartCustom3');
    var pieChartExample = new Chart(PIECHARTEXMPLE, {
        type: 'pie',
        options: {
            legend: {
                display: true,
                position: "left"
            }
        },
        data: {
            labels: [
                "TwistedFate",
                "Zoe",
                "Lebianc",
                "Syndra"
            ],
            datasets: [
                {
                    data: [5, 6, 6, 14],
                    borderWidth: 0,
                    backgroundColor: [
                        '#723ac3',
                        "#864DD9",
                        "#9762e6",
                        "#a678eb"
                    ],
                    hoverBackgroundColor: [
                        '#723ac3',
                        "#864DD9",
                        "#9762e6",
                        "#a678eb"
                    ]
                }]
            }
    });

    var pieChartExample = {
        responsive: true
    };


        // ------------------------------------------------------- //
    // Pie Chart Custom 2
    // ------------------------------------------------------ //
    var PIECHARTEXMPLE    = $('#pieChartCustom4');
    var pieChartExample = new Chart(PIECHARTEXMPLE, {
        type: 'pie',
        options: {
            legend: {
                display: true,
                position: "left"
            }
        },
        data: {
            labels: [
                "Aphelios",
                "Ezreal",
                "Kaisa",
                "Ashe"
            ],
            datasets: [
                {
                    data: [40, 21, 20, 9],
                    borderWidth: 0,
                    backgroundColor: [
                        '#723ac3',
                        "#864DD9",
                        "#9762e6",
                        "#a678eb"
                    ],
                    hoverBackgroundColor: [
                        '#723ac3',
                        "#864DD9",
                        "#9762e6",
                        "#a678eb"
                    ]
                }]
            }
    });

    var pieChartExample = {
        responsive: true
    };

    // ------------------------------------------------------- //
    // Pie Chart Custom 2
    // ------------------------------------------------------ //
    var PIECHARTEXMPLE    = $('#pieChartCustom5');
    var pieChartExample = new Chart(PIECHARTEXMPLE, {
        type: 'pie',
        options: {
            legend: {
                display: true,
                position: "left"
            }
        },
        data: {
            labels: [
                "Thresh",
                "Karma",
                "Sett",
                "Bard"
            ],
            datasets: [
                {
                    data: [9, 12, 18, 8],
                    borderWidth: 0,
                    backgroundColor: [
                        '#723ac3',
                        "#864DD9",
                        "#9762e6",
                        "#a678eb"
                    ],
                    hoverBackgroundColor: [
                        '#723ac3',
                        "#864DD9",
                        "#9762e6",
                        "#a678eb"
                    ]
                }]
            }
    });

    var pieChartExample = {
        responsive: true
    };

    });

// var a=0;
function position_act(a){
        if(a==1){ //上单
            document.getElementById("button_1_top").style.background="#34373D";
            document.getElementById("button_1_jungle").style.background = "#2d3035";
            document.getElementById("top").style.display="block";
            document.getElementById("jungle").style.display="none";
            document.getElementById("mid").style.display="none";
            document.getElementById("ADC").style.display="none";
            document.getElementById("support").style.display="none";

            document.getElementById("top_champions").style.display="block";
            document.getElementById("jungle_champions").style.display="none";
            document.getElementById("mid_champions").style.display="none";
            document.getElementById("adc_champions").style.display="none";
            document.getElementById("support_champions").style.display="none";
        }
        else if(a==2) { //打野
            document.getElementById("button_1_jungle").style.background = "#34373D";
            document.getElementById("button_1_top").style.background = "#2d3035";
            document.getElementById("top").style.display = "none";
            document.getElementById("jungle").style.display = "block";
            document.getElementById("mid").style.display = "none";
            document.getElementById("ADC").style.display = "none";
            document.getElementById("support").style.display = "none";

            document.getElementById("top_champions").style.display = "none";
            document.getElementById("jungle_champions").style.display = "block";
            document.getElementById("mid_champions").style.display = "none";
            document.getElementById("adc_champions").style.display = "none";
            document.getElementById("support_champions").style.display = "none";
        }
            else if(a==3){ //中单
            document.getElementById("button_1_jungle").style.background="#34373D";
            document.getElementById("button_1_top").style.background = "#2d3035";
            document.getElementById("top").style.display="none";
            document.getElementById("jungle").style.display="none";
            document.getElementById("mid").style.display="block";
            document.getElementById("ADC").style.display="none";
            document.getElementById("support").style.display="none";

            document.getElementById("top_champions").style.display="none";
            document.getElementById("jungle_champions").style.display="none";
            document.getElementById("mid_champions").style.display="block";
            document.getElementById("adc_champions").style.display="none";
            document.getElementById("support_champions").style.display="none";
        }
            else if(a==4){ //ADC
            document.getElementById("button_1_jungle").style.background="#34373D";
            document.getElementById("button_1_top").style.background = "#2d3035";
            document.getElementById("top").style.display="none";
            document.getElementById("jungle").style.display="none";
            document.getElementById("mid").style.display="none";
            document.getElementById("ADC").style.display="block";
            document.getElementById("support").style.display="none";

            document.getElementById("top_champions").style.display="none";
            document.getElementById("jungle_champions").style.display="none";
            document.getElementById("mid_champions").style.display="none";
            document.getElementById("adc_champions").style.display="block";
            document.getElementById("support_champions").style.display="none";
        }
            else if(a==5){ //辅助
            document.getElementById("button_1_jungle").style.background="#34373D";
            document.getElementById("button_1_top").style.background = "#2d3035";
            document.getElementById("top").style.display="none";
            document.getElementById("jungle").style.display="none";
            document.getElementById("mid").style.display="none";
            document.getElementById("ADC").style.display="none";
            document.getElementById("support").style.display="block";

            document.getElementById("top_champions").style.display="none";
            document.getElementById("jungle_champions").style.display="none";
            document.getElementById("mid_champions").style.display="none";
            document.getElementById("adc_champions").style.display="none";
            document.getElementById("support_champions").style.display="block";
        }
};


$(document).ready(counter_refresh($("#clist").attr("values")));

function counter_refresh(versusid) {
    var cid = $("#currentcid").text();
    // alert(cid);
    $.ajax({
        url:"/counter/refresh",
        method:"post",
        data:{
            cid:cid,
            versusid:versusid,
        },
        success:function (data) {

            $("#versusname").html(data["versus"]["cname"]);
            // "../../../static/img/champImg/{{ current["cid"] }}.png"
            $("img#versuspic").attr("src", "../../../static/img/champImg/" + data["versus"]['cid'] + ".png");
            var attr = ["kdr", "cwin", "kill", "killed", "cs"]
            var ids = ["tr_kdr", "tr_cwin", "tr_kill", "tr_killed", "tr_cs"]
            var name = ["KDR", "胜率","KILL COUNTER","KILLED COUNTER","压刀率(0-10 min)"]
            for (i = 0; i< 5; i++){
                data['current'][attr[i]] = data['current'][attr[i]].toFixed(2);
                data['versus'][attr[i]] = data['versus'][attr[i]].toFixed(2);
                var color_c = "#dee2e6";
                var color_v = "#dee2e6";
                if (data['current'][attr[i]] > data['versus'][attr[i]])
                {
                    color_c = "green";
                    color_v = "#dee2e6"
                }
                else{
                    color_c = "#dee2e6";
                    color_v = "green";
                }
                $("#"+ids[i]).html(
                    "<td style = 'line-height: 24px;font-size: 24px;font-weight:bolder;width:33.33333333333%;color:"  + color_c + " '>" + data['current'][attr[i]] + "</td>" +
                    "<td style = 'width:33.33333333333%' align='center'><h5 style='color: #DB6574'>" + name[i] + "</h5></td>" +
                    "<td style = 'line-height: 24px;font-size: 24px;font-weight:bolder;width:33.33333333333%;color:"+ color_v +" '  align='right'>" + data['versus'][attr[i]] + "</td>"
            );
            };


            var RADARCHARTEXMPLE  = $('#radarChartCustoma');
            var radarChartExample = new Chart(RADARCHARTEXMPLE, {
                type: 'radar',
                options: chartOptions,
                data: {
                    labels: ["A", "B", "C", "D", "E", "C"],
                    datasets: [
                        {
                            label: "First dataset",
                            backgroundColor: "rgba(113, 39, 172, 0.4)",
                            borderWidth: 2,
                            borderColor: "#7127AC",
                            pointBackgroundColor: "#7127AC",
                            pointBorderColor: "#fff",
                            pointHoverBackgroundColor: "#fff",
                            pointHoverBorderColor: "#7127AC",
                            data: [65, 59, 90, 81, 56, 55]
                        },
                        {
                            label: "Second dataset",
                            backgroundColor: "rgba(207, 83, 249, 0.4)",
                            borderWidth: 2,
                            borderColor: "#CF53F9",
                            pointBackgroundColor: "#CF53F9",
                            pointBorderColor: "#fff",
                            pointHoverBackgroundColor: "#fff",
                            pointHoverBorderColor: "#CF53F9",
                            data: [50, 60, 80, 45, 96, 70]
                        }
                    ]
                }
            });
            var radarChartExample = {
                responsive: true
            };



        }
    });
};







