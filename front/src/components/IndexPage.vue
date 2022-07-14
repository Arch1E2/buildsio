<template>
  <div>
    <el-card>
      <template #header>
        <el-row>
          <el-col :span="8" style="margin-right: 5px">
            <el-date-picker
              style="width: 95.5%"
              type="daterange"
              start-placeholder="Дата от"
              end-placeholder="Дата до"
              v-model="selected_dates"
              :clearable="false"
            ></el-date-picker>
          </el-col>
          <el-col :span="9" style="margin-right: 5px">
            <el-select
              style="width: 100%"
              multiple
              placeholder="Выберите котировку или котировки"
              v-model="selected_valutes"
              filterable
              collapse-tags
            >
              <el-option
                v-for="valute in valutes"
                :key="valute.code"
                :label="valute.name"
                :value="valute.code"
              >
              </el-option>
            </el-select>
          </el-col>
          <el-col :span="6" style="text-align: center">
            <el-button
              @click="getRates"
              v-loading="loading"
              style="margin-right: 5px"
              type="primary"
              :disabled="
                selected_dates.length || selected_valutes.length ? false : true
              "
              >Получить котировки</el-button
            >
            <el-dropdown>
              <el-button
                type="primary"
                :disabled="rates && rates.length ? false : true"
              >
                Экспорт
              </el-button>
              <template #dropdown>
                <el-dropdown-menu v-if="rates && rates.length">
                  <a :href="downloadLink.csv" download>
                    <el-dropdown-item>CSV</el-dropdown-item>
                  </a>
                  <a :href="downloadLink.pdf" download>
                    <el-dropdown-item>PDF</el-dropdown-item>
                  </a>
                  <a :href="downloadLink.xlsx" download>
                    <el-dropdown-item>XLSX</el-dropdown-item>
                  </a>
                </el-dropdown-menu>
              </template>
            </el-dropdown>
          </el-col>
        </el-row>
      </template>
      <el-table :data="valutesForShow" v-if="rates && rates.length">
        <el-table-column prop="date" label="Дата" sortable></el-table-column>
        <el-table-column
          prop="valute"
          label="Валюта"
          sortable
        ></el-table-column>
        <el-table-column
          prop="valute_name"
          label="Название"
          sortable
        ></el-table-column>
        <el-table-column
          prop="value"
          label="Покупка"
          sortable
        ></el-table-column>
        <el-table-column
          prop="nominal"
          label="Номинал"
          sortable
        ></el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import map from "lodash/map";
import find from "lodash/find";
export default {
  data() {
    return {
      valutes: [],
      selected_dates: [],
      selected_valutes: [],
      rates: [],
      loading: false,
      last_rate_request: "",
    };
  },
  computed: {
    valutesForShow() {
      return map(this.rates, (rate) => {
        return {
          valute_name: find(this.valutes, { code: rate.valute }).name,
          ...rate,
        };
      });
    },
    downloadLink() {
      return {
        csv: `${axios.defaults.baseURL}render_to_csv/${this.last_rate_request}`,
        pdf: `${axios.defaults.baseURL}render_to_pdf/${this.last_rate_request}`,
        xlsx: `${axios.defaults.baseURL}render_to_xlsx/${this.last_rate_request}`,
      };
    },
  },
  mounted() {
    this.getValutes();
  },
  methods: {
    getValutes() {
      return axios.get("get_valutes/").then((response) => {
        this.valutes = response.data;
      });
    },
    getRates() {
      var valutes = this.selected_valutes.join(",");
      this.last_rate_request += `?valutes=${valutes}`;
      if (this.selected_dates) {
        var date__gte = moment(this.selected_dates[0]).format("YYYY-MM-DD");
        var date__lte = moment(this.selected_dates[1]).format("YYYY-MM-DD");
        this.last_rate_request += `&date__gte=${date__gte}&date__lte=${date__lte}`;
      }
      this.loading = true;
      return axios
        .get("get_rates/", {
          params: {
            date__gte: date__gte,
            date__lte: date__lte,
            valutes: valutes,
          },
        })
        .then((response) => {
          this.rates = response.data;
          this.loading = false;
        });
    },
    download(type) {
      return axios.get("render_to_" + type + "/" + this.last_rate_request);
    },
  },
};
</script>