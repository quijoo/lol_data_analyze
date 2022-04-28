function tu01(diffKill) {


    var mychart = echarts.init( document.querySelector(".box_tu01"));


    option = {
    backgroundColor: '#2c343c',

    title: {
        text: '各个位置击杀数占比',
        left: 'center',
        top: 20,
        textStyle: {
            color: '#ccc'
        }
    },

    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)'
    },

    visualMap: {
        show: false,
        min: 80,
        max: 600,
        inRange: {
            colorLightness: [0, 1]
        }
    },
    series: [
        {
            name: '击杀数',
            type: 'pie',
            radius: '65%',
            center: ['50%', '50%'],
            data: [
                {value: diffKill['TOP']/1000, name: '上单'},
                {value: diffKill['JUNGLE']/1000, name: '打野'},
                {value: diffKill['MIDDLE']/1000, name: '中单'},
                {value: diffKill['BOTTOM_CARRY']/1000, name: 'AD'},
                {value: diffKill['BOTTOM_SUPPORT']/1000, name: '辅助'}
            ].sort(function (a, b) { return a.value - b.value; }),
            roseType: 'radius',
            label: {
                color: 'rgba(255, 255, 255, 0.3)'
            },
            labelLine: {
                lineStyle: {
                    color: 'rgba(255, 255, 255, 0.3)'
                },
                smooth: 0.2,
                length: 10,
                length2: 20
            },
            itemStyle: {
                color: '#c23531',
                shadowBlur: 200,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
            },

            animationType: 'scale',
            animationEasing: 'elasticOut',
            animationDelay: function (idx) {
                return Math.random() * 200;
            }
        }
    ]
};

    mychart.setOption(option);

}





