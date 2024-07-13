from helpers.height_pilot_helpers import *


def read_inputs() -> dict:
    """
    reads all the data from csv files for this pilot. Data was cleaned for users which failed the attention or comprehension checks
    :return: dictionary with the participants' answers by organization
    """
    base_path = "data/height_pilot_data/"
    tasks = ["task1", "task2", "task3", "task4"]
    data = {}
    for index, task in enumerate(tasks):
        gy_part = pd.read_csv(base_path + "gy_t" + str(index) + "_cleaned.csv")
        list_part = pd.read_csv(base_path + "list_t" + str(index) + "_cleaned.csv")
        data[task] = {"gy": gy_part, "list": list_part}
    return data


def task_1_plotter(t1_df_merged: pd.DataFrame) -> dict:
    """
    Plots the data for task 1 and return the statistics for each height and visualization for both costs and time
    :param t1_df_merged: data for task 1
    :return: statistics as a dictionary
    """
    dependent_variable_name = "history_lowest_elec_cost"
    t1_df_merged.dropna(subset=["history_lowest_elec_cost"], inplace=True)
    line_chart_df = t1_df_merged[t1_df_merged["visualization"] == "line_chart"]
    colorfield_df = t1_df_merged[t1_df_merged["visualization"] == "heatmap"]
    # generates some 1D descriptive statistics for each height group
    task_number = [i for i in list(locals().keys()) if i.__contains__("_df_merged")][0].split("_df_merged")[0].split("t")[1]
    lc_stats, h_stats = get_1D_statistics_for_each_height(colorfield_df, line_chart_df, dependent_variable_name, int(task_number))
    # calculates the statistics for each height and visualization as in the dissertation and potentially future papers
    means_stats_payload = stats_means_accuracy_height(t1_df_merged, dependent_variable_name)
    stats_1d = {"line_chart": lc_stats, "colorfields": h_stats}
    means_stats_payload["stats_1d"] = stats_1d
    viz_stats_payload = stats_means_accuracy_viz(t1_df_merged, dependent_variable_name)
    time_height_stats_payload = stats_means_time_height(t1_df_merged)
    viz_time_stats_payload = stats_means_time_viz(t1_df_merged)
    boxplots(colorfield_df, line_chart_df, dependent_variable_name, t1_df_merged)
    full_stats = {"cost_means_stats": {
        "elec_cost_by_height_stats": means_stats_payload,
        "elec_costs_by_viz_lc_or_cf": viz_stats_payload,
    },
        "time_means_stats": {
            "time_to_execute_by_height": time_height_stats_payload,
            "time_by_viz_lc_or_h": viz_time_stats_payload,
        }}
    return full_stats


def task_2_plotter(t2_df_merged: pd.DataFrame) -> dict:
    """
    Plots the data for task 2 and return the statistics for each height and visualization for both costs and time
    :param t2_df_merged: data for task 2
    :return: statistics as a dictionary
    """
    dependent_variable_name = "history_lowest_overall_cost"
    line_chart_df = t2_df_merged[t2_df_merged["visualization"] == "line_chart"]
    colorfield_df = t2_df_merged[t2_df_merged["visualization"] == "heatmap"]
    lc_stats = []
    # generates some 1D descriptive statistics for each height group
    task_number = [i for i in list(locals().keys()) if i.__contains__("_df_merged")][0].split("_df_merged")[0].split("t")[1]
    lc_stats, h_stats = get_1D_statistics_for_each_height(colorfield_df, line_chart_df, dependent_variable_name, int(task_number))
    # calculates the statistics for each height and visualization as in the dissertation and potentially future papers
    means_stats_payload = stats_means_accuracy_height(t2_df_merged, dependent_variable_name)
    stats_1d = {"line_chart": lc_stats, "heatmap": h_stats}
    means_stats_payload["stats_1d"] = stats_1d
    viz_stats_payload = stats_means_accuracy_viz(t2_df_merged, dependent_variable_name)
    time_height_stats_payload = stats_means_time_height(t2_df_merged)
    viz_time_stats_payload = stats_means_time_viz(t2_df_merged)
    boxplots(colorfield_df, line_chart_df, dependent_variable_name, t2_df_merged)
    full_stats = {"cost_means_stats": {
        "total_costs_by_height_stats": means_stats_payload,
        "total_costs_by_viz_lc_or_hm": viz_stats_payload,
    },
        "time_means_stats": {
            "time_to_execute_by_height": time_height_stats_payload,
            "time_by_viz_lc_or_h": viz_time_stats_payload,
        }}
    return full_stats


def task_3_plotter(t3_df_merged: pd.DataFrame) -> dict:
    """
    Plots the data for task 3 and return the statistics for each height and visualization for both costs and time
    :param t3_df_merged: data for task 3
    :return: statistics as a dictionary
    """
    dependent_variable_name = "history_lowest_overall_cost"
    line_chart_df = t3_df_merged[t3_df_merged["visualization"] == "line_chart"]
    colorfield_df = t3_df_merged[t3_df_merged["visualization"] == "heatmap"]
    lc_stats = []
    # generates some 1D descriptive statistics for each height group
    task_number = [i for i in list(locals().keys()) if i.__contains__("_df_merged")][0].split("_df_merged")[0].split("t")[1]
    lc_stats, h_stats = get_1D_statistics_for_each_height(colorfield_df, line_chart_df, dependent_variable_name, int(task_number))
    # calculates the statistics for each height and visualization as in the dissertation and potentially future papers
    means_stats_payload = stats_means_accuracy_height(t3_df_merged, "history_lowest_overall_cost")
    stats_1d = {"line_chart": lc_stats, "heatmap": h_stats}
    means_stats_payload["stats_1d"] = stats_1d
    viz_stats_payload = stats_means_accuracy_viz(t3_df_merged, "history_lowest_overall_cost")
    time_height_stats_payload = stats_means_time_height(t3_df_merged)
    viz_time_stats_payload = stats_means_time_viz(t3_df_merged)
    boxplots(colorfield_df, line_chart_df, dependent_variable_name, t3_df_merged)
    full_stats = {"cost_means_stats": {
        "total_costs_by_height_stats": means_stats_payload,
        "total_costs_by_viz_lc_or_hm": viz_stats_payload,
    },
        "time_means_stats": {
            "time_to_execute_by_height": time_height_stats_payload,
            "time_by_viz_lc_or_h": viz_time_stats_payload,
        }}
    return full_stats


def task_4_plotter(t4_df_merged: pd.DataFrame) -> dict:
    dependent_variable_name = "history_highest_overall_cost"
    line_chart_df = t4_df_merged[t4_df_merged["visualization"] == "line_chart"]
    colorfield_df = t4_df_merged[t4_df_merged["visualization"] == "heatmap"]
    lc_stats = []
    # generates some 1D descriptive statistics for each height group
    task_number = [i for i in list(locals().keys()) if i.__contains__("_df_merged")][0].split("_df_merged")[0].split("t")[1]
    lc_stats, h_stats = get_1D_statistics_for_each_height(colorfield_df, line_chart_df, dependent_variable_name, int(task_number))
    # calculates the statistics for each height and visualization as in the dissertation and potentially future papers
    means_accuracy_height_stats_payload = stats_means_accuracy_height(t4_df_merged, "history_highest_overall_cost")
    stats_1d = {"line_chart": lc_stats, "heatmap": h_stats}
    means_accuracy_height_stats_payload["stats_1d"] = stats_1d
    means_accuracy_viz_stats_payload = stats_means_accuracy_viz(t4_df_merged, "history_highest_overall_cost")
    time_height_stats_payload = stats_means_time_height(t4_df_merged)
    viz_time_stats_payload = stats_means_time_viz(t4_df_merged)
    boxplots(colorfield_df, line_chart_df, dependent_variable_name, t4_df_merged)
    full_stats = {"cost_means_stats": {
        "total_costs_by_height_stats": means_accuracy_height_stats_payload,
        "total_costs_by_viz_lc_or_hm": means_accuracy_viz_stats_payload,
    },
        "time_means_stats": {
            "time_to_execute_by_height": time_height_stats_payload,
            "time_by_viz_lc_or_h": viz_time_stats_payload,
        }}
    return full_stats


def main():
    data = read_inputs()
    tasks = ["task1", "task2", "task3", "task4"]
    plotters = [task_1_plotter, task_2_plotter, task_3_plotter,task_4_plotter]
    for index, task_number in enumerate(tasks):
        concat_df = concater(data[task_number]["gy"], data[task_number]["list"])
        plotter = plotters[index]
        result = plotter(concat_df)
        print(f"""results for {task_number} are: 
        {result}""")


if __name__ == '__main__':
    main()

