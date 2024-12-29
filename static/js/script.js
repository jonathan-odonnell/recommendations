$('#categories').change(function() {
    let category = $(this).val().toLowerCase().replace(' ', '_');
    let currentUrl = new URL(window.location);
    currentUrl.searchParams.set("category", category); 
    window.location.replace(currentUrl);
})
let dataset = JSON.parse($('#dataset').text())
let beveragesChartLabel = function() {
    if (dataset['unit']) {
        return `${dataset['category']} (${dataset['unit']})`
    } else {
        return `${dataset['category']}`
    }
}
new Chart($('#beverage-categories-chart'), {
    type: 'pie',
    data: {
      labels: dataset['beverage_categories_labels'],
      datasets: [{
        data: dataset['beverage_categories_data'],
        hoverOffset: 4
      }]
    },
    options: {
      plugins: {
            legend: {
                position: 'left'
            },
            title: {
                display: true,
                text: 'Beverage Types by Category',
            }
        }
    }
});
new Chart($('#nutrients-chart'), {
    type: 'bar',
    data: {
      labels: dataset['nutrients_labels'],
      datasets: [{
        label: beveragesChartLabel(),
        data: dataset['nutrients_data'],
        borderWidth: 1
      }]
    },
    options: {
      maintainAspectRatio: false,
      scales: {
        x: {
			ticks: {
				maxRotation: 45,
				minRotation: 45,
			}
		},
        y: {
          beginAtZero: true
        },
      },
      plugins: {
            title: {
                display: true,
                text:`Beverage Types by Average ${dataset['category'].replace(/ *\([^)]*\) */g, '')}`,
            }
        }
    }
  });
  new Chart($('#beverages-chart'), {
    type: 'doughnut',
    data: {
      labels: dataset['beverages_labels'],
      datasets: [{
        data: dataset['beverages_data'],
        hoverOffset: 4
      }]
    },
    options: {
      plugins: {
            legend: {
                position: 'left'
            },
            title: {
                display: true,
                text: '5 Highest and Lowest Beverage Types',
            }
        }
    }
});
new Chart($('#calories-sugar-chart'), {
    type: 'scatter',
    data: {
      labels: dataset['calories_sugar_labels'],
      datasets: [{
        data: dataset['calories_sugar_data'],
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
      }]
    },
    options: {
      maintainAspectRatio: false,
      plugins: {
            title: {
                display: true,
                text: 'Sugar and Calories for Beverage Types',
            },
            legend: {
                display: false,
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Calories',
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Sugar (g)',
                }
            }
        }
    }
});