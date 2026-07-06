// ============================================
// Activity Analytics Platform
// Dashboard JavaScript
// ============================================


// --------------------------------------------
// Global Chart Objects
// --------------------------------------------

let dailyChart = null;

let hourlyChart = null;

let weekdayChart = null;

let categoryChart = null;


// --------------------------------------------
// Dashboard Cards
// --------------------------------------------

async function loadDashboard() {

    try {

        const response = await fetch("/api/dashboard");

        const data = await response.json();


        document.getElementById("todayScreenTime").innerText =
            data.today_screen_time + " sec";


        document.getElementById("totalScreenTime").innerText =
            data.total_screen_time + " sec";


        document.getElementById("totalSessions").innerText =
            data.total_sessions;


        document.getElementById("applicationSwitches").innerText =
            data.application_switches;


        document.getElementById("longestApplication").innerText =
            data.longest_session.application;


        document.getElementById("longestDuration").innerText =
            data.longest_session.duration + " sec";

    }

    catch (error) {

        console.error(
            "Dashboard Error:",
            error
        );

    }

}


// --------------------------------------------
// Destroy Existing Chart
// --------------------------------------------

function destroyChart(chart) {

    if (chart) {

        chart.destroy();

    }

}


// --------------------------------------------
// Common Chart Options
// --------------------------------------------

const commonOptions = {

    responsive: true,

    maintainAspectRatio: false,

    plugins: {

        legend: {

            labels: {

                color: "white"

            }

        }

    },

    scales: {

        x: {

            ticks: {

                color: "white"

            },

            grid: {

                color: "#334155"

            }

        },

        y: {

            beginAtZero: true,

            ticks: {

                color: "white"

            },

            grid: {

                color: "#334155"

            }

        }

    }

};
// ============================================
// Daily Activity Chart
// ============================================

async function loadDailyChart() {

    try {

        const response = await fetch("/api/daily");

        const data = await response.json();

        destroyChart(dailyChart);

        dailyChart = new Chart(

            document.getElementById("dailyChart"),

            {

                type: "line",

                data: {

                    labels: data.map(item => item.date),

                    datasets: [{

                        label: "Daily Screen Time",

                        data: data.map(item => item.duration),

                        borderColor: "#38bdf8",

                        backgroundColor: "rgba(56,189,248,0.2)",

                        borderWidth: 3,

                        fill: true,

                        tension: 0.4

                    }]

                },

                options: commonOptions

            }

        );

    }

    catch (error) {

        console.error("Daily Chart Error:", error);

    }

}



// ============================================
// Hourly Activity Chart
// ============================================

async function loadHourlyChart() {

    try {

        const response = await fetch("/api/hourly");

        const data = await response.json();

        destroyChart(hourlyChart);

        hourlyChart = new Chart(

            document.getElementById("hourlyChart"),

            {

                type: "bar",

                data: {

                    labels: data.map(item => item.hour),

                    datasets: [{

                        label: "Hourly Usage",

                        data: data.map(item => item.duration),

                        backgroundColor: "#3b82f6"

                    }]

                },

                options: commonOptions

            }

        );

    }

    catch (error) {

        console.error("Hourly Chart Error:", error);

    }

}



// ============================================
// Weekday Activity Chart
// ============================================

async function loadWeekdayChart() {

    try {

        const response = await fetch("/api/weekday");

        const data = await response.json();

        destroyChart(weekdayChart);

        weekdayChart = new Chart(

            document.getElementById("weekdayChart"),

            {

                type: "bar",

                data: {

                    labels: data.map(item => item.day),

                    datasets: [{

                        label: "Weekday Usage",

                        data: data.map(item => item.duration),

                        backgroundColor: "#10b981"

                    }]

                },

                options: commonOptions

            }

        );

    }

    catch (error) {

        console.error("Weekday Chart Error:", error);

    }

}
// ============================================
// Category Breakdown Chart
// ============================================

async function loadCategoryChart() {

    try {

        const response = await fetch("/api/category-percentage");

        const data = await response.json();

        destroyChart(categoryChart);

        categoryChart = new Chart(

            document.getElementById("categoryChart"),

            {

                type: "doughnut",

                data: {

                    labels: data.map(item => item.category),

                    datasets: [{

                        label: "Category Percentage",

                        data: data.map(item => item.percentage),

                        backgroundColor: [

                            "#3b82f6",
                            "#10b981",
                            "#f59e0b",
                            "#ef4444",
                            "#8b5cf6",
                            "#06b6d4",
                            "#ec4899",
                            "#84cc16"

                        ],

                        borderWidth: 1

                    }]

                },

                options: {

                    responsive: true,

                    maintainAspectRatio: false,

                    plugins: {

                        legend: {

                            position: "bottom",

                            labels: {

                                color: "white"

                            }

                        }

                    }

                }

            }

        );

    }

    catch (error) {

        console.error(

            "Category Chart Error:",

            error

        );

    }

}



// ============================================
// Refresh Everything
// ============================================

async function refreshDashboard() {

    await loadDashboard();

    await loadDailyChart();

    await loadHourlyChart();

    await loadWeekdayChart();

    await loadCategoryChart();

}



// ============================================
// Initial Load
// ============================================

window.onload = function () {

    refreshDashboard();

};



// ============================================
// Auto Refresh
// ============================================

setInterval(

    refreshDashboard,

    10000

);