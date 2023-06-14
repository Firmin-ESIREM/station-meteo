params = new URLSearchParams(window.location.search)

const series = [ {name: params.get('data'), points: {{ chart_data }} } ]

const chart = JSC.chart('theChart', {
    series: series,
    axisToZoom: 'x',
    xAxis_defaultTick_enabled: false,
    legend_visible: false,
    box_fill: (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) ? "#22202D" : "#FFFFFF",
    yAxis_alternateGridFill: "rgba(0,0,0,0)"
});
