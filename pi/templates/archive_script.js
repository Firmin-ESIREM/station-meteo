params = new URLSearchParams(window.location.search)

series = [ {name: params.get('data'), points: {{ chart_data }} } ]

JSC.chart('theChart', {
    series: series
});


