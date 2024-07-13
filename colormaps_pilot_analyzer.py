from helpers.colormap_pilot_helpers import *
from helpers.common_helpers import *
import pprint

def read_data():
    df = pd.read_csv("data/colormap_pilot_data/colormapPilot_all.csv", delimiter="|")
    df = clean_raw_df(df)
    df.columns = ["userID", "stepName", "stepValue", "studyID", "sessionID", "timeBackend"]
    df = remove_invalid_submissions(df)
    return df


def task_1_plotter(t1_df_merged: pd.DataFrame):
    line_chart_df = t1_df_merged[t1_df_merged["visualization"] == "line_chart"]
    heatmap_df = t1_df_merged[t1_df_merged["visualization"] == "heatmap"]
    dependent_variable_name = "history_lowest_elec_cost"
    task_number = [i for i in list(locals().keys()) if i.__contains__("_df_merged")][0].split("_df_merged")[0].split("t")[1]
    lc_stats, h_stats = get_1d_stats_on_colormaps(line_chart_df, heatmap_df, dependent_variable_name, task_number)
    # the statistics for each of the 1d data are stored in lc_stats for line_charts and in h_stats for heatmaps
    means_stats_payload = stats_means_accuracy_colormaps(t1_df_merged, "history_lowest_elec_cost")
    stats_1d = {"line_chart": lc_stats, "heatmap": h_stats}
    means_stats_payload["stats_1d"] = stats_1d
    viz_stats_payload = stats_means_accuracy_viz(t1_df_merged, "history_lowest_elec_cost")
    time_colormaps_stats_payload = stats_means_time_colormap(t1_df_merged)
    time_viz_stats_payload = stats_means_time_viz(t1_df_merged)
    means_quali_seq_stats_payload = stats_means_sequential_qualitative_accuracy(t1_df_merged,
                                                                                "history_lowest_elec_cost")
    time_quali_seq_stats_payload = stats_means_sequential_qualitative_time(t1_df_merged, "history_lowest_elec_cost")
    # here statistical results stop
    line_chart_df.boxplot(column="history_lowest_elec_cost", by=["colormap"], showmeans=True)
    plt.title("line_chart")
    plt.ylabel("history_lowest_elec_cost [-]")
    heatmap_df["colormap"] = pd.Categorical(heatmap_df["colormap"], categories=["i_want_hue", "mokole", "set1", "oranges", "purple2", "yellow_red"])
    heatmap_df.sort_values("colormap", inplace=True)
    heatmap_df.boxplot(column="history_lowest_elec_cost", by=["colormap"])
    plt.ylabel("history_lowest_elec_cost [-]")
    plt.title("heatmap")
    plt.show()
    t1_df_merged.boxplot(column="history_lowest_elec_cost", by=["visualization"])
    plt.ylabel("history_lowest_elec_cost [-]")
    plt.title("line_charts vs colorfields")
    plt.show()
    print(f"===============DONE in for task 1==================")
    full_stats = {"cost_means_stats": {
        "elec_cost_colormaps_means_stats": means_stats_payload,
        "elec_costs_by_viz_lc_or_hm": viz_stats_payload,
        "elec_costs_by_seq_or_quali": means_quali_seq_stats_payload
    },
        "time_means_stats": {
            "time_to_execute_colormaps": time_colormaps_stats_payload,
            "time_by_viz_lc_or_h": time_viz_stats_payload,
            "time_by_seq_or_quali": time_quali_seq_stats_payload
        }}
    return full_stats


def task_2_plotter(t2_df_merged: pd.DataFrame):
    line_chart_df = t2_df_merged[t2_df_merged["visualization"] == "line_chart"]
    heatmap_df = t2_df_merged[t2_df_merged["visualization"] == "heatmap"]
    dependent_variable_name = "history_lowest_overall_cost"
    task_number = [i for i in list(locals().keys()) if i.__contains__("_df_merged")][0].split("_df_merged")[0].split("t")[1]
    lc_stats, h_stats = get_1d_stats_on_colormaps(line_chart_df, heatmap_df, dependent_variable_name, task_number)
    means_stats_payload = stats_means_accuracy_colormaps(t2_df_merged, dependent_variable_name)
    stats_1d = {"line_chart": lc_stats, "heatmap": h_stats}
    means_stats_payload["stats_1d"] = stats_1d
    viz_stats_payload = stats_means_accuracy_viz(t2_df_merged, dependent_variable_name)
    time_colormap_stats_payload = stats_means_time_colormap(t2_df_merged)
    time_viz_stats_payload = stats_means_time_viz(t2_df_merged)
    means_quali_seq_stats_payload = stats_means_sequential_qualitative_accuracy(t2_df_merged, dependent_variable_name)
    time_quali_seq_stats_payload = stats_means_sequential_qualitative_time(t2_df_merged, dependent_variable_name)
    line_chart_df.boxplot(column=dependent_variable_name, by=["colormap"], showmeans=True)
    plt.title("line_chart")
    plt.ylabel("total_cost [-]")
    heatmap_df["colormap"] = pd.Categorical(heatmap_df["colormap"], categories=["i_want_hue", "mokole", "set1", "oranges", "purple2", "yellow_red"])
    heatmap_df.sort_values("colormap", inplace=True)
    heatmap_df.boxplot(column=dependent_variable_name, by=["colormap"], showmeans=True)
    plt.title("heatmap")
    plt.ylabel("total_cost [-]")
    t2_df_merged.boxplot(column=dependent_variable_name, by=["visualization"], showmeans=True)
    plt.ylabel("history_lowest_overall_cost [-]")
    plt.title("line_charts vs colorfields")
    plt.show()
    # plt.show()
    print(f"===============DONE in for task 2==================")
    full_stats = {"cost_means_stats": {
        "total_costs_colormaps_means_stats": means_stats_payload,
        "total_costs_by_viz_lc_or_hm": viz_stats_payload,
        "total_costs_by_seq_or_quali": means_quali_seq_stats_payload
    },
        "time_means_stats": {
            "time_to_execute_colormaps": time_colormap_stats_payload,
            "time_by_viz_lc_or_h": time_viz_stats_payload,
            "time_by_seq_or_quali": time_quali_seq_stats_payload
        }}
    return full_stats


def task_3_plotter(t3_df_merged: pd.DataFrame):
    line_chart_df = t3_df_merged[t3_df_merged["visualization"] == "line_chart"]
    heatmap_df = t3_df_merged[t3_df_merged["visualization"] == "heatmap"]
    dependent_variable_name = "history_lowest_overall_cost"
    task_number = [i for i in list(locals().keys()) if i.__contains__("_df_merged")][0].split("_df_merged")[0].split("t")[1]
    lc_stats, h_stats = get_1d_stats_on_colormaps(line_chart_df, heatmap_df, dependent_variable_name, task_number)
    means_stats_payload = stats_means_accuracy_colormaps(t3_df_merged, dependent_variable_name)
    stats_1d = {"line_chart": lc_stats, "heatmap": h_stats}
    means_stats_payload["stats_1d"] = stats_1d
    viz_stats_payload = stats_means_accuracy_viz(t3_df_merged, dependent_variable_name)
    time_colormap_stats_payload = stats_means_time_colormap(t3_df_merged)
    viz_time_stats_payload = stats_means_time_viz(t3_df_merged)
    means_quali_seq_stats_payload = stats_means_sequential_qualitative_accuracy(t3_df_merged,
                                                                                dependent_variable_name)
    time_quali_seq_stats_payload = stats_means_sequential_qualitative_time(t3_df_merged, dependent_variable_name)
    line_chart_df.boxplot(column=dependent_variable_name, by=["colormap"], showmeans=True)
    plt.title("line_chart")
    plt.ylabel("history_lowest_overall_cost [-]")
    heatmap_df["colormap"] = pd.Categorical(heatmap_df["colormap"], categories=["i_want_hue", "mokole", "set1", "oranges", "purple2", "yellow_red"])
    heatmap_df.sort_values("colormap", inplace=True)
    heatmap_df.boxplot(column=dependent_variable_name, by=["colormap"], showmeans=True)
    plt.title("heatmap")
    plt.ylabel("history_lowest_overall_cost [-]")
    t3_df_merged.boxplot(column=dependent_variable_name, by=["visualization"], showmeans=True)
    plt.ylabel("history_lowest_overall_cost [-]")
    plt.title("line charts vs colorfields")
    print(f"===============DONE in for task 3==================")
    full_stats = {"cost_means_stats": {
        "total_costs_colormaps_means_stats": means_stats_payload,
        "total_costs_by_viz_lc_or_hm": viz_stats_payload,
        "total_costs_by_seq_or_quali": means_quali_seq_stats_payload
    },
        "time_means_stats": {
            "time_to_execute_colormaps": time_colormap_stats_payload,
            "time_by_viz_lc_or_h": viz_time_stats_payload,
            "time_by_seq_or_quali": time_quali_seq_stats_payload
        }}
    return full_stats


def task_4_plotter(t4_df_merged: pd.DataFrame):
    line_chart_df = t4_df_merged[t4_df_merged["visualization"] == "line_chart"]
    heatmap_df = t4_df_merged[t4_df_merged["visualization"] == "heatmap"]
    dependent_variable_name = "history_highest_overall_cost"
    task_number = [i for i in list(locals().keys()) if i.__contains__("_df_merged")][0].split("_df_merged")[0].split("t")[1]
    lc_stats, h_stats = get_1d_stats_on_colormaps(line_chart_df, heatmap_df, dependent_variable_name, task_number)
    means_accuracy_colormap_stats_payload = stats_means_accuracy_colormaps(t4_df_merged, dependent_variable_name)
    stats_1d = {"line_chart": lc_stats, "heatmap": h_stats}
    means_accuracy_colormap_stats_payload["stats_1d"] = stats_1d
    means_accuracy_viz_stats_payload = stats_means_accuracy_viz(t4_df_merged, dependent_variable_name)
    time_colormap_stats_payload = stats_means_time_colormap(t4_df_merged)
    time_viz_stats_payload = stats_means_time_viz(t4_df_merged)
    means_quali_seq_stats_payload = stats_means_sequential_qualitative_accuracy(t4_df_merged,
                                                                                dependent_variable_name)
    time_quali_seq_stats_payload = stats_means_sequential_qualitative_time(t4_df_merged, dependent_variable_name)
    line_chart_df.boxplot(column=dependent_variable_name, by=["colormap"], showmeans=True)
    plt.title("line_chart")
    plt.ylabel("history_highest_overall_cost [-]")
    heatmap_df["colormap"] = pd.Categorical(heatmap_df["colormap"], categories=["i_want_hue", "mokole", "set1", "oranges", "purple2", "yellow_red"])
    heatmap_df.sort_values("colormap", inplace=True)
    heatmap_df.boxplot(column=dependent_variable_name, by=["colormap"], showmeans=True)
    plt.title("heatmap")
    plt.ylabel("history_highest_overall_cost [-]")
    t4_df_merged.boxplot(column=dependent_variable_name, by=["visualization"])
    plt.ylabel("history_highest_overall_cost [-]")
    plt.title("line charts vs colorfields")
    print(f"===============DONE in for task 4==================")
    full_stats = {"cost_means_stats": {
        "total_costs_colormaps_means_stats": means_accuracy_colormap_stats_payload,
        "total_costs_by_viz_lc_or_hm": means_accuracy_viz_stats_payload,
        "total_costs_by_seq_or_quali": means_quali_seq_stats_payload
    },
        "time_means_stats": {
            "time_to_execute_colormaps": time_colormap_stats_payload,
            "time_by_viz_lc_or_h": time_viz_stats_payload,
            "time_by_seq_or_quali": time_quali_seq_stats_payload
        }}
    return full_stats


def main():
    df = read_data()
    eq_df, cvd_df, t1_df_merged, t2_df_merged, t3_df_merged, t4_df_merged, end_q_df = data_set_creator(df)
    common_users = get_user_intersection(t1_df_merged, t2_df_merged, t3_df_merged, t4_df_merged)
    # removes the members who aborted and have not completed the tasks till the end
    t1_common, t2_common, t3_common, t4_common = common_members_dfs(t1_df_merged, t2_df_merged, t3_df_merged,
                                                                    t4_df_merged, common_users)
    task1_stats = task_1_plotter(t1_common)
    plt.show()
    task2_stats = task_2_plotter(t2_common)
    plt.show()
    task3_stats = task_3_plotter(t3_common)
    plt.show()
    task4_stats = task_4_plotter(t4_common)
    plt.show()
    print(f"""results for task 1 are:
     { task1_stats}
    and results for task 2 are:
     {task2_stats}
    and results for task 3 are:
     {task3_stats}
     and results for task 4 are:
     {task4_stats}
    """ )


if __name__ == '__main__':
    main()
