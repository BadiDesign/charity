const vueNotifApp = new Vue({
    delimiters: ['[[', ']]'],
    el: '#notification-vue',
    data() {
        return {
            states: [],
            notification: {},
        }
    },
    created: function () {
        this.getNotifications();
    },
    methods: {
        getNotifications: function () {
            ApiAjaxReader({
                url: NOTIFICATION_SELF_API_URL,
                method: 'GET',
                success_message: false,
                success: (res) => {
                    this.states = res
                }
            })
        },
        setNotif: function (pk, state) {
            ApiAjax({
                url: NOTIFICATION_CHANGE_API_URL,
                pk,
                data: {
                    state,
                },
                method: 'PUT',
                success_message: false,
                success: (result) => {
                    swalFireSuccess(result.detail);
                    this.getNotifications();
                },
            })
        },
        showNotif: function (notif) {
            this.notification = notif;
            $('#notification-vue .modal').modal('show');
        },
        getState: function (state) {
            return ['Unread', 'Read', 'Doing', 'Done'][state]
        },
        getStateColor: function (state) {
            return ['text-danger', 'text-warning', 'text-info', 'text-success'][state]
        },
    },
});

jQuery(document).ready(function () {
    const vueVisitApp = new Vue({
        delimiters: ['[[', ']]'],
        el: '#visit-vue',
        data() {
            return {
                visit: {},
            }
        },
        created: function () {
            this.getVisits();
        },
        methods: {
            getVisits: function () {
                ApiAjaxReader({
                    url: '/api/v1/visit/all/',
                    method: 'GET',
                    success_message: false,
                    success: (res) => {
                        this.visit = res;
                        this.setChart()
                    }
                })
            },
            setChart: function () {
                const options = {
                    series: [
                        {
                            name: 'Visitor',
                            type: 'column',
                            data: this.visit.chart['visitor'].reverse()
                        },
                        {
                            name: 'Visit',
                            type: 'line',
                            data: this.visit.chart['visit'].reverse()
                        }],
                    chart: {
                        height: 350,
                        type: 'line',
                        stacked: true,
                    },
                    dataLabels: {
                        enabled: false
                    },
                    colors: [primary, info],
                    stroke: {
                        width: [1, 4]
                    },
                    title: {
                        text: 'Last 10 Day Visits',
                        align: 'left',
                    },
                    xaxis: {
                        categories: this.visit.chart['label'].reverse(),
                    },
                    yaxis: [
                        {
                            axisTicks: {
                                show: true,
                            },
                            axisBorder: {
                                show: true,
                                color: primary
                            },
                            labels: {
                                style: {
                                    colors: primary,
                                }
                            },
                            title: {
                                text: "Visit",
                                style: {
                                    color: primary,
                                    fontWeight: 'bolder'
                                }
                            },
                            tooltip: {
                                enabled: true
                            }
                        },
                    ],
                    tooltip: {
                        fixed: {
                            enabled: true,
                            position: 'topLeft', // topRight, topLeft, bottomRight, bottomLeft
                            offsetY: 30,
                            offsetX: 60
                        },
                    },
                    legend: {
                        horizontalAlign: 'left',
                        offsetX: 40
                    }
                };
                var chart = new ApexCharts(document.querySelector("#chart-visit"), options);
                chart.render();
            },
        },
    });

})