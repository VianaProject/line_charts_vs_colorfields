import pathlib
from helpers.study_helpers.general_study_helpers import *
import pprint

current_dir = pathlib.Path(__file__).parent.absolute()


def read_data():
    filename = "./data/study_data/participant_data.csv"
    remove_first_and_last_lines(filename)
    processed_file_name = filename.replace(".csv", "_processed.csv")
    df = pd.read_csv(processed_file_name, delimiter="|")
    df = clean_raw_df(df)
    df.columns = ["userID", "stepName", "stepValue", "studyID", "sessionID", "timeBackend"]
    df = remove_invalid_submissions(df)
    return df


def task_1_plotter(t0_df_merged: pd.DataFrame):
    line_chart_df = t0_df_merged[t0_df_merged["visualization"] == "line_chart"]
    heatmap_df = t0_df_merged[t0_df_merged["visualization"] == "heatmap"]
    dependent_variable_name = "history_lowest_elec_cost"
    task_number = [i for i in list(locals().keys()) if i.__contains__("_df_merged")][0].split("_df_merged")[0].split("t")[1]
    lc_stats, h_stats = get_1d_stats_on_experiment(line_chart_df, heatmap_df, dependent_variable_name, task_number)
    # these are all the statistical tests
    # the statistics for each of the 1d data are stored in lc_stats for line_charts and in h_stats for heatmaps
    means_stats_payload = stats_means_accuracy(t0_df_merged, dependent_variable_name)
    time_stats_payload = stats_time(t0_df_merged)
    full_stats = {"normalized_costs_task1": means_stats_payload,
                  "time_stats_task1": time_stats_payload}
    return full_stats


def task_2_plotter(t1_df_merged: pd.DataFrame):
    line_chart_df = t1_df_merged[t1_df_merged["visualization"] == "line_chart"]
    heatmap_df = t1_df_merged[t1_df_merged["visualization"] == "heatmap"]
    dependent_variable_name = "history_lowest_overall_cost"
    task_number = [i for i in list(locals().keys()) if i.__contains__("_df_merged")][0].split("_df_merged")[0].split("t")[1]
    lc_stats, h_stats = get_1d_stats_on_experiment(line_chart_df, heatmap_df, dependent_variable_name, task_number)
    means_stats_payload = stats_means_accuracy(t1_df_merged, dependent_variable_name)
    time_stats_payload = stats_time(t1_df_merged)
    full_stats = {"normalized_costs_task1": means_stats_payload,
                  "time_stats_task1": time_stats_payload}
    return full_stats


def task_3_plotter(t2_df_merged: pd.DataFrame):
    line_chart_df = t2_df_merged[t2_df_merged["visualization"] == "line_chart"]
    heatmap_df = t2_df_merged[t2_df_merged["visualization"] == "heatmap"]
    dependent_variable_name = "history_lowest_overall_cost"
    task_number = [i for i in list(locals().keys()) if i.__contains__("_df_merged")][0].split("_df_merged")[0].split("t")[1]
    lc_stats, h_stats = get_1d_stats_on_experiment(line_chart_df, heatmap_df, dependent_variable_name, task_number)
    means_stats_payload = stats_means_accuracy(t2_df_merged, dependent_variable_name)
    time_stats_payload = stats_time(t2_df_merged)
    full_stats = {"normalized_costs_task1": means_stats_payload,
                  "time_stats_task1": time_stats_payload}
    return full_stats


def task_4_plotter(t3_df_merged: pd.DataFrame):
    line_chart_df = t3_df_merged[t3_df_merged["visualization"] == "line_chart"]
    heatmap_df = t3_df_merged[t3_df_merged["visualization"] == "heatmap"]
    dependent_variable_name = "history_highest_overall_cost"
    task_number = [i for i in list(locals().keys()) if i.__contains__("_df_merged")][0].split("_df_merged")[0].split("t")[1]
    lc_stats, h_stats = get_1d_stats_on_experiment(line_chart_df, heatmap_df, dependent_variable_name, task_number)
    means_stats_payload = stats_means_accuracy(t3_df_merged,  dependent_variable_name)
    time_stats_payload = stats_time(t3_df_merged)
    full_stats = {"normalized_costs_task1": means_stats_payload,
                  "time_stats_task1": time_stats_payload}
    return full_stats


def main():
    df = read_data()
    eq_df, cvd_df, t1_df_merged, t2_df_merged, t3_df_merged, t4_df_merged, end_q_df = data_set_creator(df)
    common_users = get_user_intersection(t1_df_merged, t2_df_merged, t3_df_merged, t4_df_merged)
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
