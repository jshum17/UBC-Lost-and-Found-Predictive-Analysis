<template>
  <div>
    <div class="row">
      <div class="col-lg-6">
        <card type="chart">
          <template slot="header">
            <div class="row">
              <div class="col-sm-6" :class="isRTL ? 'text-right' : 'text-left'">
                <h5 class="card-category">Lost Item Trend</h5>
                <h2 class="card-title">Monthly Count</h2>
              </div>
              <div class="col-sm-6">
                <div
                  class="btn-group btn-group-toggle"
                  :class="isRTL ? 'float-left' : 'float-right'"
                  data-toggle="buttons"
                >
                  <label
                    v-for="(option, index) in years"
                    :key="option"
                    class="btn btn-sm btn-primary btn-simple"
                    :class="{ active: timelineChart.activeIndex === index }"
                    :id="index"
                  >
                    <input
                      type="radio"
                      @click="initTimeChart(index)"
                      name="options"
                      autocomplete="off"
                      :checked="timelineChart.activeIndex === index"
                    />
                    {{ option }}
                  </label>
                </div>
              </div>
            </div>
          </template>
          <div class="chart-area">
            <line-chart
              style="height: 100%"
              ref="timeChart"
              chart-id="time-line-chart"
              :chart-data="timelineChart.chartData"
              :gradient-colors="timelineChart.gradientColors"
              :gradient-stops="timelineChart.gradientStops"
              :extra-options="timelineChart.extraOptions"
            >
            </line-chart>
          </div>
        </card>
      </div>
      <div class="col-lg-6" :class="{ 'text-right': isRTL }">
        <card type="chart">
          <template slot="header">
            <h5 class="card-category">Lost Item Prediction</h5>
            <h3 class="card-title">
              <i class="tim-icons icon-send text-success"></i> Daily Forecast
            </h3>
          </template>
          <div class="chart-area">
            <line-chart
              style="height: 100%"
              ref="forecastLineChart"
              chart-id="forecast-Line-Chart"
              :chart-data="forecastLineChart.chartData"
              :gradient-stops="forecastLineChart.gradientStops"
              :extra-options="forecastLineChart.extraOptions"
            >
            </line-chart>
          </div>
        </card>
      </div>
    </div>
    <!-- <div class="row">
      
    </div> -->
    <div class="row">
      <div class="col-12">
        <card class="card" :header-classes="{ 'text-right': isRTL }">
          <h4 slot="header" class="card-title">All Lost Items</h4>
          <div class="table-responsive item-table">
            <base-table
              :data="tableData"
              :columns="tableColumns"
              thead-classes="text-primary"
            >
            </base-table>
          </div>
        </card>
      </div>
    </div>
  </div>
</template>
<script>
import LineChart from "@/components/Charts/LineChart";
import BarChart from "@/components/Charts/BarChart";
import * as chartConfigs from "@/components/Charts/config";
import { BaseTable } from "@/components";
import config from "@/config";
import api from "@/services/api";

export default {
  components: {
    LineChart,
    BarChart,
    BaseTable,
  },
  data() {
    return {
      timelineChart: {
        allData: [],
        activeIndex: 0,
        chartData: {
          datasets: [{}],
          labels: [],
        },
        extraOptions: chartConfigs.timeChartOptions,
        gradientColors: config.colors.primaryGradient,
        gradientStops: [1, 0.4, 0],
        categories: [],
      },
      forecastLineChart: {
        extraOptions: chartConfigs.forecastLineChartOptions,
        chartData: {
          labels: [],
          datasets: [
            {
              label: "Predicted Count",
              fill: true,
              borderColor: config.colors.red,
              borderWidth: 2,
              borderDash: [5, 5],
              borderDashOffset: 0.0,
              pointBackgroundColor: config.colors.red,
              pointBorderColor: "rgba(255,255,255,0)",
              pointHoverBackgroundColor: config.colors.red,
              pointBorderWidth: 20,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 15,
              pointRadius: 4,
              data: [],
            },
          ],
        },
        gradientColors: [
          "rgba(66,134,121,0.15)",
          "rgba(66,134,121,0.0)",
          "rgba(66,134,121,0)",
        ],
        gradientStops: [1, 0.4, 0],
      },
      tableData: [],
      tableColumns: [
        { key: "id", label: "ID" },
        { key: "item_type", label: "Item Type" },
        { key: "description", label: "Description" },
        { key: "date_lost", label: "Date Lost" },
        { key: "location", label: "Location" },
        { key: "status", label: "Status" },
      ],
    }
  },
  computed: {
    enableRTL() {
      return this.$route.query.enableRTL;
    },
    isRTL() {
      return this.$rtl.isRTL;
    },
    years() {
      return ["2024", "2025"];
    },
  },
  async created() {
    // Fetch data from Flask backend
    await this.fetchMonthlyTrend();
    await this.fetchAllItems();
    await this.fetchDailyForecast();
  },
  methods: {
    async fetchMonthlyTrend() {
      try {
        const response2024 = await api.getCount2024();
        let data2024 = response2024.data.map((d) => d.count);
        let paddedData2024 = new Array(4).fill(null).concat(data2024);
        this.timelineChart.allData[0] = paddedData2024;
        this.initTimeChart(0);

        const response2025 = await api.getCount2025();
        this.timelineChart.allData[1] = response2025.data.map((d) => d.count);
        this.initTimeChart(1);
      } catch (error) {
        console.error("Error fetching monthly trend data:", error);
      }
    },
    async fetchDailyForecast() {
      try {
        const lstmResponse = await api.getDailyForecast();
        let lstmPredictions = lstmResponse.data.counts;
        let futureDates = lstmResponse.data.dates;

        // Update the chart data with predictions and future dates
        this.forecastLineChart.chartData = {
          labels: futureDates,  // Use future dates as labels
          datasets: [
            {
              label: "Predicted Count",
              fill: true,
              borderColor: config.colors.red,
              borderWidth: 2,
              borderDash: [5, 5],
              borderDashOffset: 0.0,
              pointBackgroundColor: config.colors.red,
              pointBorderColor: "rgba(255,255,255,0)",
              pointHoverBackgroundColor: config.colors.red,
              pointBorderWidth: 20,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 15,
              pointRadius: 4,
              data: lstmPredictions, 
            },
          ],
        };
      } catch (error) {
        console.error("Error fetching prediction data:", error);
      }
    },
    async fetchAllItems() {
      try {
        const response = await api.getItems();
        console.log("Fetched items:", response.data); // Log the fetched data
        this.tableData = response.data.map(item => ({
          ...item,
          date_lost: this.formatDate(item.date_lost)
        }));
      } catch (error) {
        console.error("Error fetching all items data:", error);
      }
    },
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'short', day: 'numeric' };
      return new Date(dateString).toLocaleDateString(undefined, options);
    },
    initTimeChart(index) {
      let chartData = {
        datasets: [
          {
            fill: true,
            borderColor: config.colors.primary,
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            pointBackgroundColor: config.colors.primary,
            pointBorderColor: "rgba(255,255,255,0)",
            pointHoverBackgroundColor: config.colors.primary,
            pointBorderWidth: 20,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 15,
            pointRadius: 4,
            data: this.timelineChart.allData[index],
          }
        ],
        labels: [
          "JAN",
          "FEB",
          "MAR",
          "APR",
          "MAY",
          "JUN",
          "JUL",
          "AUG",
          "SEP",
          "OCT",
          "NOV",
          "DEC",
        ],
      };
      this.$refs.timeChart.updateGradients(chartData);
      this.timelineChart.chartData = chartData;
      this.timelineChart.activeIndex = index;
    },
  },
  mounted() {
    this.i18n = this.$i18n;
    if (this.enableRTL) {
      this.i18n.locale = "ar";
      this.$rtl.enableRTL();
    }
    this.initTimeChart(0);
  },
  beforeDestroy() {
    if (this.$rtl.isRTL) {
      this.i18n.locale = "en";
      this.$rtl.disableRTL();
    }
  },
};
</script>
<style>
.item-table {
  max-height: 400px;
  overflow-y: auto;
  overflow-x: hidden;
}

.item-table::-webkit-scrollbar {
  width: 10px; 
}

.item-table::-webkit-scrollbar-thumb {
  background-color: rgba(98, 97, 97, 0.5); 
  border-radius: 10px; 
  height:70px;
}

.item-table::-webkit-scrollbar-thumb:hover {
  background-color: rgba(104, 104, 104, 0.7); 
}

.item-table::-webkit-scrollbar-track {
  background: transparent; 
}
</style>

